"""praproses.py: rangkaian praproses SIMUTEH (dipakai ulang mulai P5)."""
import json
from pathlib import Path

import cv2
import numpy as np

PARAM_BAWAAN = {
    "lebar": 640,            # sampling: lebar citra kerja (piksel)
    "gamma": 1.0,            # < 1 mencerahkan, > 1 menggelapkan
    "clahe_clip": 2.0,       # 0 berarti CLAHE tidak dipakai
    "clahe_tile": 8,
    "penapis": "median",     # "none", "rerata", "gaussian", "median"
    "kernel": 3,
    "sigma": 1.0,
    "tajam_k": 0.0,          # 0 berarti tanpa penajaman
}


def praproses(img_bgr, p=None):
    """
        Urutan: ubah ukuran -> gamma -> CLAHE kanal V -> redam derau ->
        tajamkan.
    """
    p = {**PARAM_BAWAAN, **(p or {})}

    if img_bgr is None:
        raise ValueError("img_bgr tidak boleh None")

    img = np.asarray(img_bgr).copy()
    if img.ndim == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # TODO 1: ubah ukuran agar lebar = p["lebar"], rasio aspek tetap,
    #         gunakan interpolation=cv2.INTER_AREA, simpan ke variabel img
    h, w = img.shape[:2]
    target_w = int(p["lebar"])
    if target_w > 0 and w != target_w:
        target_h = max(1, int(round(h * (target_w / float(w)))))
        img = cv2.resize(img, (target_w, target_h), interpolation=cv2.INTER_AREA)

    # TODO 2: bila p["gamma"] != 1, terapkan koreksi gamma dengan cv2.LUT
    if p["gamma"] != 1:
        gamma = float(p["gamma"])
        lut = np.power(np.linspace(0, 1, 256, dtype=np.float32), 1.0 / gamma) * 255.0
        lut = np.clip(lut, 0, 255).astype(np.uint8)
        img = cv2.LUT(img, lut)

    # TODO 3: bila p["clahe_clip"] > 0, ubah ke HSV, terapkan CLAHE pada
    #         kanal V saja, lalu kembalikan ke BGR
    if p["clahe_clip"] > 0:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        v = hsv[:, :, 2]
        clahe = cv2.createCLAHE(
            clipLimit=float(p["clahe_clip"]),
            tileGridSize=(int(p["clahe_tile"]), int(p["clahe_tile"]))
        )
        v_eq = clahe.apply(v)
        hsv[:, :, 2] = v_eq
        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # TODO 4: redam derau sesuai p["penapis"], p["kernel"], p["sigma"]
    penapis = str(p["penapis"]).lower()
    kernel = int(p["kernel"])
    sigma = float(p["sigma"])
    if penapis == "none":
        pass
    elif penapis == "rerata":
        k = max(1, kernel if kernel % 2 == 1 else kernel + 1)
        img = cv2.blur(img, (k, k))
    elif penapis == "gaussian":
        k = max(1, kernel if kernel % 2 == 1 else kernel + 1)
        img = cv2.GaussianBlur(img, (k, k), sigmaX=sigma, sigmaY=sigma)
    elif penapis == "median":
        k = max(1, kernel if kernel % 2 == 1 else kernel + 1)
        img = cv2.medianBlur(img, k)

    # TODO 5: bila p["tajam_k"] > 0, lakukan unsharp masking
    tajam_k = float(p["tajam_k"])
    if tajam_k > 0:
        blur = cv2.GaussianBlur(img, (0, 0), sigma)
        img = cv2.addWeighted(img, 1.0 + tajam_k, blur, -tajam_k, 0)

    return img


def simpan_param(p, path="../hasil/param_praproses.json"):
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        json.dump({**PARAM_BAWAAN, **p}, f, indent=2)
