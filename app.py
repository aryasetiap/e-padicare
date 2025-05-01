import streamlit as st
from cf_engine import inferensi_cf, gejala
import time

def tampilkan_hasil_diagnosa(hasil):
    """
    Menampilkan hasil diagnosa berdasarkan hasil inferensi Certainty Factor (CF).
    """
    if hasil:
        hasil.sort(key=lambda x: x['cf'], reverse=True)
        st.subheader("🌾 Hasil Diagnosa:")

        ditampilkan = 0
        for penyakit in hasil:
            if penyakit['cf'] > 0.4:  # Tampilkan hanya penyakit dengan CF > 0.4
                persentase_cf = round(penyakit['cf'] * 100, 2)
                st.success(
                    f"**Penyakit:** {penyakit['nama']}  \n"
                    f"**Akurasi:** {persentase_cf}%"
                )
                with st.expander("💡 Saran Penanganan"):
                    st.write(penyakit['solusi'])
                ditampilkan += 1

        if ditampilkan == 0:
            st.info("Tidak ada penyakit dengan tingkat kepastian yang cukup tinggi. Silakan tambahkan beberapa gejala lagi.")
    else:
        st.write("Tidak ada penyakit yang terdeteksi berdasarkan gejala yang diberikan.")

def input_gejala():
    """
    Menampilkan antarmuka pengguna untuk memilih gejala dan tingkat keyakinan,
    serta melakukan diagnosa penyakit berdasarkan input pengguna.
    """
    tab1, tab2 = st.tabs(["🏠 Home", "🧪 Diagnosa"])

    with tab1:
        st.markdown("""
        **e-PadiCare** adalah Sistem Pakar untuk membantu petani dalam mendiagnosis penyakit pada tanaman padi  
        berdasarkan gejala-gejala yang muncul menggunakan metode *Certainty Factor (CF)*.
        
        👉 Silakan buka tab **Diagnosa** untuk memulai pengecekan.  
        """)
        st.markdown("---")
        st.subheader("Tentang Pengembang")
        st.markdown("""
        - 👨‍💻 **Arya Setia Pratama** (2215061034)  
        - 👩‍💻 **Amalia Rizki Puspadewi** (2215061081)  
        - 👩‍💻 **Tri Novita** (2215061079)  

        Program Studi Teknik Informatika  
        Universitas Lampung - 2025
        """)

    with tab2:
        st.header("Diagnosa Penyakit Tanaman Padi 🌾")
        st.write("Pilih gejala yang muncul pada tanaman padi Anda, lalu atur tingkat keyakinan terhadap gejala tersebut:")

        input_user = {}
        jumlah_dipilih = 0

        st.markdown("### Pilih Gejala dan Tingkat Keyakinan")
        for g in gejala:
            with st.expander(f"🌱 {gejala[g]}", expanded=False):
                dipilih = st.checkbox(f"Saya mengalami gejala ini", key=f"check_{g}")
                if dipilih:
                    confidence = st.slider(
                        "Seberapa yakin Anda?",
                        min_value=0.3,
                        max_value=1.0,
                        value=0.66,
                        step=0.1,
                        key=f"slider_{g}"
                    )
                    input_user[g] = confidence
                    jumlah_dipilih += 1

        if st.button("🔍 Diagnosa Sekarang"):
            if jumlah_dipilih == 0:
                st.warning("Harap pilih minimal satu gejala untuk didiagnosa.")
            else:
                with st.spinner("🔄 Menganalisis gejala..."):
                    time.sleep(1.5)  # Simulasi proses agar spinner sempat muncul
                    hasil = inferensi_cf(input_user)
                    tampilkan_hasil_diagnosa(hasil)

# Judul utama aplikasi
st.title("Selamat Datang di E-PadiCare 🌾")
st.image("image.png", use_container_width=True)

if __name__ == "__main__":
    input_gejala()

# Footer aplikasi
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 14px; color: gray;'>
        <p>© 2025 e-PadiCare</p>
        <p>Dikembangkan oleh:</p>
        <p><strong>Arya Setia Pratama</strong> (2215061034)         <strong>Amalia Rizki Puspadewi</strong> (2215061081)            <strong>Tri Novita</strong> (2215061079)</p>
        <p>Program Studi Teknik Informatika, Universitas Lampung</p>
    </div>
    """,
    unsafe_allow_html=True
)
