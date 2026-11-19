# Jawaban Analisis UTS

Jawaban ini merujuk pada keluaran yang tersimpan di notebook P5 (tepi/Canny) dan P6 (morfologi), serta berkas evaluasi hasil. Nilai yang disebut adalah nilai dari eksekusi tersebut; kesimpulan yang tidak dapat dipastikan dari tabel saja saya tandai sebagai dugaan yang perlu diuji.

## Pertemuan 5 — Gradien, operator tepi, dan Canny

### P1.1

Pada contoh lembar hitung, Sobel menghasilkan `Gx=534` dan `Gy=22` (Prewitt: `Gx=399`, `Gy=17`). Perubahan intensitas dominan terjadi pada arah x, sehingga magnitudo gradien arah x jauh lebih besar. Gradien menunjuk tegak lurus terhadap tepi, bukan sepanjang tepi. Sudut gradien Sobel sekitar 2,36° dan arah tepinya sekitar 92,36°; jadi tepinya hampir vertikal. Panel arah menunjukkan hubungan tegak lurus tersebut.

### P1.2

Kernel Sobel memberi bobot lebih besar pada tetangga dekat pusat daripada Prewitt, sehingga respons gradiennya pada tepi contoh lebih besar (534 dibanding 399 untuk `Gx`). Dengan ambang yang sama, Sobel lebih mudah melewati ambang dan dapat menghasilkan lebih banyak piksel tepi; Prewitt mungkin melewatkan tepi lemah. Perbandingan yang adil perlu menyesuaikan ambang terhadap skala respons tiap operator.

### P1.3

Pada data mentah, kanal Gray memberi F1 lebih tinggi untuk Sobel (0,847 vs 0,626) dan Prewitt (0,866 vs 0,686); kanal R lebih tinggi untuk LoG (0,944 vs 0,787) dan Canny (0,979 vs 0,747). Setelah praproses, pola itu tetap: Gray unggul untuk Sobel/Prewitt, sedangkan R unggul untuk LoG/Canny. Tabel KB yang tersimpan menunjukkan pada kondisi bayangan KB kanal R=4,01 dan Gray=1,20. Kontras R yang lebih tinggi dapat membantu LoG/Canny memisahkan bercak dari daun, tetapi tidak menjamin semua operator membaik—hasilnya juga bergantung pada respons kernel dan ambang.

### P1.4

Tidak. Secara agregat, praproses menurunkan F1 Sobel dan Prewitt pada kedua kanal, serta LoG pada kedua kanal. Canny Gray naik dari 0,747 menjadi 0,788, sedangkan Canny R sedikit turun dari 0,979 menjadi 0,976. Presisi juga turun pada seluruh kombinasi agregat yang ditampilkan; misalnya Canny Gray 0,750 menjadi 0,684 dan Canny R 0,983 menjadi 0,964. Penghalusan/peningkatan kontras dapat menghilangkan gangguan, tetapi median filter dan perubahan intensitas juga dapat mengaburkan batas atau mengubah respons tepi. Jadi manfaatnya bergantung pada kanal, operator, serta parameter.

### P1.5

LoG menghaluskan citra dengan Gaussian, lalu mencari perubahan tanda (perlintasan nol) pada respons Laplacian sebagai lokasi tepi. Perubahan kecil akibat tekstur atau derau juga dapat menghasilkan perlintasan nol. Tanpa penyaringan/ambang yang memadai, banyak respons lemah dianggap tepi: hasil eksekusi LoG memang menunjukkan recall 0,997, tetapi presisinya lebih rendah (Gray 0,656; R 0,907). Karena itu sigma dan ambang perlu dipilih untuk menekan tepi palsu tanpa menghapus bercak.

### P2.1

NMS membandingkan piksel sepanjang arah gradien karena arah tersebut melintasi tepi dan menunjukkan arah perubahan intensitas terbesar. Perbandingan ini menipiskan tepi menjadi puncak lokal; membandingkan sepanjang arah tepi tidak akan menguji puncak melintasi batas. Hysteresis memakai ambang tinggi untuk memilih tepi kuat dan ambang rendah untuk calon tepi lemah yang hanya dipertahankan bila terhubung ke tepi kuat. Pada contoh, piksel bernilai 90 yang hanya melewati ambang bawah dibuang karena tidak terhubung ke piksel kuat.

