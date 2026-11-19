Berikut pertanyaan analisis (kode P1.1 sampai P5.5) dari petunjuk. Ada 25 pertanyaan, dan semuanya wajib dijawab di laporan dengan mencantumkan kodenya.

## Pertemuan 5

**Bagian 1: Gradien dan operator tepi**

- **P1.1** Dari lembar hitung, mengapa |Gx| jauh lebih besar daripada |Gy|? Jelaskan hubungan arah gradien dengan arah tepi, lalu tunjukkan hubungan ini pada panel arah Kode 1.2.
- **P1.2** Mengapa magnitudo Sobel lebih besar daripada Prewitt untuk tepi yang sama? Apa akibatnya bila ambang T yang sama dipakai untuk keduanya?
- **P1.3** Berdasarkan Tabel 6, kanal mana yang memberi F1 lebih tinggi untuk tiap operator? Kaitkan jawaban Anda dengan Kontras Bercak (KB) per kanal pada Evaluasi P1-P4.
- **P1.4** Apakah praproses menaikkan F1 untuk semua operator dan kanal? Untuk kombinasi mana praproses justru menurunkan presisi atau recall? Jelaskan penyebabnya.
- **P1.5** LoG menghasilkan recall sangat tinggi tetapi presisinya bergantung pada sigma dan ambang. Jelaskan cara kerja perlintasan nol (zero crossing) dan mengapa LoG tanpa ambang yang memadai menghasilkan banyak tepi palsu.

**Bagian 2: Algoritma Canny dan keputusan pemakaian tepi**

- **P2.1** Dari lembar hitung, mengapa NMS membandingkan piksel dengan tetangga searah gradien, bukan searah tepi? Mengapa hysteresis memakai dua ambang, dan mengapa piksel bernilai 90 pada soal (b) dibuang walaupun lebih besar dari ambang bawah?
- **P2.2** Berdasarkan Tabel 7, kombinasi mana yang memberi F1 tertinggi? Apakah kombinasi itu juga terbaik untuk bercak kelas ringan? Jelaskan trade-off antara meredam derau dan mempertahankan bercak kecil.
- **P2.3** Pada citra kontras rendah kanal Gray, ambang otomatis berbasis median dan ambang tetap 30/90 sama-sama gagal, sedangkan pada kanal R tidak. Hitung ambang otomatis dari median keluaran Kode 2.2, lalu bandingkan dengan besarnya gradien di tepi daun pada citra kontras rendah untuk kanal Gray dan R. Mengapa ambang yang dihitung dari intensitas tidak cocok untuk Canny yang bekerja pada magnitudo gradien?
- **P2.4** Mengapa ambang dari persentil magnitudo (Langkah 2.4) lebih tahan terhadap perubahan kontras? Mengapa nilai q yang tepat berkaitan dengan proporsi piksel tepi dalam citra?
- **P2.5** Mengapa tulang daun pada daun sehat dapat terdeteksi sebagai tepi pada kanal Gray tetapi tidak pada kanal R? Apa artinya bagi pemilihan kanal di SIMUTEH?
- **P2.6** Jelaskan keputusan Anda pada Tabel keputusan. Mengapa tepi saja belum cukup untuk menghitung persentase luas bercak? Kaitkan dengan kebutuhan pengguna nomor 2 dan 4 (keluaran persen bercak dan proses yang cepat).

## Pertemuan 6

**Bagian 3: Operasi morfologi**

- **P3.1** Dari lembar hitung, mengapa erosi saja dan opening saja menghapus bercak berlubang? Apa yang terjadi pada celah antara piksel diagonal dan garis saat closing, dan mengapa hal ini berisiko bagi penghitungan bercak di SIMUTEH?
- **P3.2** Konektivitas mana (4 atau 8) yang lebih tepat untuk menghitung bercak? Berikan contoh dari lembar hitung dan alasan dari sisi bentuk bercak nyata.
- **P3.3** Pada Kode 3.2, mengapa opening berhasil membuang titik derau dan tepi daun, sedangkan closing saja hampir tidak mengurangi jumlah komponen? Mengapa potongan tulang daun pada daun sehat masih tersisa setelah opening?
- **P3.4** Berdasarkan Tabel 9, kombinasi k, bentuk, dan ukuran SE mana yang Anda pilih? Jelaskan trade-off antara bercak kelas ringan dan bercak palsu pada daun sehat. Mengapa hasil SE elips 3 x 3 identik dengan SE silang 3 x 3?
- **P3.5** Mengapa gradien morfologi dari mask daun memberi tepi daun yang lebih baik daripada Canny, terutama pada kondisi kontras rendah? Kapan Canny tetap diperlukan?

