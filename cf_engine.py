# List Gejala dan Bobot
gejala_list = [
    ("G001", "Padi mengalami kerusakan sejak dari pesemaian hingga dalam penyimpanan", 0.9),
    ("G002", "Tanaman yang terserang banyak bekas potongan dan terdapat bekas gigitan", 0.9),
    ("G003", "Kerusakan tanaman banyak kelihatan pada pagi hari", 0.9),
    ("G004", "Daun dan batang hilang dari pertanaman", 0.9),
    ("G005", "Banyak potongan daun dan batang terlihat mengambang", 0.9),
    ("G006", "Padi banyak terserang saat fase matang susu sampai pemasakan biji (sebelum panen)", 0.9),
    ("G007", "Banyak biji hampa dan hilang", 0.9),
    ("G008", "Banyaknya kupu-kupu kecil berwarna putih pada sore dan malam hari", 0.9),
    ("G009", "Banyak daun padi muda menguning dan mati", 0.9),
    ("G010", "Padi yang sedang bunting buliran padinya keluar, berguguran, gabah-gabah kosong dan berwarna keabu-abuan", 0.7),
    ("G011", "Banyak binatang kecil di tempat lembab, gelap dan teduh", 0.6),
    ("G012", "Banyak malai dan bulir padi yang hampa", 0.4),
    ("G013", "Tanaman kerdil", 0.2),
    ("G014", "Tanaman padi terserang pada fase masak susu", 0.9),
    ("G015", "Terdapat bekas tusukan dan pecah", 0.9),
    ("G016", "Daun menggulung rapat seperti daun bawang", 0.9),
    ("G017", "Daun memucat, menguning, akhirnya kering", 0.9),
    ("G018", "Daun terpotong seperti digunting", 0.9),
    ("G019", "Tanaman padi yang diserang kebanyakan berasal dari bibit-bibit lemah", 0.9),
    ("G020", "Tanaman terpotong pada pangkal batang", 0.9),
    ("G021", "Rusaknya akar muda dan bagian pangkal tanaman yang berada di bawah tanah", 0.9),
    ("G022", "Tanaman padi muda yang diserang mati sehingga terlihat adanya spot-spot kosong di sawah", 0.9),
    ("G023", "Warna daun menjadi kemerahan, atau daun-daun luar menguning, akhirnya menjadi kering", 0.9),
    ("G024", "Pertumbuhan panjang terhenti, sehingga daun-daun teratur seperti kipas", 0.9),
    ("G025", "Bunga tetap tersimpan di dalam upih-upih daun", 0.9),
    ("G026", "Ujung daun berwarna kuning, hijau jingga atau kuning cokelat", 0.9),
    ("G027", "Pada daun yang masih muda terdapat bintik-bintik cokelat", 0.9),
    ("G028", "Pada daun terdapat bercak klorotis", 0.9),
    ("G029", "Daunnya berbintik-bintik kecil berwarna cokelat hitam", 0.9),
    ("G030", "Tanaman yang terserang justru malah banyak anakanya", 0.9),
    ("G031", "Daunnya sempit dan lancip", 0.9),
    ("G032", "Daun memutih kemudian menguning", 0.9),
    ("G033", "Pada satu rumpun terdapat banyak anakan", 0.9),
    ("G034", "Pada pucuk daun bagian atas, terdapat bercak-bercak kuning dan bercak-bercak tersebut sejajar dengan tulang daun", 0.9),
    ("G035", "Pada serangan yang berat, penyakitnya merusak titik tumbuh, dan menyebabkan matinya tanaman itu", 0.9)
]

# Membuat dictionary untuk gejala dan bobotnya
gejala = {kode: deskripsi for kode, deskripsi, _ in gejala_list}
bobot_gejala = {kode: bobot for kode, _, bobot in gejala_list}

