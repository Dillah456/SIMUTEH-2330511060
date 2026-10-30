# Rundown Pengerjaan Evaluasi Praktikum P1-P4 Computer Vision (SIMUTEH)

Disusun dari dokumen *Petunjuk Praktikum Evaluasi P1-P4 Computer Vision*, Teknik Informatika UMMI.

## 1. Ringkasan

| Item | Keterangan |
|---|---|
| Bentuk | Praktikum individu berbasis studi kasus SIMUTEH, Python (Jupyter/Colab) |
| Batas pengumpulan | **Minggu, 1 November 2026** (LMS UMMI bila aktif, Google Form bila belum). Setelah itu ada presentasi |
| Bobot | 15% nilai akhir (komponen Praktikum/Portofolio) |
| SEED | 4 digit terakhir NIM (ubah di `buat_dataset_sintetis.py`) |
| Luaran | (1) Laporan PDF, (2) ZIP kode, (3) Slide PPTX, (4) Tautan repository GitHub |

**Nama berkas luaran**

- `Laporan_EvalP1-4_<NIM>_<Nama>.pdf` (maksimal 20 halaman tanpa lampiran)
- `Kode_EvalP1-4_<NIM>.zip` (berisi `notebook/`, `src/`, `requirements.txt`, `README.md`; folder `data/` tidak disertakan)
- `Slide_EvalP1-4_<NIM>.pptx` (10-12 slide)
- Repository `simuteh-<NIM>` dengan tag `v0.1-praproses`

## 2. Bobot Penilaian

| Komponen | Bobot | Estimasi waktu di dokumen |
|---|---|---|
| Bagian 1: lingkungan kerja dan formulasi masalah | 10% | 25 menit |
| Bagian 2: pembentukan citra dan ruang warna | 15% | 35 menit |
| Bagian 3: histogram dan perbaikan citra | 20% | 40 menit |
| Bagian 4: konvolusi dan penapisan spasial | **25%** | 50 menit |
| Bagian 5: integrasi rangkaian praproses | 15% | 30 menit + mandiri |
| Laporan dan slide | 10% | - |
| Repository dan reprodusibilitas | 5% | - |

Nilai Bagian 1-5 dihitung dari: ketepatan perhitungan dan konsep 30%, implementasi dan hasil kode 35%, analisis dan jawaban pertanyaan 35%.

## 3. Jadwal Pengerjaan yang Disarankan (Jumat 30 Okt - Minggu 1 Nov 2026)

> Perkiraan waktu mengikuti estimasi di dokumen, ditambah waktu untuk menulis laporan dan slide. Sesuaikan dengan kondisi Anda.

### Jumat malam, 30 Okt (sekitar 3 jam)

| Waktu | Kegiatan | Hasil |
|---|---|---|
| 0:00-0:25 | **Bagian 1**: buat repo `simuteh-<NIM>`, struktur folder, `requirements.txt` | Repo + commit pertama |
| | Salin `buat_dataset_sintetis.py` dan `utils_cv.py` ke `src/`, ubah SEED, jalankan generator | 60 citra di `data/sintetis/citra/` |
| | Jalankan Kode 1.1 di `B1_lingkungan.ipynb` | `b1_bgr_rgb.png` |
| 0:25-1:00 | Tulis problem statement, diagram pipeline 6 tahap (`b1_pipeline.png`), tabel risiko (Tabel 6) | Hasil Bagian 1 lengkap |
| | Jawab P1.1-P1.4, commit "B1: setup lingkungan dan formulasi masalah" | |
| 1:00-1:45 | **Bagian 2, lembar hitung manual** (butir a-f) dengan langkah, rumus, dan satuan | Foto/scan lembar hitung |
| 1:45-2:15 | Rencana akuisisi citra (Langkah 2.2) dalam satu tabel | Tabel rencana akuisisi |
| 2:15-3:00 | Kode 2.1 dan 2.2 (kanal, sampling, kuantisasi) di `B2_citra_warna.ipynb` | Panel 8 citra + tabel sampling/kuantisasi |

### Sabtu pagi-siang, 31 Okt (sekitar 4 jam)

