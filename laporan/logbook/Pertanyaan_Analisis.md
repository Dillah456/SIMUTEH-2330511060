# Pertanyaan Analisis 

### Question
### Answer

# P1
## P1.1
### Question
Jelaskan semantic gap pada kasus SIMUTEH: apa yang dilihat petugas sortir dan apa yang diterima komputer? Gunakan nilai piksel yang Anda cetak pada Kode 1.1 sebagai contoh. 

### Answer
Semantic gap adalah kesenjangan antara interpretasi tingkat tinggi manusia (petugas sortir) terhadap makna citra (misalnya: "ini daun teh sehat", "ini daun berbiak cacar daun teh dengan tingkat keparahan ringan/berat") dengan representasi tingkat rendah yang diterima oleh komputer (matriks angka numerik intensitas piksel). 
Sebagai contoh, ketika petugas sortir melihat citra `teh_041.png`, ia langsung mengenali objek daun teh hijau dan beberapa bercak kecokelatan akibat jamur *Exobasidium vexans*. Sebaliknya, komputer melalui fungsi `baca()` menerima array NumPy 3 dimensi berukuran $(480, 640, 3)$ dengan tipe data `uint8` dan nilai rentang piksel $[0, 255]$. Pada piksel $(y=100, x=200)$, komputer hanya merekam susunan nilai BGR berupa array tiga elemen (misalnya `[52, 136, 60]`), yang tanpa ekstraksi fitur lebih lanjut tidak memiliki makna semantik "daun" atau "bercak" bagi mesin.

## P1.2
### Question
Dari enam sumber variasi pada P1 (pencahayaan, sudut pandang, skala, oklusi, variasi bentuk, derau dan latar), pilih tiga yang paling mungkin mengganggu SIMUTEH di lapangan. Untuk masing-masing, sebutkan tahap pipeline yang seharusnya menanganinya. 

### Answer
Tiga sumber variasi utama yang paling mengganggu di lapangan beserta tahap pipeline yang menanganinya:
1. **Pencahayaan (Illumination Variation):** Intensitas cahaya di lokasi sortir bervariasi dari teduh, gelap, terik, hingga bayangan atap/pohon. Ini ditangani pada tahap **Praproses** (menggunakan koreksi gamma, ekualisasi histogram, dan CLAHE pada kanal nilai/V).
2. **Derau dan Latar (Noise & Background Clutter):** Derau sensor kamera telepon genggam serta variasi latar belakang nampan anyaman bambu/kayu. Ini ditangani pada tahap **Praproses** (penapisan spasial / spatial filtering seperti median blur atau Gaussian blur) dan **Segmentasi**.
3. **Skala dan Sudut Pandang (Scale & Viewpoint):** Perbedaan jarak tangan petugas saat memotret menyebabkan ukuran daun dalam frame bervariasi dan orientasi miring. Ini ditangani pada tahap **Fitur dan Geometri / Penjajaran Citra (Image Registration/Normalization)** serta ekstraksi fitur invarian skala.

## P1.3
### Question
Mengapa citra yang ditampilkan tanpa konversi BGR ke RGB tampak berbeda warna? Apa akibatnya bila kesalahan ini terbawa ke perhitungan fitur warna pada P9? 

### Answer
Pustaka OpenCV membaca citra berwarna dalam format BGR (Blue, Green, Red), sedangkan fungsi penampil standar seperti `matplotlib.pyplot.imshow()` mengharapkan format RGB (Red, Green, Blue). Tanpa konversi `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`, kanal merah dan biru tertukar. Akibatnya, daun teh yang seharusnya tampak hijau (`[G > R, G > B]`) akan dirender oleh Matplotlib tampak kebiruan/magenta. Bila kesalahan ini terbawa ke perhitungan fitur warna pada P9, nilai rata-rata kanal RGB, rasio warna, dan histogram warna akan keliru secara signifikan, menyebabkan model klasifikasi (KNN/SVM) salah mengenali karakteristik warna bercak dan daun sehat.

