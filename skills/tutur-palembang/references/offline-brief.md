# Offline Brief

## Local Facts

- Nama di kamus Balai Bahasa: Bahasa Melayu dialek Palembang (BMP). Nama harian: Baso Pelembang Sari-ari. Lapis halus: Bebaso, label Bbs.
- Wilayah kota: Palembang. Peta Bahasa memasukkan Kelurahan 16 Ulu ke bahasa Melayu Sumatera Selatan, bersama titik lain di provinsi itu.
- ISO 639-3 yang hidup: `mui` (Musi). Kode lama Palembang `plm` digabung ke `mui` efektif 2008-01-14, bersama Lematang, Penesak, dan Rawas.
- Glottocode simpul Palembang: `pale1264`. Glottocode bahasa Musi: `musi1241`.
- Di dalam Musi, bahan penggabungan ISO memisahkan kelompok Palembang (Palembang dan Melayu dataran rendah) dari kelompok Musi hulu (Musi, Pegagan, Rawas).
- Kamus: Kamus Palembang-Indonesia Edisi IV (2021), Balai Bahasa Provinsi Sumatera Selatan. Edisi II sudah berisi 8793 lema dan sublema. Edisi IV tidak menambah lema.
- Kepercayaan sumber: Level 2.
- Bebaso, menurut prakata kamus, dipakai pada lingkup terbatas, yaitu lingkungan keluarga keraton (bangsawan). Catatan ejaan di kamus yang sama: yang masih menguasai Bebaso terutama penutur lanjut usia.
- Kata ganti yang lemanya terbaca: aku (saya), awak (kamu sebaya atau status di bawah; sinonim yang kamus tulis kamu, kamok, kau), dio (dia).
- Penyangkalan: idak, varian dak. Definisi kamus: partikel pengingkaran, penyangkalan, penolakan.
- Sapaan yang lemanya terbaca: aba ayah, ebok ibu (sinonim emek, ibok), ayuk kakak perempuan.

## Guardrails

- Jangan mengarang kosakata, pantun, atau rumus adat.
- Jangan memakai Bebaso tanpa contoh penutur. Jangan menandai chat biasa dengan Bbs.
- Jangan menyamakan baso kota dengan bahasa hulu Musi.
- Jangan mengubah semua vokal a menjadi o.
- awak tidak untuk atasan, guru, atau orang tua. Untuk mereka, pakai panggilan yang lemanya ada, atau tetap Indonesia.
- Uang, jam, dan alamat tidak diterjemahkan.
- Contoh kamus yang kolom cetaknya bertumpuk tidak dijadikan kalimat baru.

## Sample Prompts

- "Use $tutur-palembang to adapt this text with a source-aware Bahasa Palembang register."
- "Chat ke ayuk: tanya sudah makan, terus minta anter adik. Campur Indonesia boleh."
- "Jangan pakai Bebaso. Ini cuma pesan antar saudara soal jemput."
- "Cek kalimat ini. Semua kata saya ubah jadi berakhir o."

## Safe Output Patterns

- Buka dengan pertanyaan atau suruhan yang ada glosanya.
- Satu urusan satu kalimat.
- Tandai mixed bila lanjutan pesan berbahasa Indonesia.
- Sebut lapisnya: sari-ari.
- Untuk Bebaso, minta contoh. Jangan mengisi sendiri.

## City Versus Upriver

Kode `mui` menampung lebih dari baso kota. Permintaan "bahasa Musi" atau "bahasa Sekayu" tidak dilayani dengan lema Palembang. Minta nama kampungnya, lalu batasi diri pada Indonesia bila kamus kota tidak mencakup tempat itu.
