import itertools
import random

# ==============================
# wordlist-indonesia-2025.py
# ==============================

# Nama depan populer
nama_depan = [
    "andi","budi","agus","siti","putri","ani","agus","joko","fariz","eka",
    "rudi","dwi","tono","yudi","adi","rizki","nanda","lina","ratna","dian",
    "agus","wahyu","rio","bagus","sri","wulan","fitri","yusuf","nina","fajar"
]

# Nama belakang populer
nama_belakang = [
    "pratama","saputra","maulana","fauzi","hidayat","permana","setiawan",
    "rahman","wijaya","kurniawan","siregar","hutapea","silalahi","manurung",
    "nababan","sitompul","simanjuntak","syahputra","putra","putri"
]

# Kota/daerah populer
daerah = [
    "jakarta","bandung","surabaya","medan","makassar","bekasi","tangerang",
    "depok","bogor","palembang","semarang","yogyakarta","denpasar","malang",
    "padang","pekanbaru","banjarmasin","pontianak","ambon","jayapura"
]

# Kata umum bahasa Indonesia
kata_umum = [
    "sayang","cinta","rahasia","indonesia","merdeka","anjing","kucing","bismillah",
    "alhamdulillah","123456","admin","root","ganteng","cantik","gratis","password",
    "sandi","sandiwara","doraemon","naruto","mobilelegends","ff","pubg","tiktok"
]

# Angka dan tahun
angka = ["123","1234","007","999","212","08","2024","2025"] + [str(x) for x in range(1990,2026)]

# Gabungan semua base words
base_words = nama_depan + nama_belakang + daerah + kata_umum

# Fungsi pembuat kombinasi
def generate_variants(words, numbers):
    variants = []
    for w in words:
        variants.append(w)
        for n in numbers:
            variants.append(w + str(n))
            variants.append(w + "_" + str(n))
            variants.append(w.capitalize() + str(n))
    return variants

# Buat kombinasi dasar
wordlist = set(generate_variants(base_words, angka))

# Gabungan nama depan + belakang
for nd in nama_depan:
    for nb in nama_belakang:
        wordlist.add(nd+nb)
        wordlist.add(nd+"_"+nb)
        wordlist.add(nd.capitalize()+nb.capitalize())
        for n in angka:
            wordlist.add(nd+nb+str(n))
            wordlist.add(nd+"_"+nb+str(n))

# Gabungan nama + daerah
for nd in nama_depan:
    for d in daerah:
        wordlist.add(nd+d)
        for n in angka:
            wordlist.add(nd+d+str(n))

# Konversi ke list dan acak
wordlist = list(wordlist)
random.shuffle(wordlist)

# Simpan ke file
output_file = "wordlist_full_indo_2025.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for w in wordlist:
        f.write(w + "\n")

print(f"[+] Wordlist berhasil dibuat: {output_file}")
print(f"[+] Total entry: {len(wordlist):,}")
print("[+] Wordlist sudah diacak agar lebih natural.")
