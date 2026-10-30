"""praproses.py: rangkaian praproses SIMUTEH (dipakai ulang mulai P5).""" 
import json 
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
    # TODO 1: ubah ukuran agar lebar = p["lebar"], rasio aspek tetap, 
    #         gunakan interpolation=cv2.INTER_AREA, simpan ke variabel img 
    # TODO 2: bila p["gamma"] != 1, terapkan koreksi gamma dengan cv2.LUT 
    # TODO 3: bila p["clahe_clip"] > 0, ubah ke HSV, terapkan CLAHE pada 
    #         kanal V saja, lalu kembalikan ke BGR 
    # TODO 4: redam derau sesuai p["penapis"], p["kernel"], p["sigma"] 
    # TODO 5: bila p["tajam_k"] > 0, lakukan unsharp masking 
    return img 
def simpan_param(p, path="../hasil/param_praproses.json"): 
    with open(path, "w") as f: 
        json.dump({**PARAM_BAWAAN, **p}, f, indent=2) 