| Waktu | Kegiatan | Hasil |
|---|---|---|
| 0:00-0:40 | Kode 2.3 (KB per kanal per kondisi), isi Tabel 8 | `b2_kb_kanal.csv` |
| | **Kerjakan sendiri** Langkah 2.6: ulangi untuk kelas ringan, panel kanal terbaik teh_021 dan teh_045 | |
| 0:40-1:10 | Jawab P2.1-P2.6, commit | Bagian 2 selesai |
| 1:10-1:50 | **Bagian 3, lembar hitung manual** (histogram, regang, ekualisasi tabel, operasi titik 8 bit) | Foto/scan lembar hitung |
| 1:50-2:30 | Kode 3.1 (diagnosis, Tabel 9) dan Kode 3.2 (perbaikan, Tabel 10, tata letak seperti Gambar 4) | `b3_histogram_5kondisi.png`, Tabel 9 dan 10 |
| 2:30-3:10 | Kode 3.3 (grid CLAHE, CLAHE kanal V vs tiap kanal BGR) | Tabel KB CLAHE + panel perbandingan |
| | **Kerjakan sendiri** Langkah 3.5: satu perbaikan per kondisi pada kelas berat dan ringan | Panel sebelum-sesudah 4 kondisi |
| 3:10-4:00 | Jawab P3.1-P3.6, commit | Bagian 3 selesai |

### Sabtu sore-malam, 31 Okt (sekitar 4 jam)

| Waktu | Kegiatan | Hasil |
|---|---|---|
| 0:00-0:40 | **Bagian 4, lembar hitung manual** (rerata/Gaussian/median, kernel tajam, padding) | Foto/scan lembar hitung |
| 0:40-1:20 | Kode 4.1 (verifikasi konvolusi) dan modifikasi `konvolusi_sejati` | Keluaran Kode 4.1 |
| 1:20-2:10 | Kode 4.2 (6 penapis x 5 derau), isi Tabel 11, buat grafik PSNR dan waktu | `b4_tabel_penapis.csv` + grafik |
| 2:10-2:50 | Kode 4.3 (kernel median vs dI/KB) dan Kode 4.4 (urutan penajaman) | Grafik dI + crop bercak |
| 2:50-3:20 | **Kerjakan sendiri** Langkah 4.6: PSNR 12 citra kondisi normal sebelum/sesudah | Tabel PSNR |
| 3:20-4:00 | Jawab P4.1-P4.7, commit | Bagian 4 selesai |

### Minggu pagi-siang, 1 Nov (sekitar 4 jam, **hari batas pengumpulan**)

| Waktu | Kegiatan | Hasil |
|---|---|---|
| 0:00-1:00 | **Bagian 5**: lengkapi 5 TODO di `src/praproses.py`, tentukan parameter dari temuan Bagian 2-4, simpan `param_praproses.json` | Modul praproses |
| 1:00-1:30 | Kode 5.2 (Tabel 12), uji bercak palsu kelas sehat (Langkah 5.3) | Tabel 12 + panel sebelum/sesudah |
| 1:30-1:50 | Tabel 13 (justifikasi), gambar ulang diagram dengan parameter final, jawab P5.1-P5.5 | Bagian 5 selesai |
| 1:50-2:30 | Restart & Run All semua notebook, README, commit, `git tag v0.1-praproses`, `git push --tags` | Tag di repository |
| 2:30-3:30 | Susun laporan PDF (Arial 11, spasi 1,5), lampirkan lembar hitung | Laporan |
| 3:30-4:00 | Slide 10-12 (huruf minimal 20 pt), ZIP kode, unggah ke LMS/Google Form | **Terkumpul** |

## 4. Rincian Tiap Bagian

### Bagian 1: Lingkungan Kerja dan Formulasi Masalah (Pertemuan 1)

**Yang dikerjakan**

1. Repo `simuteh-<NIM>`, struktur folder sesuai C.2, tambahkan dosen sebagai kolaborator.
2. `pip install opencv-python numpy matplotlib scikit-image pandas pillow`, catat versi ke `requirements.txt`.
3. Salin kode awal ke `src/`, ubah SEED, jalankan generator dari folder utama repository.
4. Kode 1.1 di `notebook/B1_lingkungan.ipynb`.
5. **Kerjakan sendiri:** problem statement (kerangka P1), diagram pipeline 6 tahap, tabel risiko (6 aspek).

**Hasil wajib:** keluaran Kode 1.1 dan `b1_bgr_rgb.png`; problem statement, diagram, tabel risiko; repo dengan minimal satu commit.

**Pertanyaan:** P1.1-P1.4 (semantic gap, tiga sumber variasi, BGR vs RGB, pihak yang diuntungkan/dirugikan).

