# Offline Brief

## Local Facts

- Nama kamus: Bahasa Kerinci dialek Siulak. Judul bab rumah: umah, diglosakan rumah. Judul warna: warno, diglosakan warna. Judul kalender: bulan ngan ahi, diglosakan bulan dan hari.
- Penerbit: Kantor Bahasa Provinsi Jambi, 2023. ISBN 978-623-118-908-6. 355 kata, 21 tema, dengan aksara Incung.
- ISO 639-3: `kvr`. Glottocode: `keri1250`.
- ISO menaruh Kerinci di dalam macrolanguage Melayu (`msa`). Itu bukan alasan untuk mengganti lema Siulak dengan bahasa Indonesia atau Minangkabau.
- Peta Bahasa: dituturkan di sejumlah desa Kabupaten Kerinci. Batas yang diakui penduduk pada entri itu: timur Melayu dialek Jambi, barat Minangkabau, utara Melayu dialek Bungo, selatan bahasa Bengkulu.
- Kepercayaan sumber: Level 2.
- Kamus gambar tidak memuat kalimat. Tidak ada sapaan "apa kabar" yang terbaca.
- Hari pada tabel kamus: sinanyan Senin, selasa Selasa, rebu Rabu, kmih Kamis, maat Jumat, stu Sabtu, ahad Minggu.
- abang pada halaman warna berarti merah. klabu berarti biru. klabu asap berarti abu-abu.
- lawang berarti pintu. tanggo berarti tangga. singem berarti jendela. lindin berarti dinding.
- anak skula diglosakan pelajar. siraga diglosakan pedagang. tani diglosakan petani.

## Guardrails

- Jangan mengarang kalimat utuh dalam bahasa Kerinci.
- Jangan mengarang sapaan kerabat. Kamus gambar tidak memuatnya.
- Jangan memindahkan lema Siulak ke Sungai Penuh, Gunung Raya, atau ke bahasa Minangkabau.
- Jangan memakai abang sebagai panggilan kakak.
- Jangan memakai klabu untuk abu-abu. Abu-abu pada kamus ini klabu asap.
- Jangan menghasilkan aksara Incung.
- Jam, uang, nama sekolah, dan alamat tetap Indonesia.
- Tandai mixed pada setiap pesan yang mencampur bahasa Indonesia.

## Sample Prompts

- "Use $tutur-kerinci to adapt this text with a source-aware Bahasa Kerinci register."
- "Ingatkan tetangga, dialek Siulak: hari Senin kumpul di rumah. Jangan mengarang sapaan."
- "Cek catatan ini. Saya panggil orangnya abang, dan saya tulis klabu untuk cat abu-abu."
- "Ini untuk Sungai Penuh, bukan Siulak. Jangan pakai kamus gambar itu sebagai kalimat."

## Safe Output Patterns

- Satu atau dua kata Siulak yang ada di tabel.
- Sisa pesan bahasa Indonesia.
- Baris catatan: dialek Siulak, kamus gambar 2023, plus glosa kata yang dipakai.
- Untuk kampung lain, tolak penggantian kata dan minta sampel dari kampung itu.
- Untuk Incung, sebut bahwa kamus memasangkannya, lalu tulis Latin yang sudah diglosakan.

## Why This Is Not Minangkabau

Glottolog menaruh Kerinci di kelompok Kerinci-Minangkabau, dan Peta Bahasa menyebut batas barat dengan bahasa Minangkabau. Kedekatan itu bukan izin untuk mengisi kata Siulak yang kosong dengan kata Minangkabau. Kosong tetap bahasa Indonesia.