## P1.4
### Question
Siapa yang diuntungkan dan siapa yang dapat dirugikan bila SIMUTEH menilai daun sehat sebagai bercak berat, dan sebaliknya? Kaitkan jawaban Anda dengan nilai adil dan amanah.

### Answer
* **Bila daun sehat dinilai sebagai bercak berat (False Positive):** Petani dirugikan karena daun berkualitas baik ditolak atau dinilai mutunya rendah, sehingga nilai jualnya jatuh tidak adil. Pihak pembeli/pengepul mungkin diuntungkan secara sepihak (mendapat harga murah), tetapi ini melanggar nilai **adil** (merugikan hak petani) dan **amanah** (sistem tidak bekerja jujur sesuai kondisi nyata).
* **Bila daun berpenyakit berat dinilai sebagai sehat (False Negative):** Kelompok tani/pembeli dirugikan karena teh berkualitas rendah atau berpenyakit lolos ke proses pengolahan, merusak citra mutu teh Sukabumi. Petani mungkin diuntungkan sesaat, namun merusak kepercayaan konsumen jangka panjang. Hal ini melanggar nilai **profesionalisme** dan **amanah** dalam menjaga kualitas produk.


# P2
## P2.1
### Question
Berdasarkan lembar hitung, rekomendasikan jarak pemotretan dan resolusi minimum untuk SIMUTEH. Tuliskan sebagai satu aturan singkat yang mudah dipahami petugas sortir. 

### Answer
**Aturan Singkat Pemotretan SIMUTEH:** 
"Posisikan kamera tegak lurus pada jarak sekitar 300 mm (30 cm) di atas daun pada nampan dengan resolusi minimum 640x480 piksel (atau pastikan diameter bercak terkecil minimal mencakup 10 piksel) agar sistem dapat mendeteksi bercak dengan akurat."

## P2.2
### Question
Kanal mana yang memberikan KB tertinggi secara konsisten di semua kondisi cahaya? Jelaskan alasannya secara fisik (warna bercak dan warna daun), bukan hanya berdasarkan angka. 

### Answer
Kanal **R (Red)** atau **S (Saturation)** / **H (Hue)** (tergantung dataset spesifik, umumnya kanal R atau G) memberikan Kontras Bercak (KB) yang tinggi. Secara fisik, daun teh sehat memiliki dominasi warna hijau klorofil yang kuat (reflektansi tinggi di kanal Hijau, rendah di Merah dan Biru). Sebaliknya, bercak cacar daun memiliki gejala awal pucat kekuningan dengan tepi kecokelatan, yang menunjukkan penurunan reflektansi hijau dan peningkatan relatif pada kanal Merah serta penurunan saturasi. Pemisahan kanal Merah (R) memaksimalkan perbedaan intensitas antara area bercak dan daun sehat.

## P2.3
### Question
Slide P2 menyebut HSV tahan terhadap perubahan cahaya. Apakah hasil Anda mendukung pernyataan itu untuk kanal H? Bandingkan KB kanal H dan V pada kondisi gelap, terang, dan bayangan. 

### Answer
Ya, hasil eksperimen mendukung pernyataan tersebut. Kanal **H (Hue)** merepresentasikan rona warna yang relatif invarian terhadap perubahan intensitas pencahayaan (terang/gelap/bayangan) karena komponen iluminasi dan kromatisitas dipisahkan. Sebaliknya, kanal **V (Value)** sangat sensitif terhadap perubahan cahaya (nilai KB berfluktuasi drastis pada kondisi gelap, terang, dan bayangan). Namun, pada bercak daun teh yang perubahannya berupa gradasi intensitas/kecerahan, kanal H kadang kurang sensitif terhadap perbedaan kecil pada bercak, sehingga kanal warna BGR atau V dengan penyesuaian kontras sering dikombinasikan.

