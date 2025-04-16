# Bobot gejala yang digunakan untuk menghitung nilai CF (Certainty Factor) berdasarkan input pengguna
bobot_gejala = {
    "G1": 0.9, "G2": 0.7, "G3": 0.8, "G4": 0.7,
    "G5": 0.6, "G6": 0.6, "G7": 0.3, "G8": 0.8,
    "G9": 0.5, "G10": 0.5, "G11": 0.4, "G12": 0.7,
    "G13": 0.6, "G14": 0.5, "G15": 0.9, "G16": 0.6,
    "G17": 0.6, "G18": 0.8, "G19": 0.8
}

# Aturan (rules) yang menghubungkan penyakit dengan gejala-gejalanya
rules = {
    "P1": {"nama": "Blast", "gejala": ["G1", "G2"]},
    "P2": {"nama": "Hawar Daun", "gejala": ["G3"]},
    "P3": {"nama": "Hawar Pelepah", "gejala": ["G4", "G16", "G17"]},
    "P4": {"nama": "Busuk Leher", "gejala": ["G2", "G5"]},
    "P5": {"nama": "Gosong Akar", "gejala": ["G6", "G7"]},
    "P6": {"nama": "Hawar Daun Bakteri", "gejala": ["G9", "G7"]},
    "P7": {"nama": "Bercak Daun Bakteri", "gejala": ["G8"]},
    "P8": {"nama": "Tungro", "gejala": ["G9", "G10", "G11"]},
    "P9": {"nama": "Kerdil Rumput", "gejala": ["G11", "G10"]},
    "P10": {"nama": "Kerdil Hampa", "gejala": ["G11", "G12"]},
    "P11": {"nama": "Busuk Batang", "gejala": ["G13", "G7", "G14"]},
    "P12": {"nama": "Karat Daun Padi", "gejala": ["G15"]},
    "P13": {"nama": "Fusarium", "gejala": ["G18", "G19"]}
}

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
        return 0  # Jika gejala tidak ada dalam input pengguna, nilai CF adalah 0
    cf_user = input_user[kode_gejala]  # Nilai keyakinan pengguna untuk gejala
    bobot = bobot_gejala.get(kode_gejala, 0)  # Bobot gejala
    return bobot * cf_user  # Mengalikan bobot dengan nilai keyakinan pengguna

def gabung_cf(cf_list):
    """
    Menggabungkan nilai-nilai CF menggunakan formula kombinasi CF.

    Args:
        cf_list (list): Daftar nilai CF yang akan digabungkan.

    Returns:
        float: Nilai CF gabungan.
    """
    if not cf_list:
        return 0  # Jika daftar kosong, nilai CF gabungan adalah 0
    cf_total = cf_list[0]  # Inisialisasi dengan nilai CF pertama
    for cf in cf_list[1:]:
        # Formula kombinasi CF: CFtotal = CFtotal + CFbaru * (1 - CFtotal)
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
    hasil = []  # Menyimpan hasil inferensi
    for kode_p, data in rules.items():
        cf_list = []  # Menyimpan nilai CF untuk setiap gejala dalam aturan
        for g in data["gejala"]:
            cf_g = hitung_cf_gejala(g, input_user, bobot_gejala)  # Hitung CF untuk gejala
            if cf_g > 0:
                cf_list.append(cf_g)  # Tambahkan ke daftar jika CF > 0
        if cf_list:
            cf_total = gabung_cf(cf_list)  # Gabungkan nilai CF
            hasil.append({
                "kode": kode_p,
                "nama": data["nama"],
                "cf": round(cf_total, 3)  # Simpan hasil dengan pembulatan 3 desimal
            })
    # Urutkan hasil berdasarkan nilai CF secara menurun
    hasil.sort(key=lambda x: x["cf"], reverse=True)
    return hasil
