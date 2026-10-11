# Examples

All Mandar lines are printed examples or headword glosses from Kamus Mandar–Indonesia, edisi revisi, 2025. Indonesian follows that dictionary. Messages that continue past the example are labeled mixed.

## Target-Language Examples

- Indonesian: "Saya mau makan."
  Bahasa Mandar: "Meloaq ummande."
  Note: 2025 dictionary, morphology examples. The person is the `-aq` on `meloaq`. `iyau` is not required in this sentence.
  Usage: A short text when you are about to eat. Do not add a new object.
- Indonesian: "Datanglah kamu besok!"
  Bahasa Mandar: "Poleo medondong!"
  Note: 2025 dictionary. `madondong` is besok. Related: `malai mi dionging` "ia sudah pulang kemarin".
  Usage: Asking someone to come the next day. Clock time stays Indonesian.
- Indonesian: "Duduklah kamu!"
  Bahasa Mandar: "Peqoro moqo!"
  Note: 2025 dictionary. `meqoro` is the dictionary's form for duduk. `q` is the glottal.
  Usage: A direct "sit" to someone you address as `iqo`, not as the respectful `itaq`.
- Indonesian: "Ada kabar baik yang kuterima."
  Bahasa Mandar: "Diang karewa macoa u tarima."
  Note: 2025 dictionary, stress section. `karewa` is glossed kabar beside this sentence. The good news itself is not in the example, so add it in Indonesian.
  Usage: Open a family update, then state the fact in Indonesian.
- Indonesian: "Permisi."
  Bahasa Mandar: "Tabeq."
  Note: Glossed permisi in the `daeng` entry of the same Mandar dictionary. Spelling is `tabeq`, with `q`. This is not the Bugis apostrophe form, and `iye` is not paired with it here.
  Usage: Passing someone or opening a short chat. Do not build a ceremonial welcome around it.
- Indonesian: "Anda yang diperlukan."
  Bahasa Mandar: "Itaq na paralluang."
  Note: 2025 dictionary, respectful second-person free form. Ordinary `kamu` in the same table is `iqo`, as in `iqo nasio` "kamu yang disuruhnya".
  Usage: Only for that respectful "you are needed" meaning.

## Casual Chat

Input:

> Balas sepupu yang tanya jadi datang besok atau tidak.

Output:

> Label: mixed. Poleo medondong! Aku usahakan siang, sekitar pukul 13.00. Kabari kalau rumahnya sepi.

Use:

The command "come tomorrow" is the dictionary line. The hour is Indonesian so the time is not guessed in Mandar.

## Public Reminder

Input:

> Ingatkan tetangga bahwa rapat RT dipindah.

Output:

> Label: mixed. Tabeq. Diang karewa macoa u tarima, tapi isi rapatnya saya tulis di sini: rapat RT pindah ke hari Minggu pukul 16.00 di rumah Pak RT. Bawa catatan iuran.

Use:

`Tabeq` and the "good news I received" line are dictionary examples. The day, hour, and place stay Indonesian. Do not pretend the meeting news is part of the Mandar gloss.

## Professional Or Admin

Input:

> Pesan admin ke peserta yang diminta datang besok untuk lengkapi berkas.

Output:

> Label: mixed. Poleo medondong! Berkas yang kurang dibawa besok sebelum pukul 11.00. Kalau berhalangan, balas pesan ini hari ini.

Use:

One dictionary command, then the office detail in Indonesian. No `iye`.

## Adat Boundary

Input:

> Buat kalindaqdaq pembuka acara adat Mandar.

Safe response:

> Kamus 2025 menyebut `kalindaqdaq` sebagai sindiran berbalas yang mirip pantun. Skill ini tidak menambah bait baru. Minta teks dari pelaku adat di Balanipa, Banggae, Pamboang, atau kampung yang kamu tuju, lalu pemeriksaan hanya menandai kata di luar contoh kamus yang sudah dikutip.

## Review Mode

Input:

> Cek: "Tabe' iye, meloqaq makan di rumah."

Response:

> `Tabe'` dengan apostrof dan `iye` tidak diambil dari kamus Mandar ini. Permisi yang tercatat adalah `tabeq`. Kalimat makan yang tercetak utuh adalah `meloaq ummande`, bukan `meloqaq makan`. `di rumah` tidak ada pada contoh itu. Label: mixed. "Tabeq. Meloaq ummande. Nanti aku ke rumah, kabari kalau sudah dekat."