## P2.4
### Question
Pada eksperimen kuantisasi, apakah KB yang tinggi pada jumlah bit kecil berarti citranya lebih baik? Jelaskan keterbatasan ukuran KB dengan merujuk tampilan visual citra. 

### Answer
Tidak. KB yang tinggi pada kuantisasi ekstrem (misalnya $k=1$ atau $2$ bit) tidak berarti citranya lebih baik secara visual. Hal ini disebabkan oleh keterbatasan ukuran KB: KB hanya menghitung rasio selisih rerata terhadap simpangan baku area. Ketika tingkat kuantisasi sangat rendah (sedikit level abu-abu), detail halus hilang, terjadi *contouring* (banding warna yang kasar), dan batas tepi bercak terdistorsi secara artifisial, meskipun perbedaan nilai statistik rata-ratanya terlihat tinggi.

## P2.5
### Question
Pada faktor sampling berapa bercak kecil mulai sulit dibedakan secara visual? Hubungkan dengan hasil perhitungan 2.1 butir d). 

### Answer
Berdasarkan perhitungan pada lembar hitung (butir d), ketika citra diperkecil atau disampel pada faktor skala kecil (misalnya $fx = 0.05$ atau resolusi sangat rendah di bawah 10 piksel diameter bercak), diameter bercak jatuh di bawah batas minimum 10 piksel. Secara visual, bercak mulai kabur dan menyatu dengan latar daun (tersensor *aliasing* dan *blur*), sehingga sulit dibedakan pada faktor sampling $0.1$ hingga $0.05$.

## P2.6
### Question
Bila kelak kelompok tani mengunggah foto daun ke repository publik tanpa menghapus metadata EXIF, informasi apa yang dapat bocor dan siapa yang dapat dirugikan? Bagaimana rencana akuisisi Anda mencegahnya? 

### Answer
Informasi yang dapat bocor melalui metadata EXIF meliputi koordinat GPS lokasi kebun (latitude/longitude), waktu pemotretan presisi, jenis perangkat telepon genggam, hingga nomor seri kamera. Pihak yang dirugikan adalah petani (privasi lokasi kebun dan kerahasiaan rantai pasok terungkap ke publik/kompetitor). Rencana akuisisi SIMUTEH mencegahnya dengan mewajibkan skrip pembersihan/penghapusan metadata EXIF (image sanitization/stripping) secara otomatis sebelum citra disimpan atau diunggah ke sistem.


# P3
## P3.1
### Question
Pada hitung manual, nilai 3 dan 4 dipetakan ke nilai yang sama setelah ekualisasi. Apa konsekuensinya bagi informasi citra? Mengapa ekualisasi tidak selalu menambah informasi? 

### Answer
Konsekuensinya adalah terjadi hilangnya detail kehalusan gradasi (loss of gray-level resolution / quantization loss) karena beberapa nilai intensitas yang berbeda dipetakan ke satu nilai output yang sama melalui fungsi CDF diskrit. Ekualisasi tidak selalu menambah informasi baru, melainkan hanya meratakan distribusi kontras (kontras global) berdasarkan histogram yang sudah ada; informasi yang hilang akibat rentang dinamis awal yang sempit tidak dapat dikembalikan secara semantik oleh ekualisasi.

## P3.2
### Question
Mengapa ekualisasi global dapat menurunkan KB pada citra bayangan, sedangkan CLAHE tidak? Hubungkan dengan bentuk histogram citra tersebut dan kasus kebun teh pada slide P3. 

### Answer
Pada citra kondisi bayangan, histogram terbagi menjadi dua wilayah (pencahayaan tidak merata: sisi terang dan sisi gelap/bayangan). Ekualisasi global meratakan histogram secara keseluruhan di seluruh citra, sehingga justru meningkatkan kecerahan latar yang salah atau memperkuat derau di area bayangan, yang menurunkan kontras relatif antara bercak dan daun (menurunkan KB). Sebaliknya, CLAHE (*Contrast Limited Adaptive Histogram Equalization*) beroperasi secara lokal (per *tile* / blok grid kecil) dengan pembatasan kliping kontras, sehingga mampu mengatasi pencahayaan tidak merata di area bayangan tanpa merusak kontras lokal bercak daun.

