import streamlit as st

def hitung_kecukupan_gizi_umur_berat_badan_tinggi_umum(umur, berat_badan, tinggi, jenis_kelamin):
    # Hitung kebutuhan energi dasar (Basal Metabolic Rate/BMR) berdasarkan rumus Harris-Benedict
    if jenis_kelamin.lower() == 'laki-laki':
        bmr = 88.362 + (13.397 * berat_badan) + (4.799 * tinggi) - (5.677 * umur)
    elif jenis_kelamin.lower() == 'perempuan':
        bmr = 447.593 + (9.247 * berat_badan) + (3.098 * tinggi) - (4.330 * umur)
    else:
        return "Jenis kelamin tidak valid"

    # Hitung Total Energy Expenditure (TEE) berdasarkan aktivitas fisik
    # Misalnya, menggunakan faktor aktivitas fisik sedentary (1.2)
    faktor_aktivitas = 1.2
    tee = bmr * faktor_aktivitas

    # Hitung kebutuhan energi total (Total Daily Energy Expenditure/TDEE) perhari
    tdee = tee

    return tdee

def main():
    st.title('Kalkulator Kecukupan Gizi')

    # Penjelasan sebelum kalkulator
    st.write("Selamat datang di Kalkulator Kecukupan Gizi! Aplikasi ini dapat membantu Anda menghitung kebutuhan energi harian berdasarkan umur, berat badan, tinggi, jenis kelamin, dan tingkat aktivitas fisik. "
             "Silakan isi informasi Anda di bawah ini dan tekan tombol 'Hitung' untuk melihat hasilnya.")

    umur = st.number_input('Masukkan umur (tahun)', min_value=0, step=1)
    berat_badan = st.number_input('Masukkan berat badan (kg)', min_value=0.0, step=0.1)
    tinggi = st.number_input('Masukkan tinggi (cm)', min_value=0.0, step=0.1)
    jenis_kelamin = st.selectbox('Pilih jenis kelamin', ['Laki-laki', 'Perempuan'])

    # Pilihan tingkat aktivitas fisik
    aktivitas_fisik_options = ['Sangat Ringan (Tidak beraktivitas atau beraktivitas ringan)',
                               'Ringan (Beraktivitas ringan, seperti duduk)',
                               'Sedang (Beraktivitas sedang, seperti berjalan kaki)',
                               'Berat (Beraktivitas berat, seperti berlari)',
                               'Sangat Berat (Beraktivitas sangat berat, seperti berolahraga intensitas tinggi setiap hari)']

    aktivitas_fisik = st.selectbox('Pilih tingkat aktivitas fisik', aktivitas_fisik_options)

    # Informasi nama anggota kelompok dan tim
    st.sidebar.title('Informasi Tim')
    st.sidebar.write('Kelompok 4')
    st.sidebar.write('Anggota:')
    st.sidebar.write('- Amara Rifa Pratamy 2320506')
    st.sidebar.write('- Muhammad Baldiyansyah 2320536')
    st.sidebar.write('- Shofi Nabila Khoirunnisa 2320556')
    st.sidebar.write('- Tabitha Zoeana Salsabila 2320560')
    st.sidebar.write('- Afdatul Saputra 2120377')

    # Tabel informasi kalori makanan
    st.write("Tabel Informasi Kalori Makanan:")
    kalori_makanan = {
        "Makanan": ["Nasi putih", "Nasi merah", "Kentang rebus", "Ubi jalar", "Singkong", "Roti putih", "Roti gandum", "Mi goreng instan", "Dada ayam goreng (dengan kulit)", "Dada ayam goreng (tanpa kulit)", "Bebek goreng", "Ikan kembung", "Ikan lele goreng", "Ikan salmon panggang", "Udang goreng tepung", "Bakso sapi", "Chicken nugget", "Telur orak arik", "Telur rebus", "Telur dadar", "Telur ceplok", "Tempe goreng", "Tempe bacem", "Tahu bacem", "Tahu isi", "Tahu bakso", "Tahu sumedang", "Tumis labu siam", "Tumis kangkung", "Tumis kacang panjang dan tempe", "Sambal goreng kentang", "Perkedel kentang", "Apel", "Pisang", "Jambu biji", "Jambu air", "Semangka", "Melon", "Alpukat", "Anggur", "Jeruk", "Salak", "Manggis", "Mangga manalagi", "Buah naga", "Pepaya"],
        "Jumlah": ["100 gram", "100 gram", "100 gram", "100 gram", "100 gram", "1 iris", "1 iris", "80 gram", "100 gram", "100 gram", "100 gram", "100 gram", "100 gram", "100 gram", "100 gram", "100 gram", "100 gram", "100 gram", "2 btr telur sedang", "1 btr sedang", "1 btr besar", "1 btr besar", "1 porsi", "1 porsi", "1 porsi", "1 porsi", "1 porsi", "1 porsi", "100 gram", "85 gram", "110 gram", "100 gram", "75 gram", "1 buah sedang", "1 buah sedang", "1 buah", "1 buah", "100 gram", "100 gram", "100 gram", "100 gram", "1 buah", "100 gram", "1 buah", "100 gram", "1 buah", "100 gram"],
        "Kalori": ["175 kalori", "110 kalori", "87 kalori", "86 kalori", "160 kalori", "66 kalori", "67 kalori", "350 kalori", "216 kalori", "184 kalori", "286 kalori", "167 kalori", "105 kalori", "171 kalori", "150 kalori", "202 kalori", "297 kalori", "199 kalori", "68 kalori", "93 kalori", "92 kalori", "118 kalori", "157 kalori", "119 kalori", "124 kalori", "119 kalori", "113 kalori", "106 kalori", "155 kalori", "102 kalori", "107 kalori", "117 kalori", "72 kalori", "105 kalori", "37 kalori", "55 kalori", "30 kalori", "34 kalori", "322 kalori", "69 kalori", "62 kalori", "8 kalori", "73 kalori", "72 kalori", "50 kalori", "39 kalori"]
    }
    st.table(kalori_makanan)

    asupan_kalori = st.number_input('Masukkan jumlah kalori yang Anda konsumsi hari ini', min_value=0.0, step=0.1)

    if st.button('Hitung'):
        kecukupan_gizi = hitung_kecukupan_gizi_umur_berat_badan_tinggi_umum(umur, berat_badan, tinggi, jenis_kelamin)
        st.write("Angka Kecukupan Gizi perhari:", kecukupan_gizi, "kcal")

        # Membandingkan asupan kalori dengan kebutuhan kalori harian
        if asupan_kalori < kecukupan_gizi:
            st.write("Asupan kalori Anda kurang dari kebutuhan harian Anda. Pastikan untuk mengonsumsi makanan yang cukup untuk memenuhi kebutuhan gizi Anda.")
            st.write("Disarankan untuk menambahkan makanan bergizi seperti buah, sayuran, protein, dan karbohidrat kompleks.")
        elif asupan_kalori > kecukupan_gizi:
            st.write("Asupan kalori Anda melebihi kebutuhan harian Anda. Pastikan untuk mengonsumsi makanan dengan bijak dan sesuai dengan kebutuhan gizi Anda.")
            st.write("Disarankan untuk mengurangi konsumsi makanan tinggi lemak jenuh, gula tambahan, dan garam.")
        else:
            st.write("Asupan kalori Anda telah mencukupi kebutuhan harian Anda. Pertahankan pola makan yang seimbang untuk menjaga kesehatan Anda.")

        # Informasi tips untuk menjaga kalori agar sesuai dengan kebutuhan
        st.subheader("Tips Menjaga Kalori Sesuai dengan Kebutuhan:")
        st.write("1. Pilih makanan yang kaya akan nutrisi seperti buah-buahan, sayuran, biji-bijian utuh, dan protein tanpa lemak.")
        st.write("2. Kurangi konsumsi makanan dan minuman tinggi gula tambahan, lemak jenuh, dan garam.")
        st.write("3. Perhatikan porsi makanan Anda dan hindari makan berlebihan.")
        st.write("4. Perbanyak aktivitas fisik dengan berolahraga secara teratur.")
        st.write("5. Minumlah cukup air setiap hari untuk menjaga hidrasi tubuh.")

if __name__ == "__main__":
    main()
