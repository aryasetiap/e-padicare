# 🌾 E-PadiCare

**E-PadiCare** adalah sebuah sistem pakar berbasis web yang dirancang untuk membantu petani atau pengguna dalam mendiagnosis penyakit pada tanaman padi. Sistem ini dibangun menggunakan model **Rule-Based Expert System** dan dikembangkan sebagai tugas pada mata kuliah **Sistem Pakar** di Program Studi Teknik Informatika, Universitas Lampung.

---

## 🧠 Latar Belakang

Tanaman padi merupakan salah satu komoditas utama di Indonesia. Namun, banyak petani masih kesulitan mengenali jenis penyakit yang menyerang tanaman mereka secara dini. E-PadiCare hadir sebagai solusi digital untuk membantu proses diagnosis berdasarkan gejala yang dialami oleh tanaman, sehingga petani bisa segera mengambil tindakan yang tepat.

---

## ⚙️ Fitur Utama

- ✅ Input gejala melalui form berbasis web
- ✅ Diagnosa otomatis berdasarkan basis aturan (rule-based)
- ✅ Output berupa nama penyakit dan saran penanganan
- ✅ Antarmuka sederhana dan responsif

---

## 🏗️ Teknologi yang Digunakan

- **Backend**: Python + Flask
- **Frontend**: HTML, CSS, JavaScript, Bootstrap (opsional)
- **Database**: SQLite (pengembangan), MySQL/PostgreSQL (produksi)
- **Template Engine**: Jinja2
- **Rule Engine**: Custom Rule-Based System (IF-THEN)

---

## 🗂️ Struktur Direktori

    e-padicare/
    │
    ├── app/ # Direktori utama aplikasi
    │ ├── **init**.py # Inisialisasi aplikasi Flask
    │ ├── routes.py # Routing aplikasi (endpoint dan tampilan)
    │ ├── rules_engine.py # Logika inferensi sistem pakar (engine berbasis rule)
    │ ├── models.py # Struktur data atau model yang digunakan
    │ ├── templates/ # Template HTML (menggunakan Jinja2)
    │ └── static/ # File statis seperti CSS, JS, gambar
    │
    ├── data/
    │ └── rules.json # Basis aturan (rules) untuk diagnosis penyakit padi
    │
    ├── tests/ # Direktori pengujian aplikasi
    │ ├── instance/ # Konfigurasi testing khusus, jika diperlukan
    │ ├── config.py # Konfigurasi untuk testing
    │ ├── run.py # Skrip untuk menjalankan testing
    │ ├── requirements.txt # Daftar dependensi untuk environment testing
    │ └── tests/ # Kumpulan file pengujian unit/integrasi
    │
    └── README.md # Dokumentasi utama proyek

---

## 🚀 Cara Menjalankan Aplikasi (Development)

1. **Clone repository**

   ```bash
   git clone https://github.com/aryasetiap/e-padicare.git
   cd e-padicare
   ```

2. **Buat virtual environment & install dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Jalankan aplikasi**

   ```bash
   python run.py
   ```

4. **Akses aplikasi melalui browser**

   ```bash
   http://localhost:5000
   ```

---

## 👨‍🎓 Tentang Proyek

- **Nama Proyek:** E-PadiCare
- **Mata Kuliah:** Sistem Pakar
- **Program Studi:** Teknik Informatika, Universitas Lampung
- **Pengembang:**
  - **Arya Setia Pratama**
  - **Amalia Rizki Puspadewi**
  - **Tri Novita**

---

## 📄 Lisensi

Proyek ini dikembangkan untuk keperluan akademik dan bersifat open-source. Silakan gunakan dan kembangkan sesuai kebutuhan, dengan tetap mencantumkan kredit.

---

## 🙌 Kontribusi

Jika kamu tertarik untuk mengembangkan proyek ini lebih lanjut (misalnya untuk riset, KKN, atau inovasi pertanian digital), silakan hubungi dan buat pull request!

---
