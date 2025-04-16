import streamlit as st
from cf_engine import inferensi_cf

# Function to display the diagnosis results
def tampilkan_hasil_diagnosa(hasil):
    """
    Menampilkan hasil diagnosa berdasarkan hasil inferensi CF.

    Args:
        hasil (list): List hasil diagnosa yang berisi nama penyakit dan nilai CF.
    """
    if hasil:
        # Sort the results by certainty factor (CF) in descending order
        hasil.sort(key=lambda x: x['cf'], reverse=True)
        cf_tertinggi = hasil[0]['cf']
        for penyakit in hasil:
            if penyakit['cf'] == cf_tertinggi:
                persentase_cf = round(penyakit['cf'] * 100, 2)
                st.success(
                    f"**Penyakit:** {penyakit['nama']}  \n"
                    f"**Akurasi:** {persentase_cf}%"
                )
                with st.expander("💡 Saran Penanganan"):
                    st.write(penyakit['solusi'])
    else:
        # Display a message if no disease is detected
        st.write("Tidak ada penyakit yang terdeteksi berdasarkan gejala yang diberikan.")

# Function to handle user input for symptoms
def input_gejala():
    """
    Menampilkan antarmuka untuk pengguna memilih gejala dan melakukan diagnosa.
    """
    # Title and header for the application
    st.title("Sistem Pakar Diagnosis Penyakit Tanaman Padi 🌾🧑‍🌾👩‍🌾")
    st.image("image.png", use_container_width=True)
    st.write("Pilih gejala yang muncul pada tanaman padi Anda:")

    # Dictionary to store user input
    input_user = {}
    # List of symptoms and their descriptions
    gejala = {
        "G1": "Bercak belah ketupat di daun", 
        "G2": "Malai busuk", 
        "G3": "Bercak coklat besar di daun", 
        "G4": "Lesi abu/coklat di pelepah", 
        "G5": "Malai tidak tumbuh", 
        "G6": "Akar hitam", 
        "G7": "Tanaman layu", 
        "G8": "Garis coklat di daun", 
        "G9": "Ujung daun menguning", 
        "G10": "Banyak anakan", 
        "G11": "Tanaman kerdil", 
        "G12": "Daun sobek", 
        "G13": "Batang membusuk", 
        "G14": "Tanaman roboh", 
        "G15": "Bercak oranye di daun", 
        "G16": "Pelepah membusuk", 
        "G17": "Pelepah kering", 
        "G18": "Lesi/nekrosis di daun", 
        "G19": "Malai patah"
    }

    for g in gejala:
        confidence = st.radio(
            f"Seberapa yakin Anda dengan gejala: {gejala[g]}?",
            options=["Sangat Tidak Yakin", "Tidak Yakin", "Yakin", "Sangat Yakin"],
            index=0
        )
        
        if confidence == "Sangat Tidak Yakin":
            input_user[g] = 0.0
        elif confidence == "Tidak Yakin":
            input_user[g] = 0.33
        elif confidence == "Yakin":
            input_user[g] = 0.66
        elif confidence == "Sangat Yakin":
            input_user[g] = 1.0

    if st.button("Diagnosa"):
        if all(value == 0.0 for value in input_user.values()):
            st.warning("Harap pilih minimal satu gejala!")
        else:
            hasil = inferensi_cf(input_user)
            tampilkan_hasil_diagnosa(hasil)

if __name__ == "__main__":
    input_gejala()

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