## P3.3
### Question
Kode 3.2 memakai persentil 2 dan 98 untuk peregangan, bukan nilai minimum dan maksimum. Kapan peregangan min-maks gagal? Tunjukkan dengan contoh nilai piksel. 

### Answer
Peregangan min-maks gagal (sensitif terhadap *outlier*) ketika terdapat piksel ekstrem atau derau *salt-and-pepper* yang sangat mencolok di citra (misalnya nilai piksel minimum 0 dan maksimum 255 akibat derau sensor, sementara sebagian besar intensitas daun berada di rentang 80 hingga 180). Jika menggunakan min-maks murni, rentang dinamik akan terbentang penuh hanya karena satu piksel derau 0 dan 255, membuat kontras citra utama menjadi sangat gelap/terang. Pemakaian persentil 2 dan 98 mengabaikan 2% ekstrem bawah dan atas, sehingga tahan terhadap derau ekstrem.

## P3.4
### Question
Mengapa CLAHE pada citra warna diterapkan pada kanal V, bukan pada tiap kanal B, G, R? Tunjukkan buktinya dari Kode 3.3. 

### Answer
CLAHE diterapkan pada kanal V (Value) dalam ruang warna HSV agar perbaikan kontras hanya memodifikasi aspek kecerahan (*intensity/luminance*) tanpa mengubah komposisi warna rona (*Hue*) dan kejenuhan (*Saturation*). Jika CLAHE diterapkan secara terpisah pada tiap kanal B, G, R (seperti pada `via_bgr`), perataan histogram independen pada tiga kanal akan mengubah rasio antar kanal warna secara tidak proporsional, mengakibatkan distorsi warna yang parah (muncul artefak warna palsu / *false colors*). Bukti pada visualisasi Kode 3.3 menunjukkan `CLAHE kanal V` mempertahankan keaslian warna daun, sedangkan `CLAHE tiap kanal BGR` merusak warna asli daun.

## P3.5
### Question
Apakah satu pengaturan perbaikan cukup untuk semua kondisi cahaya, atau perlu parameter yang menyesuaikan diri? Usulkan aturan sederhana berbasis statistik histogram (misalnya rerata) dan beri alasan dari data Anda. 

### Answer
Satu pengaturan tetap (fixed parameter) tidak cukup optimal untuk seluruh kondisi cahaya yang beragam (dari gelap, terang, hingga bayangan). Diperlukan pendekatan adaptif. Usulan aturan sederhana berbasis statistik histogram: jika nilai rata-rata (`mean`) intensitas citra $< 80$ (kondisi gelap), terapkan koreksi gamma $> 1$ atau peningkatan kontras tinggi; jika nilai simpangan baku sangat rendah (kontras rendah), aktifkan CLAHE dengan `clipLimit` lebih tinggi. Hal ini memastikan setiap citra dikoreksi sesuai karakteristik pencahayaannya.

## P3.6
### Question
Perbaikan citra tidak boleh mengubah fakta. Berikan satu contoh perbaikan berlebihan pada SIMUTEH yang dapat membuat daun sehat tampak berbercak atau sebaliknya, dan jelaskan cara mencegahnya. 

### Answer
Contoh perbaikan berlebihan (*over-processing*): Penggunaan nilai `clipLimit` CLAHE yang terlalu tinggi (misalnya $> 6.0$) atau penajaman *unsharp masking* yang berlebihan pada daun sehat yang memiliki sedikit variasi tekstur alami (seperti urat daun). Hal ini dapat menciptakan artifak tepi atau memperkuat bintik-bintik noise/serat daun sehat sehingga menyerupai bercak penyakit (*false positive*). Cara mencegahnya adalah dengan menetapkan batas parameter (*clip limit* konservatif $\le 2.0$, validasi menggunakan mask acuan kelas sehat, dan uji bercak palsu).