# Basis pengetahuan untuk penyakit dan gejalanya
rules = {
    "J001": {
        "nama": "Tikus",
        "gejala": ["G001", "G002", "G003"],
        "solusi": "Bersihkan gulma dan semak, pasang jebakan, dan tanam serempak untuk mengurangi populasi tikus."
    },
    "J002": {
        "nama": "Keong Mas",
        "gejala": ["G004", "G005"],
        "solusi": "Kumpulkan keong secara manual, gunakan umpan beracun, dan jaga kebersihan saluran air."
    },
    "J003": {
        "nama": "Burung",
        "gejala": ["G006", "G007"],
        "solusi": "Gunakan orang-orangan sawah dan jaring pelindung untuk mengusir burung."
    },
    "J004": {
        "nama": "Sundep (Scirpophaga innotata)",
        "gejala": ["G008", "G009", "G010"],
        "solusi": "Gunakan pestisida selektif dan lakukan rotasi tanaman untuk mencegah siklus hidup sundep."
    },
    "J005": {
        "nama": "Ulat",
        "gejala": ["G011", "G012"],
        "solusi": "Gunakan insektisida berbahan aktif emamektin benzoat atau pestisida nabati."
    },
    "J006": {
        "nama": "Wereng",
        "gejala": ["G011", "G012", "G013"],
        "solusi": "Gunakan varietas tahan wereng, tanam serempak, dan kendalikan dengan insektisida imidakloprid."
    },
    "J007": {
        "nama": "Walang Sangit",
        "gejala": ["G014", "G012", "G015"],
        "solusi": "Gunakan perangkap alami, tanam serempak, dan semprot insektisida kontak seperti sipermetrin."
    },
    "J008": {
        "nama": "Ganjur",
        "gejala": ["G016", "G017"],
        "solusi": "Jaga kebersihan lahan dan kendalikan dengan insektisida berbasis organofosfat."
    },
    "J009": {
        "nama": "Hama Putih",
        "gejala": ["G018", "G019"],
        "solusi": "Semprot insektisida sistemik seperti abamektin dan gunakan varietas tahan."
    },
    "J010": {
        "nama": "Orong-Orong",
        "gejala": ["G020", "G021", "G022"],
        "solusi": "Gunakan umpan beracun dan jaga kebersihan lahan."
    },
    "J011": {
        "nama": "Penggerek Batang",
        "gejala": ["G013", "G023", "G024", "G025"],
        "solusi": "Gunakan insektisida sistemik dan buang bagian tanaman yang terserang."
    },
    "J012": {
        "nama": "Tungro",
        "gejala": ["G013", "G026", "G027"],
        "solusi": "Gunakan varietas tahan dan kendalikan vektor wereng hijau."
    },
    "J013": {
        "nama": "Kerdil Rumput",
        "gejala": ["G028", "G029", "G030", "G013", "G031"],
        "solusi": "Tanam serempak dan semprot insektisida untuk kendalikan vektor."
    },
    "J014": {
        "nama": "Kerdil Kuning",
        "gejala": ["G032", "G033", "G013"],
        "solusi": "Gunakan varietas tahan, benih sehat, dan semprot insektisida."
    },
    "J015": {
        "nama": "Kresek (Hawar Daun Bakteri)",
        "gejala": ["G034", "G035"],
        "solusi": "Gunakan benih sehat, semprot bakterisida, dan hindari pemupukan nitrogen berlebih."
    }
}

def konsultasi(gejala_terpilih):
    """
    Melakukan konsultasi menggunakan metode forward chaining untuk mencocokkan gejala dengan penyakit.

    Args:
        gejala_terpilih (list): Daftar kode gejala yang dipilih pengguna.

    Returns:
        list: Daftar penyakit yang cocok dengan gejala yang dipilih, diurutkan berdasarkan bobot total.
    """
    hasil = []
    for kode, data in rules.items():
        if all(g in gejala_terpilih for g in data["gejala"]):
            total_bobot = sum(bobot_gejala.get(g, 0) for g in data["gejala"])
            hasil.append({
                "kode": kode,
                "nama": data["nama"],
                "solusi": data["solusi"],
                "bobot_total": round(total_bobot, 2)
            })
    hasil.sort(key=lambda x: x["bobot_total"], reverse=True)
    return hasil

def hitung_cf_gejala(kode_gejala, input_user, bobot_gejala):
    """
    Menghitung nilai CF (Certainty Factor) untuk sebuah gejala berdasarkan input pengguna.

    Args:
        kode_gejala (str): Kode gejala yang akan dihitung.
        input_user (dict): Input dari pengguna berupa nilai keyakinan untuk setiap gejala.
        bobot_gejala (dict): Bobot gejala yang telah ditentukan.

    Returns:
        float: Nilai CF untuk gejala tersebut.
    """
    if kode_gejala not in input_user:
        return 0
    cf_user = input_user[kode_gejala]
    bobot = bobot_gejala.get(kode_gejala, 0)
    return bobot * cf_user

def gabung_cf(cf_list):
    """
    Menggabungkan nilai-nilai CF menggunakan formula kombinasi CF.

    Args:
        cf_list (list): Daftar nilai CF yang akan digabungkan.

    Returns:
        float: Nilai CF gabungan.
    """
    if not cf_list:
        return 0
    cf_total = cf_list[0]
    for cf in cf_list[1:]:
        cf_total = cf_total + cf * (1 - cf_total)
    return cf_total

def inferensi_cf(input_user):
    """
    Melakukan inferensi untuk menentukan penyakit berdasarkan gejala yang diberikan pengguna.

    Args:
        input_user (dict): Input dari pengguna berupa nilai keyakinan untuk setiap gejala.

    Returns:
        list: Daftar penyakit yang terdeteksi beserta nilai CF-nya, diurutkan dari yang tertinggi.
    """
    hasil = []
    for kode_p, data in rules.items():
        cf_list = []
        for g in data["gejala"]:
            cf_g = hitung_cf_gejala(g, input_user, bobot_gejala)
            if cf_g > 0:
                cf_list.append(cf_g)
        if cf_list:
            cf_total = gabung_cf(cf_list)
            hasil.append({
                "kode": kode_p,
                "nama": data["nama"],
                "cf": round(cf_total, 3),
                "solusi": data.get("solusi", "Belum ada solusi tersedia.")
            })
    hasil.sort(key=lambda x: x["cf"], reverse=True)
    return hasil