### P2.2

F1 tertinggi pada uji sigma/ambang adalah 0,981, dicapai oleh sigma=1 dengan ambang 100/200 dan sigma=2 dengan 50/150. Untuk menjaga bercak ringan, sigma=1 dan 100/200 lebih seimbang: recall bercak 0,971 dan F1 kelas ringan 0,968. Sigma=2 dan 50/150 memiliki recall bercak 0,888 dan F1 ringan 0,839, sehingga lebih berisiko menghilangkan bercak kecil. Ambang 30/90 pada sigma=0 memberi F1 kelas ringan tinggi (0,992), tetapi presisi keseluruhan hanya 0,021 karena sangat banyak tepi palsu. Pilihan parameter harus menimbang derau terhadap bercak kecil, bukan F1 kelas saja.

### P2.3

Dengan rumus ambang otomatis berbasis median dan faktor 0,33, median keluaran untuk kondisi kontras rendah memberi:

- Gray, median 149,2: ambang sekitar 100 dan 198.
- R, median 150,8: ambang sekitar 100 dan 201.

Angka tersebut berasal dari intensitas median, sedangkan Canny membandingkan magnitudo gradien. Median intensitas tidak memberi tahu kuat-lemahnya perubahan di batas daun/bercak; karena itu ambang hasilnya dapat terlalu tinggi atau rendah terhadap gradien aktual. Pada tabel eksekusi, F1 kontras rendah untuk ambang otomatis adalah 0,792 (Gray) dan 0,744 (R), sedangkan ambang tetap 30/90 menghasilkan 0,936 dan 0,982. Jadi keluaran tersimpan tidak mendukung klaim bahwa ambang otomatis lebih baik pada R; pada hasil ini ambang tetap justru lebih baik.

### P2.4

Ambang berbasis persentil magnitudo menyesuaikan diri dengan distribusi kekuatan gradien citra, sehingga lebih tahan terhadap perubahan skala kontras daripada satu nilai tetap atau ambang yang dihitung dari intensitas. Persentil q menentukan titik potong distribusi (berapa banyak piksel berada di atas ambang); q terlalu rendah memasukkan terlalu banyak gradien lemah sebagai tepi, sedangkan q terlalu tinggi dapat menekan tepi halus. Pada hasil yang diuji, persentil 98 memberi F1 paling tinggi dan paling konsisten: 0,746–0,816 untuk Gray dan 0,948–0,987 untuk R. Persentil 90 hanya memberi sekitar 0,069–0,083.

### P2.5

Tulang daun memiliki perubahan intensitas yang tampak pada Gray, sehingga ikut terdeteksi sebagai tepi. Pada kanal R, tulang daun yang sehat lebih seragam terhadap latar daun dan responsnya jauh lebih kecil. Hitungan piksel tepi tulang daun yang tercatat untuk Gray jauh lebih besar, misalnya 942 pada kondisi normal dan 53,5 pada kontras rendah, sedangkan R tercatat 0 pada kondisi tersebut (R=209 pada kondisi terang). Ini mendukung pemilihan kanal R untuk mengurangi tepi tulang daun pada kondisi yang diuji, tetapi kanal tetap perlu divalidasi pada seluruh kondisi cahaya.

### P2.6

Tepi dapat dipakai untuk membantu mencari batas daun atau memberi petunjuk bentuk, tetapi tidak cukup untuk mengukur luas bercak: tepi hanya berupa garis dan dapat terputus, berderau, atau bercampur dengan tulang daun. Persentase luas memerlukan mask wilayah bercak dan mask daun yang terisi, lalu rasio luas piksel bercak terhadap luas daun. Maka untuk kebutuhan pengguna berupa persen bercak dan proses cepat, tepi sebaiknya menjadi fitur bantu/opsional, bukan satu-satunya tahap segmentasi. Tabel keputusan pada notebook masih kosong; keputusan ini merupakan rekomendasi berdasarkan evaluasi.