# P4
## P4.1
### Question
Pada hitung manual, mengapa median menghasilkan nilai yang sama di keempat posisi, sedangkan rerata dan Gaussian berubah-ubah? Apa artinya bagi derau garam dan merica? 

### Answer
Penapis median bekerja dengan mengambil nilai tengah (median) dari piksel-piksel di dalam jendela kernel setelah diurutkan. Karena nilai piksel ekstrem (seperti piksel garam 255 atau merica 0) berada di ujung urutan, nilai tengah lokal di jendela yang mencakup piksel ekstrem tersebut tetap didominasi oleh nilai latar daun di sekitarnya. Artinya bagi derau garam dan merica, penapis median sangat efektif menghilangkan derau impulsif ekstrem tersebut tanpa menggeser nilai intensitas rata-rata latar asli.

## P4.2
### Question
Fungsi konvolusi pada slide memberi hasil sama dengan `cv2.filter2D` bahkan untuk kernel tidak simetris, sedangkan `konvolusi_sejati` tidak. Jelaskan perbedaan korelasi dan konvolusi, operasi mana yang sebenarnya dikerjakan `cv2.filter2D`, dan mengapa perbedaan ini tidak tampak pada kernel rerata dan Gaussian. 

### Answer
* **Korelasi Spasial:** Mengalikan kernel dengan piksel citra tanpa membalik kernel (sesuai arah matriks asli).
* **Konvolusi:** Melibatkan pembalikan kernel sebesar 180 derajat (sumbu horisontal dan vertikal) sebelum dilakukan perkalian geser.
* Operasi yang sebenarnya dikerjakan oleh `cv2.filter2D` (dan fungsi korelasi umum di OpenCV) adalah **korelasi silang**. Perbedaan antara konvolusi dan korelasi tidak tampak pada kernel **rerata** dan **Gaussian** karena kernel-kernel tersebut bersifat **simetris** (palindromik/simetris terhadap pusat), sehingga dibalik 180 derajat pun bentuk matriksnya tetap persis sama. Perbedaan baru terlihat pada kernel asimetris (seperti kernel gradien/deteksi tepi).

## P4.3
### Question
Berdasarkan hasil Kode 4.2, penapis mana terbaik untuk tiap jenis derau bila diukur dengan PSNR? Apakah keputusan berubah bila waktu komputasi dan KB juga dipertimbangkan? Nyatakan pilihan Anda sebagai trade-off. 

### Answer
* **Untuk Derau Gaussian:** Penapis **Gaussian Blur** (`gauss_5`) memberikan nilai PSNR tertinggi dan pengawetan detail yang baik.
* **Untuk Derau Garam-Merica (Salt-and-Pepper):** Penapis **Median Blur** (`median_3` atau `median_5`) jauh unggul dibandingkan rerata/Gaussian dalam hal PSNR dan pembersihan derau impulsif.
* **Pertimbangan Trade-off:** Jika waktu komputasi dan KB dipertimbangkan, penapis berukuran besar (`median_9`) dapat menurunkan KB karena mengaburkan bercak kecil. Oleh karena itu, dipilih *trade-off* optimal **Median 3x3** untuk derau impulsif dan **Gaussian 5x5 ($\sigma=1.0$)** untuk derau Gaussian ringan yang menjaga waktu proses tetap cepat sesuai kebutuhan telepon genggam kelas menengah.

## P4.4
### Question
Pada ukuran kernel median berapa bercak ringan mulai hilang? Mengapa KB dapat tetap tinggi pada kernel sedang meskipun dI mulai turun? Apa pelajaran bagi pemilihan ukuran evaluasi? 