**Bagian 4: Komponen terhubung dan pengukuran bercak**

- **P4.1** Dari lembar hitung, bandingkan kebulatan bercak dan garis. Mengapa kebulatan bercak 3 x 3 tidak sama dengan 1 walaupun bentuknya "hampir bulat", dan mengapa pada komponen yang sangat kecil kebulatan hasil OpenCV bisa lebih dari 1?
- **P4.2** Konversi 1 piksel = 0,4375 mm berasal dari lembar hitung P2. Sebutkan asumsi yang mendasarinya. Apa yang terjadi pada luas bercak dalam mm² bila petugas memotret dari jarak 30 cm, dan bagaimana SIMUTEH mengatasinya pada foto nyata?
- **P4.3** Berdasarkan Tabel 11 dan diagram sebar, aturan mana yang paling efektif membuang bercak palsu? Apa risiko aturan rasio aspek pada bercak yang memanjang atau dua bercak yang menyatu?
- **P4.4** Bandingkan luas total bercak hasil Anda pada teh_041 dengan luas pada mask acuan. Apakah hasil Anda lebih besar atau lebih kecil, dan berapa persen selisihnya? Jelaskan penyebabnya. Petunjuk: perhatikan nilai kanal R pada cincin kecokelatan di tepi bercak, pengaruh penapis median pada praproses, dan pengaruh closing.

**Bagian 5: Integrasi modul bercak.py**

- **P5.1** Seberapa tepat SIMUTEH v0.3 mengukur persen bercak dan menebak kelas? Jelaskan setiap kesalahan yang terjadi beserta penyebabnya, merujuk Langkah 5.3.
- **P5.2** Batas kelas 0,1% dan 2,0% pada parameter bawaan ditentukan dengan melihat label.csv seluruh dataset. Mengapa cara ini membuat akurasi terlalu optimistis? Bagaimana seharusnya batas ditentukan (kaitkan dengan pembagian data latih, validasi, dan uji pada P11)?
- **P5.3** Kondisi cahaya mana yang menghasilkan kesalahan? Apakah kesalahan itu berasal dari praproses, dari citra biner awal, atau dari penyaringan? Usulkan perbaikan yang dapat diuji pada P7.
- **P5.4** Bagi kelompok tani, mana yang lebih merugikan: daun sehat dinilai berbercak atau daun berbercak dinilai sehat? Parameter mana yang Anda ubah bila ingin mengurangi jenis kesalahan tersebut, dan apa konsekuensinya? Bagaimana SIMUTEH sebaiknya menampilkan hasil agar petugas tetap dapat memeriksa keputusan sistem (nilai amanah dan transparansi)?
- **P5.5** Bercak pada dataset sintetis berbentuk lingkaran sempurna. Aturan mana di modul Anda yang mungkin terlalu cocok dengan data sintetis dan akan gagal pada foto bercak nyata yang bentuknya tidak beraturan? Bagaimana Anda akan mengujinya?

Selain 25 pertanyaan itu, Bagian B.3 memuat 5 pertanyaan umum yang dijawab oleh keseluruhan praktikum. Jawabannya bisa dirangkum di Pendahuluan dan Kesimpulan laporan:

1. Operator tepi dan kanal mana yang paling tepat, dan apakah praproses membantu?
2. Bagaimana memilih parameter Canny agar bercak kecil tidak hilang dan derau tidak ikut terdeteksi?
3. Apakah deteksi tepi perlu dipakai di SIMUTEH, untuk apa, dan di tahap mana?
4. Bagaimana membersihkan citra biner bercak tanpa menghapus bercak kecil?
5. Berapa jumlah, luas, dan persentase bercak setiap daun, dan seberapa tepat kelas mutunya?

Jika Anda ingin saya membuatnya menjadi berkas, misalnya templat laporan (docx) dengan kode pertanyaan sebagai kerangka jawaban, beri tahu saya.