### Bagian 2: Pembentukan Citra dan Ruang Warna (Pertemuan 2)

**Yang dikerjakan**

1. Lembar hitung manual (Tabel 7): ukuran bayangan bercak (Z = 300 dan 600 mm), jarak maksimum untuk ≥ 10 piksel, ukuran setelah diperkecil ke lebar 640, memori citra dan 300 foto, konversi keabuan dan Hue. Tuliskan langkah dan satuan.
2. **Kerjakan sendiri:** tabel rencana akuisisi (jarak dan sudut, resolusi minimum, alas dan acuan ukuran, kondisi cahaya, jumlah citra per kelas, penamaan berkas, izin, penghapusan EXIF, larangan wajah).
3. Kode 2.1 (pisah kanal B, G, R, Gray, H, S, V dan hitung KB), Kode 2.2 (sampling dan kuantisasi), Kode 2.3 (rerata KB per kondisi, Tabel 8).
4. **Kerjakan sendiri:** ulangi untuk kelas ringan, tampilkan kanal terbaik teh_021 dan teh_045.

**Pertanyaan:** P2.1-P2.6.

### Bagian 3: Histogram dan Perbaikan Citra (Pertemuan 3)

**Yang dikerjakan**

1. Lembar hitung manual: histogram matriks 4x4, peregangan kontras 0-7, ekualisasi (tabel r, n, PDF, CDF, 7xCDF, s), operasi titik 8 bit (negatif, kontras 1,4r - 30 dengan clipping, gamma 0,6 dan 1,8).
2. Kode 3.1 (diagnosis 5 kondisi + 5 citra ringan, Tabel 9).
3. Kode 3.2 (9 metode pada teh_045, Tabel 10, tata letak Gambar 4).
4. Kode 3.3 (grid clip x tile, CLAHE kanal V vs tiap kanal BGR).
5. **Kerjakan sendiri:** satu perbaikan per kondisi (gelap, terang, kontras rendah, bayangan) pada kelas berat dan ringan.

**Pertanyaan:** P3.1-P3.6.

### Bagian 4: Konvolusi dan Penapisan Spasial (Pertemuan 4), bobot terbesar

**Yang dikerjakan**

1. Lembar hitung manual: rerata, Gaussian, median pada P 4x4; kernel tajam pada Q (perhatikan clipping); tiga jenis padding pada baris [12, 30, 45, 70].
2. Kode 4.1: bandingkan konvolusi manual dengan `cv2.filter2D`, modifikasi fungsi menjadi konvolusi sejati.
3. Kode 4.2: 6 penapis x 5 derau, ukur PSNR, waktu, KB. Isi Tabel 11 (Gaussian 20 dan garam-merica 4%) dan buat grafik seluruh hasil.
4. Kode 4.3: pengaruh ukuran kernel median pada dI dan KB (20 citra ringan), grafik, dan crop satu bercak.
5. Kode 4.4: urutan redam-tajamkan vs tajamkan-redam.
6. **Kerjakan sendiri:** PSNR 12 citra kondisi normal sebelum dan sesudah penapisan.

**Pertanyaan:** P4.1-P4.7.

### Bagian 5: Integrasi Rangkaian Praproses

**Yang dikerjakan**

1. **Kerjakan sendiri:** lengkapi 5 TODO di `src/praproses.py` (ubah ukuran dengan INTER_AREA, gamma dengan LUT, CLAHE kanal V, redam derau, unsharp masking).
2. Kode 5.2: simpan `param_praproses.json`, bandingkan KB sebelum dan sesudah pada 40 citra berbercak (Tabel 12). Ganti `KANAL` sesuai kanal terbaik dari Bagian 2.
3. **Kerjakan sendiri:** uji bercak palsu pada 20 citra kelas sehat (simpangan baku daun sebelum/sesudah, panel per kondisi).
4. Tabel 13 (justifikasi) dan diagram praproses dengan parameter final.
5. Restart & Run All, perbarui README (cara menjalankan, SEED, ringkasan hasil), commit, `git tag v0.1-praproses`, `git push --tags`.

**Pertanyaan:** P5.1-P5.5 (termasuk dua nilai AIK).

## 5. Laporan (maksimal 20 halaman tanpa lampiran)

