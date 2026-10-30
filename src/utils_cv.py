"""utils_cv.py: fungsi bantu yang dipakai ulang sepanjang semester."""
import cv2
import numpy as np
import matplotlib.pyplot as plt


def baca(path):
    """Membaca citra dan langsung memberi pesan jelas bila gagal."""
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Citra tidak ditemukan: {path}")
    return img


def tampil(daftar, judul, baris=1, ukuran=(14, 4)):
    """Menampilkan beberapa citra berdampingan. Citra 3 kanal dianggap BGR."""
    kolom = int(np.ceil(len(daftar) / baris))
    plt.figure(figsize=ukuran)
    for i, (im, jd) in enumerate(zip(daftar, judul)):
        plt.subplot(baris, kolom, i + 1)
        if im.ndim == 3:
            plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
        else:
            plt.imshow(im, cmap="gray", vmin=0, vmax=255)
        plt.title(jd)
        plt.axis("off")
    plt.tight_layout()


def kontras_bercak(kanal, mask_daun, mask_bercak):
    """KB = |rerata bercak - rerata daun sehat| / simpangan baku daun sehat.
    Makin besar KB, makin mudah bercak dipisahkan dari daun sehat."""
    k = kanal.astype(np.float64)
    sehat = (mask_daun > 0) & (mask_bercak == 0)
    bercak = mask_bercak > 0
    if bercak.sum() == 0:
        return float("nan")
    return abs(k[bercak].mean() - k[sehat].mean()) / (k[sehat].std() + 1e-6)


def statistik(gray):
    """Ringkasan statistik intensitas untuk mendiagnosis mutu citra."""
    return {"rerata": round(float(gray.mean()), 1),
            "simpangan_baku": round(float(gray.std()), 1),
            "min": int(gray.min()), "maks": int(gray.max()),
            "persen_gelap": round(100 * float((gray < 50).mean()), 1),
            "persen_terang": round(100 * float((gray > 205).mean()), 1)}


# --- Tambahan (tidak ada di Lampiran B) ---------------------------------
def tampil_hist(img, judul, ax_img, ax_hist):
    """Menampilkan citra aras keabuan beserta histogram dan CDF-nya
    (dari Modul 3 Kode A1; dipakai untuk tata letak seperti Gambar 4)."""
    hist = np.bincount(img.ravel(), minlength=256)
    cdf = hist.cumsum() / img.size
    ax_img.imshow(img, cmap="gray", vmin=0, vmax=255)
    ax_img.set_title(judul)
    ax_img.axis("off")
    ax_hist.bar(range(256), hist, width=1, color="0.4")
    ax_hist.set_xlim(0, 255)
    ax_hist.set_xlabel("Intensitas")
    ax_hist.set_ylabel("Jumlah piksel")
    ax2 = ax_hist.twinx()
    ax2.plot(cdf, color="tab:red")
    ax2.set_ylim(0, 1.05)