## Pertemuan 6 — Morfologi, komponen, dan integrasi

### P3.1

Erosi menghapus foreground yang tidak cukup tebal untuk menampung elemen struktur (SE). Opening melakukan erosi lalu dilasi, sehingga lubang/bercak kecil yang sudah hilang saat erosi tidak dapat dipulihkan. Closing melakukan dilasi lalu erosi; celah sempit, termasuk celah diagonal, dapat tertutup dan bagian yang berdekatan dapat menyatu. Akibatnya luas satu komponen dapat membesar dan dua bercak berbeda dapat dihitung sebagai satu, sehingga persen maupun jumlah bercak SIMUTEH bias.

### P3.2

Pada contoh lembar hitung, konektivitas 4 menghasilkan 4 komponen sedangkan konektivitas 8 menghasilkan 3. Konektivitas 8 lebih sesuai bila piksel yang hanya bersentuhan diagonal secara visual merupakan satu bercak. Namun, bercak yang sangat berdekatan juga dapat tergabung; hasil perlu diperiksa pada mask nyata. Pada citra teh_041, jumlah komponen yang dilaporkan sama-sama 11 untuk konektivitas 4 dan 8.

### P3.3

Pada teh_021, mask awal memiliki 220 komponen, opening menurunkannya menjadi 8 (439 piksel; IoU 0,551), sedangkan closing masih menyisakan 202 komponen (1.838 piksel; IoU 0,175). Pada daun sehat teh_011, opening menurunkan komponen dari 177 menjadi 15. Opening membuang objek tipis/titik yang tidak mampu memuat SE; closing justru mengisi celah dan mempertahankan banyak objek. Potongan tulang daun yang cukup tebal masih bertahan karena memenuhi ukuran SE, sehingga opening bukan pemisah semantik antara bercak dan tulang daun.

### P3.4

Konfigurasi yang tersimpan untuk evaluasi adalah `k=4`, bentuk SE elips, ukuran opening dan closing 5. Ini merupakan kompromi, bukan hasil terbaik pada setiap ukuran: pada tabel eksperimen, SE elips 4×5 memberi IoU 0,69 (berat) dan 0,40 (ringan), dengan galat jumlah rata-rata 2,45, 3,25, dan 2,45 untuk berat, ringan, dan sehat. SE ukuran 7 memperbaiki IoU bercak ringan, tetapi operasi lebih besar berisiko menghapus bercak kecil atau menyatukan objek. Bila fokusnya mengurangi bercak palsu pada daun sehat, kandidat lain seperti SE persegi 4×7 memberi galat sehat 0 pada tabel, tetapi IoU bercak ringan sedikit lebih rendah (0,46). Elips dan silang 3×3 identik pada piksel karena bentuk raster keduanya hanya mencakup pusat dan empat tetangga; titik sudut elips 3×3 tidak termasuk.

### P3.5

Gradien morfologi dari mask daun memanfaatkan batas mask yang jelas dan tidak bergantung langsung pada kontras warna daun-latar seperti Canny; ini dapat memberi tepi daun yang rapi ketika mask awalnya baik. Namun, pada kondisi kontras rendah hasil yang tersimpan justru menunjukkan F1 gradien morfologi 0,208 dibanding F1 Canny 0,908. Karena itu Canny tetap diperlukan saat batas mask morfologi tidak andal atau ketika tepi tekstur/bercak tertentu perlu dianalisis. Untuk mengukur bercak, keduanya tetap perlu diikuti segmentasi wilayah, bukan hanya garis tepi.

### P4.1

Kebulatan dihitung sebagai \(4\pi A/P^2\). Pada contoh, bercak 3×3 memiliki kebulatan 0,785, sedangkan garis 1×6 bernilai 0,385; bercak lebih kompak daripada garis, tetapi rasterisasi membuat kelilingnya tidak sama dengan keliling lingkaran ideal. Untuk komponen sangat kecil, aproksimasi kontur dan keliling piksel OpenCV dapat membuat penyebut terlalu kecil sehingga kebulatan terhitung sedikit di atas 1 (contoh tabel komponen mencapai 1,12). Nilai di atas 1 adalah efek diskretisasi/perhitungan kontur, bukan bentuk yang secara geometri lebih bulat dari lingkaran.