Format: Arial 11, spasi 1,5, rata kiri-kanan. Judul tabel **di atas** tabel, judul gambar **di bawah** gambar, keduanya bernomor.

1. Halaman judul: judul, nama, NIM, kelas, SEED, tautan repository
2. Pendahuluan: ringkasan kasus, problem statement, tujuan
3. Data dan lingkungan kerja: SEED, jumlah per kelas/kondisi, ringkasan `persen_bercak`, rencana akuisisi, versi pustaka
4. Hasil dan analisis Bagian 1-5: tabel dan gambar bernomor, jawab seluruh pertanyaan dengan kode (P1.1, P1.2, ...)
5. Rangkaian praproses akhir: diagram, parameter final, justifikasi
6. Kesimpulan dan rencana Pertemuan 5
7. Refleksi: responsible computer vision, nilai AIK, pemakaian AI generatif (bila ada)
8. Daftar pustaka dan lampiran: lembar hitung manual, tangkapan layar

## 6. Slide (10-12 slide, sekitar 5 menit presentasi)

Huruf minimal 20 pt, utamakan gambar dan grafik, satu pesan utama per slide.

| Slide | Isi |
|---|---|
| 1 | Judul, nama, NIM, tautan repository |
| 2 | Masalah dan pengguna |
| 3 | Pipeline SIMUTEH dan posisi P1-P4 |
| 4 | Data: contoh citra lima kondisi dan tiga kelas |
| 5 | Syarat akuisisi (jarak dan resolusi dari lembar hitung) |
| 6 | Kanal warna terpilih (grafik KB per kanal per kondisi) |
| 7 | Diagnosis dan perbaikan (histogram sebelum/sesudah, KB tiap metode) |
| 8 | Penapisan (PSNR, waktu, pengaruh median pada bercak kecil) |
| 9 | Rangkaian praproses (diagram dan parameter final) |
| 10 | Hasil integrasi (KB sebelum/sesudah, uji bercak palsu) |
| 11 | Tanggung jawab dan keterbatasan |
| 12 | Kesimpulan dan langkah berikutnya (tiga temuan utama, rencana P5) |

## 7. Daftar Periksa Sebelum Mengumpulkan

- [ ] SEED sama dengan 4 digit terakhir NIM dan tercantum di laporan
- [ ] Semua notebook berhasil dengan **Restart & Run All**
- [ ] Semua pertanyaan P1.1 sampai P5.5 dijawab dengan merujuk bukti sendiri
- [ ] Lembar hitung manual Bagian 2, 3, 4 terlampir (langkah, bukan hanya jawaban akhir)
- [ ] Semua langkah **Kerjakan sendiri** ada hasilnya
- [ ] Format laporan: Arial 11, spasi 1,5, rata kiri-kanan, judul tabel di atas, judul gambar di bawah
- [ ] Nama berkas sesuai ketentuan; tag `v0.1-praproses` sudah di-push
- [ ] Dosen menjadi kolaborator repository
- [ ] Folder `data/` tidak ikut di ZIP
- [ ] Bagian kode atau teks yang dibantu AI generatif dicantumkan di refleksi, dan Anda bisa menjelaskan setiap baris dan angka

## 8. Catatan Penting dari Dokumen

- Ini evaluasi **individu**. Diskusi konsep boleh, tetapi kode, angka, dan analisis harus milik sendiri. Hasil identik dengan mahasiswa lain akan diperiksa.
- Notebook diletakkan di `notebook/`, sehingga jalur di dalam kode diawali `../`.
- Jalankan generator dari **folder utama repository**, bukan dari dalam `src/`.
- Kondisi cahaya berulang setiap 5 citra (normal, gelap, terang, kontras_rendah, bayangan). Citra normal: teh_001, teh_006, teh_011, dan seterusnya.
- Ukuran KB dan dI punya keterbatasan; menemukan keterbatasan itu bagian dari analisis yang dinilai.
- Simpan semua artefak: `praproses.py` dan `param_praproses.json` dipakai lagi pada Pertemuan 5.

## 9. Tantangan Opsional (nilai tambah sesuai kebijakan dosen)

- Koreksi gamma otomatis dari rerata intensitas citra, dibandingkan dengan gamma tetap
- KB pada kanal a dan b CIELAB, dibandingkan dengan kanal terbaik Bagian 2
- Mempercepat konvolusi manual tanpa perulangan Python (misalnya `sliding_window_view`) dan bandingkan waktunya