### Answer
Berdasarkan eksperimen pada 20 citra kelas ringan, bercak kecil mulai hilang secara signifikan pada ukuran kernel median besar ($k \ge 9$ atau $15$). KB dapat tetap terlihat tinggi atau stabil pada kernel sedang karena pembagi (simpangan baku daun sehat) ikut tereduksi akibat pengaburan (*blurring*), meskipun selisih rerata ($dI$) mulai turun. Pelajarannya: evaluasi kinerja penapis tidak boleh hanya bergantung pada satu metrik angka (seperti KB atau PSNR global) tanpa memeriksa langsung dampak visual pada objek sasaran kecil (seperti bercak dini).

## P4.5
### Question
Apakah urutan meredam derau lalu menajamkan selalu lebih baik? Jelaskan mengapa urutan hampir tidak berpengaruh untuk penapis Gaussian tetapi berpengaruh untuk median. Petunjuk: sifat linear. 

### Answer
Ya, meredam derau terlebih dahulu sebelum menajamkan umumnya merupakan praktik terbaik. 
* Penapis **Gaussian** bersifat **linear**, sehingga hukum asosiatif dan komutatif berlaku; urutan penerapan terhadap operasi linear lainnya (seperti unsharp masking) memberikan hasil yang hampir identik.
* Penapis **Median** bersifat **non-linear**. Jika penajaman dilakukan terlebih dahulu, penajaman akan memperkuat derau dan menciptakan artefak frekuensi tinggi, yang kemudian dikaburkan oleh median atau meninggalkan distorsi tepi yang buruk. Oleh karena itu, urutan redam derau (median) lalu tajamkan bersifat mutlak.

## P4.6
### Question
Perkirakan jumlah operasi perkalian konvolusi manual dengan kernel $5	imes5$ pada foto $4000	imes3000$ dan pada citra $640	imes480$. Kaitkan dengan waktu komputasi pada Kode 4.1 dan kebutuhan pengguna nomor 4. 

### Answer
* **Estimasi operasi perkalian ($5 	imes 5 = 25$ perkalian per piksel):**
  - Pada foto asli $4000 	imes 3000 = 12.000.000$ piksel $	imes 25 = 300.000.000$ (300 juta) operasi perkalian.
  - Pada citra kerja $640 	imes 480 = 307.200$ piksel $	imes 25 = 7.680.000$ (~7,68 juta) operasi perkalian.
* **Kaitan:** Perhitungan manual dengan perulangan Python pada citra besar memakan waktu sangat lambat (bisa beberapa detik hingga menit). Ini melanggar **kebutuhan pengguna nomor 4** (proses harus cukup cepat untuk telepon genggam kelas menengah). Oleh karena itu, pengecilan resolusi citra ke $640 	imes 480$ dan penggunaan fungsi teroptimasi berbasis C/C++ di OpenCV (`cv2.filter2D` / `cv2.medianBlur`) sangat esensial agar pemrosesan berjalan dalam hitungan milidetik.

## P4.7
### Question
Bila suatu saat foto SIMUTEH tidak sengaja memuat wajah petani, mengapa blur ringan tidak cukup untuk anonimisasi? Usulkan prosedur yang lebih aman. 

### Answer
* **Alasan blur ringan tidak cukup:** *Blur* ringan (seperti Gaussian blur kecil) masih memungkinkan algoritma rekonstruksi wajah modern (deep learning de-blurring / face hallucination) atau pengenalan wajah berbasis fitur struktural untuk mengidentifikasi identitas petani.
* **Prosedur yang lebih aman:** 
  1. Deteksi wajah otomatis menggunakan detektor objek (misalnya Haar Cascade atau MediaPipe Face Detection) pada tahap akuisisi awal.
  2. Melakukan *black-out* total (penutupan area piksel wajah dengan warna hitam solid) atau pemotongan area (*crop*) otomatis yang hanya menyertakan nampan dan daun teh, sehingga data wajah tidak pernah tersimpan di sistem.


# P5
## P5.1
### Question
Apakah rangkaian praproses Anda menaikkan KB di semua kondisi? Kondisi mana yang paling sulit, dan mengapa? 