### P4.2

Skala 0,4375 mm/piksel mengasumsikan jarak kamera, zoom/fokus, resolusi, orientasi, dan bidang daun terhadap kamera sama dengan saat kalibrasi. Jika daun difoto dari 30 cm, skala perlu dihitung ulang; tanpa jarak kalibrasi awal, perubahan luas numerik tidak dapat ditentukan. Secara pendekatan, skala panjang berubah sebanding dengan jarak, sehingga luas mm² berubah sebanding dengan kuadrat rasio jarak. SIMUTEH sebaiknya memakai jarak/penyangga kamera yang tetap atau objek kalibrasi berukuran diketahui di bidang daun, dan memperingatkan bila kondisi kalibrasi tidak terpenuhi.

### P4.3

Aturan luas + kebulatan + rasio aspek paling efektif mengurangi bercak palsu pada daun sehat dalam hasil ini: rata-rata galat jumlah sehat turun dari 2,45 tanpa saring menjadi 0,45, dan jumlah daun sehat yang masih memiliki bercak palsu turun dari 11 menjadi 6. Aturan rasio aspek dapat menolak bercak asli yang memanjang, dan dapat gagal memisahkan dua bercak yang menyatu menjadi satu objek memanjang. Karena itu rasio aspek sebaiknya menjadi salah satu bukti, bukan aturan mutlak.

### P4.4

Untuk teh_041, acuan bercak adalah 2,65% luas daun dan prediksi 1,796%. Prediksi lebih rendah sebesar 0,854 poin persentase, atau sekitar 32,2% lebih rendah relatif terhadap acuan. Jumlah komponen sama-sama 8, jadi selisih utamanya berada pada luas mask yang terhitung, bukan jumlah bercak. Cincin kecokelatan di tepi bercak dapat memiliki nilai kanal R yang tidak lolos pemisahan warna; median filter dapat menghaluskan batas cincin tersebut, sedangkan closing dapat mengubah/menyatukan batas kecil. Hasil yang tersedia konsisten dengan luas yang terlewat, tetapi kontribusi tiap tahap perlu dipastikan dengan membandingkan mask sebelum dan sesudah tiap operasi.

### P5.1

Pada evaluasi 60 citra, galat absolut rerata persen bercak adalah 0,553 poin persentase, korelasi prediksi dengan acuan 0,947, dan akurasi kelas 0,883 (53 dari 60 citra). Matriks kebingungan menunjukkan 3 daun ringan dinilai sehat, 3 daun berat dinilai ringan, 1 daun sehat dinilai ringan, dan 17 dari 20 citra pada masing-masing kelas berat/ringan diklasifikasikan benar; 19 dari 20 daun sehat benar. Dengan demikian, kelas sering tepat tetapi persen luas masih dapat meleset. Contohnya teh_041 memiliki 8 komponen seperti acuan, tetapi persentasenya 1,796% vs 2,65%, sehingga turun ke kelas ringan. Hasil CSV juga menunjukkan teh_024 dan teh_039 diprediksi 0% meski acuan masing-masing 0,49% dan 0,63%.

### P5.2

Menentukan batas kelas setelah melihat label seluruh dataset membocorkan informasi data evaluasi ke pemilihan parameter, sehingga akurasi tampak lebih baik daripada kemampuan pada data baru. Batas 0,1% dan 2,0% seharusnya dipilih hanya menggunakan data latih/validasi (atau validasi silang), lalu dikunci sebelum mengukur data uji yang tidak pernah dipakai memilih parameter. Data uji idealnya mencakup kondisi cahaya dan daun yang berbeda dari latih.

### P5.3