### Answer
Rangkaian praproses berhasil menaikkan Kontras Bercak (KB) secara signifikan pada sebagian besar kondisi, namun tidak selalu seragam di semua kondisi. Kondisi yang **paling sulit** adalah **kondisi bayangan (shadow)** dan **kontras rendah**. Alasannya, pada kondisi bayangan terdapat gradasi pencahayaan yang tidak merata (sebagian daun terang dan sebagian gelap gulita), sehingga operasi pencerahan atau penyesuaian global sering kali gagal memisahkan bercak kecil yang tertutup bayangan tanpa memperkuat derau latar.

## P5.2
### Question
Bila ada kondisi yang KB-nya justru turun setelah praproses, jelaskan penyebabnya dan usulkan perbaikan, misalnya parameter yang dipilih otomatis berdasarkan statistik histogram. 

### Answer
Jika KB suatu kondisi turun setelah praproses, penyebabnya adalah parameter praproses (seperti kekuatan CLAHE atau kernel redam derau) terlalu agresif, sehingga mengaburkan batas tepi bercak atau meratakan perbedaan intensitas antara bercak dan daun sehat. **Usulan perbaikan:** Menerapkan sistem parameter adaptif berbasis statistik histogram (misalnya, `clipLimit` CLAHE dan ukuran kernel disesuaikan secara dinamis berdasarkan nilai simpangan baku dan rentang persentil histogram citra masukan).

## P5.3
### Question
Apakah praproses Anda menimbulkan bercak palsu atau menaikkan keragaman intensitas daun sehat secara berlebihan? Kondisi mana yang paling berisiko? Kaitkan dengan risiko salah klasifikasi daun sehat pada P11. 

### Answer
Bila parameter ketajaman (*unsharp masking*) atau *clip limit* CLAHE diset terlalu tinggi, praproses dapat menimbulkan artifak atau memperkuat tekstur alami daun sehat sehingga memunculkan bintik-bintik yang menyerupai bercak (*bercak palsu* / *false positive*). Kondisi yang paling berisiko adalah **kondisi terang terik** dan **kontras rendah**. Pada tahap klasifikasi (P11), daun sehat yang memiliki bercak palsu akibat praproses berisiko tinggi salah diklasifikasikan sebagai daun berpenyakit (bercak ringan), yang merugikan petani.

## P5.4
### Question
Mengapa praproses yang sama persis, dengan parameter yang sama, harus diterapkan pada data latih dan data uji pada P11? Apa akibatnya bila tidak? 

### Answer
Praproses yang sama persis dengan parameter yang sama harus diterapkan pada data latih (*training data*) dan data uji (*testing data*) untuk menjaga konsistensi ruang fitur (*feature space consistency*). Bila tidak, model klasifikasi (KNN/SVM) akan menerima distribusi fitur masukan yang berbeda antara saat dilatih dan saat diuji (*covariate shift*), yang mengakibatkan penurunan akurasi drastis, model salah mengenali pola, dan sistem gagal berfungsi dengan handal di lapangan.

## P5.5
### Question
Pilih dua nilai AIK (amanah, jujur, adil, peduli, profesional, tabligh) dan jelaskan secara konkret bagaimana Anda menerapkannya dalam pekerjaan ini, misalnya dalam pengambilan data, pelaporan angka, atau dokumentasi. 

### Answer
1. **Amanah:** Diterapkan dalam menjaga kerahasiaan data pengguna (petani) dengan memastikan seluruh metadata EXIF dihapus, tidak menyebarkan foto tanpa izin, dan membangun sistem yang benar-benar handal sesuai fungsi yang diamanatkan kelompok tani.
2. **Jujur:** Diterapkan dalam pelaporan angka evaluasi (seperti tabel KB, PSNR, dan metrik akurasi) apa adanya tanpa melakukan manipulasi data atau menyembunyikan keterbatasan hasil eksperimen pada laporan praktikum.