Kesalahan muncul pada kontras rendah (akurasi kelas 0,75), kondisi normal (0,75), dan terang (0,92); kondisi bayangan dan gelap mencapai 1,00 pada ringkasan tersimpan. Semua tiga citra ringan kontras rendah yang salah kelas—teh_024, teh_034, dan teh_039—diprediksi sehat; pada dua citra prediksi mask/luas nol. Ini mengarah pada kemungkinan bercak tidak terbentuk di mask awal atau terhapus sebelum pengukuran, bukan sekadar salah batas kelas. Sebaliknya, teh_041, teh_056, dan teh_058 tetap memiliki bercak tetapi persen prediksinya rendah sehingga kelas berat turun menjadi ringan. Output ringkasan belum mengisolasi kesalahan per tahap, jadi penyebab praproses vs mask awal vs penyaringan belum dapat dipastikan. Pada P7, simpan dan evaluasi mask tiap tahap terhadap acuan untuk melokalisasi sumbernya.

### P5.4

Untuk kelompok tani, daun berbercak yang dinilai sehat berisiko menunda pemeriksaan atau penanganan. Pada hasil ini ada 3 kasus tersebut, dibanding 1 daun sehat yang dinilai berbercak. Untuk menekan kesalahan negatif, ambang minimum luas/bercak atau syarat bentuk dapat dilonggarkan (misalnya menurunkan `luas_min` atau `bulat_min`) dan ambang kelas ringan dapat diturunkan. Konsekuensinya, bercak palsu pada daun sehat dapat bertambah. Sistem sebaiknya menampilkan persen dan kelas, mask overlay, jumlah/luas komponen, serta status “perlu pemeriksaan” untuk hasil dekat ambang agar petugas dapat memverifikasi keputusan.

### P5.5

Data bercak sintetis yang berbentuk lingkaran sempurna dapat membuat aturan kebulatan minimum dan rasio aspek maksimum terlalu cocok pada bentuk ideal. Bercak nyata bisa bergerigi, memanjang, tidak bulat, atau berdekatan/menyatu; aturan tersebut berpotensi menolaknya. Pengujian perlu memakai foto nyata berlabel manual yang dipisahkan dari data pengembangan, beragam tingkat keparahan dan cahaya. Ukur precision/recall deteksi, IoU mask, galat jumlah, galat persen luas, dan akurasi kelas per kondisi, lalu periksa khusus bercak memanjang dan bercak yang saling berdekatan.

## Ringkasan umum B.3

1. **Operator dan kanal:** pada hasil agregat, kanal R terbaik untuk LoG dan Canny; Gray lebih baik untuk Sobel dan Prewitt. Tidak ada operator/kanal yang unggul untuk semua kondisi. Praproses tidak otomatis membantu dan perlu dipilih berdasarkan evaluasi.
2. **Parameter Canny:** sigma dan dua ambang perlu menyeimbangkan derau dengan bercak kecil. Uji menunjukkan sigma=1 dan 100/200 sebagai pilihan seimbang; ambang otomatis berbasis median intensitas tidak konsisten dengan magnitudo gradien. Validasi per kondisi dan per kelas tetap diperlukan.
3. **Peran tepi:** tepi berguna untuk batas daun/fitur, tetapi bukan mask isi bercak. Pengukuran persen harus memakai wilayah bercak dan daun yang tersegmentasi; Canny bersifat bantu atau opsional sesuai kualitas mask.
4. **Membersihkan mask:** opening efektif mengurangi komponen kecil, tetapi SE besar dapat menghapus bercak ringan. Gunakan SE terkecil yang memenuhi kebutuhan, cek galat per kelas, dan hindari closing agresif yang menyatukan bercak.
5. **Pengukuran dan kelas:** pada 60 citra, sistem memiliki galat absolut rerata persen 0,553 poin, korelasi 0,947, dan akurasi kelas 88,3%. Jumlah komponen dapat benar sementara luasnya masih bias, seperti teh_041. Hasil sebaiknya ditampilkan bersama mask dan indikator verifikasi, bukan kelas saja.

## Sumber hasil

- [Notebook P5 — tepi dan Canny](../../notebook/P5_tepi.ipynb)
- [Notebook P6 — morfologi](../../notebook/P6_morfologi.ipynb)
- [Evaluasi bercak P6](../../hasil/p6_evaluasi_bercak.csv)
- [Parameter bercak](../../hasil/param_bercak.json)
