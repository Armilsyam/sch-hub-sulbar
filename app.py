import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="SCH-Hub Sulbar", page_icon="🥥", layout="wide")

# --- HEADER ---
st.title("🥥 Transformasi Ekonomi Sulawesi Barat")
st.subheader("Hilirisasi Komoditas Kelapa Melalui Model *Strategic Coconut Hilirization Hub* (SCH-Hub)")
st.markdown("---")

# --- SIDEBAR UNTUK NAVIGASI ---
st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman:", ["Latar Belakang & Analisis", "Konsep SCH-Hub", "Prediksi & Proyeksi Ekonomi"])

# --- HALAMAN 1: LATAR BELAKANG ---
if menu == "Latar Belakang & Analisis":
    st.header("Anomali dan Kerentanan Struktural Ekonomi")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Pondasi Perekonomian (2025)**\n\nSektor Pertanian, Kehutanan, dan Perikanan mendominasi dengan pangsa PDRB mencapai **47,71%**.")
        st.success("**Pertumbuhan Industri**\n\nSektor Industri Pengolahan mencatatkan pertumbuhan tertinggi sebesar **15,81%** (c-to-c).")
    with col2:
        st.error("**Kerentanan Struktural (Monokultur)**\n\n**91,49%** aktivitas industri pengolahan bersandar pada makanan-minuman berbasis kelapa sawit (CPO).")
        st.warning("**Kebocoran Ekonomi Lokal**\n\nPetani menjual kelapa butiran mentah/kopra bermutu rendah, menyebabkan *local economic leakage* ke wilayah luar provinsi.")

    st.markdown("### Mengapa Kelapa (Cocos nucifera)?")
    st.write("Kelapa memiliki keunggulan kompetitif (luas lahan dan produksi) di peringkat 4 besar regional Sulawesi. Pengembangan komoditas non-sawit mutlak diperlukan untuk mengurai ketergantungan pada *single-commodity*.")

# --- HALAMAN 2: KONSEP SCH-HUB ---
elif menu == "Konsep SCH-Hub":
    st.header("5 Pilar Strategic Coconut Hilirization Hub (SCH-Hub)")
    st.write("Rekayasa ekosistem hulu-hilir secara terbuka dan komprehensif:")
    
    st.write("") # Memberi sedikit jarak (spacer)

    # Susunan Baris 1 (2 Kolom)
    col1, col2 = st.columns(2)
    col1.metric("Pilar 1", "Investasi Manufaktur", "Klaster Terpadu")
    col2.metric("Pilar 2", "Digitalisasi Rantai Pasok", "Supply Chain Terhubung")
    
    st.write("") # Spacer
    
    # Susunan Baris 2 (2 Kolom)
    col3, col4 = st.columns(2)
    col3.metric("Pilar 3", "Penciptaan Lapangan Kerja", "Ekonomi Sirkular")
    col4.metric("Pilar 4", "Reformasi Kelembagaan", "Korporatisasi (BUMP)")

    st.write("") # Spacer

    # Susunan Baris 3 (Dibuat di tengah dengan trik rasio kolom)
    left_spacer, center_col, right_spacer = st.columns([1, 2, 1])
    center_col.metric("Pilar 5", "Inovasi Produksi", "Smart Farming")

    st.markdown("---")
    st.subheader("Diversifikasi Produk Hilirisasi")
    st.write("Mengubah kelapa butiran menjadi produk bernilai tinggi:")
    st.markdown("- 🥥 **Desiccated Coconut** (Kelapa Parut Kering)\n- 🧪 **Virgin Coconut Oil (VCO)**\n- 🔥 **Activated Carbon** (Arang Aktif dari Tempurung)")

# --- HALAMAN 3: PREDIKSI MASA DEPAN (MACHINE LEARNING) ---
elif menu == "Prediksi & Proyeksi Ekonomi":
    st.header("📈 Prediksi Berbasis Machine Learning")
    st.write("Unggah dataset historis (CSV) untuk memprediksi Populasi, Kebutuhan Lapangan Kerja, atau Nilai Komoditas di masa depan.")

    # 1. UNGGAH DATASET
    uploaded_file = st.file_uploader("Unggah File Dataset (Format .csv)", type=["csv"])
    
    # Memberikan contoh format dataset yang benar jika pengguna belum mengunggah
    with st.expander("Lihat Panduan Format CSV yang Dibutuhkan"):
        st.markdown("""
        Pastikan file CSV Anda memiliki kolom **Tahun** sebagai acuan waktu, dan kolom metrik lainnya. Contoh:
        | Tahun | Populasi_Sulbar | Lapangan_Kerja_Tersedia | Produksi_Kelapa_Ton |
        |---|---|---|---|
        | 2015 | 1300000 | 45000 | 50000 |
        | 2016 | 1320000 | 47000 | 52000 |
        """)

    if uploaded_file is not None:
        try:
            # Membaca data
            df = pd.read_csv(uploaded_file)
            st.success("Dataset berhasil dimuat!")
            
            st.subheader("1. Eksplorasi & Pembersihan Data Mentah")
            st.dataframe(df.head())

            # Pastikan ada kolom 'Tahun'
            if 'Tahun' not in df.columns:
                st.error("Error: Dataset harus memiliki kolom bernama 'Tahun'.")
            else:
                # 2. DATA CLEANING (Pembersihan Data)
                # Mengisi nilai yang kosong (NaN) dengan nilai rata-rata (mean) dari kolom tersebut
                df_cleaned = df.fillna(df.mean(numeric_only=True))
                st.write("**Status Pembersihan:** Nilai kosong (NaN) telah ditangani menggunakan nilai rata-rata.")

                # Memilih variabel yang ingin diprediksi
                kolom_metrik = [col for col in df_cleaned.columns if col != 'Tahun']
                target_col = st.selectbox("Pilih Metrik yang Ingin Diprediksi (Misal: Lapangan Kerja / Produksi):", kolom_metrik)
                
                tahun_prediksi = st.slider("Prediksi Berapa Tahun ke Depan?", min_value=1, max_value=20, value=5)

                if st.button("Jalankan Prediksi AI"):
                    from sklearn.linear_model import LinearRegression
                    from sklearn.preprocessing import MinMaxScaler
                    
                    st.markdown("---")
                    st.subheader(f"📊 Hasil Prediksi: {target_col}")

                    # 3. NORMALISASI DATA (Opsional untuk Regresi Linear sederhana, namun baik sebagai standar ML)
                    # Kita pisahkan X (Tahun) dan y (Target)
                    X = df_cleaned[['Tahun']].values
                    y = df_cleaned[[target_col]].values

                    scaler_X = MinMaxScaler()
                    scaler_y = MinMaxScaler()

                    X_scaled = scaler_X.fit_transform(X)
                    y_scaled = scaler_y.fit_transform(y)

                    # 4. PEMODELAN (Regresi Linear)
                    model = LinearRegression()
                    model.fit(X_scaled, y_scaled) # Melatih model dengan data historis

                    # 5. MEMBUAT PREDIKSI KE DEPAN
                    tahun_terakhir = int(df_cleaned['Tahun'].max())
                    tahun_masa_depan = np.array([[tahun_terakhir + i] for i in range(1, tahun_prediksi + 1)])
                    
                    # Normalisasi tahun masa depan sebelum diprediksi
                    tahun_masa_depan_scaled = scaler_X.transform(tahun_masa_depan)
                    
                    # Prediksi
                    prediksi_scaled = model.predict(tahun_masa_depan_scaled)
                    
                    # Kembalikan nilai prediksi ke skala aslinya (Denormalisasi)
                    prediksi_asli = scaler_y.inverse_transform(prediksi_scaled)

                    # Menggabungkan data historis dan prediksi untuk visualisasi
                    df_historis = pd.DataFrame({'Tahun': df_cleaned['Tahun'], 'Nilai': df_cleaned[target_col], 'Keterangan': 'Historis'})
                    df_prediksi = pd.DataFrame({'Tahun': tahun_masa_depan.flatten(), 'Nilai': prediksi_asli.flatten(), 'Keterangan': 'Prediksi ML'})
                    
                    df_gabungan = pd.concat([df_historis, df_prediksi])

                    # 6. VISUALISASI HASIL PREDIKSI (PLOTLY)
                    fig = px.line(df_gabungan, x='Tahun', y='Nilai', color='Keterangan', 
                                  markers=True, title=f"Proyeksi {target_col} hingga Tahun {tahun_terakhir + tahun_prediksi}",
                                  color_discrete_map={"Historis": "blue", "Prediksi ML": "orange"})
                    
                    fig.update_layout(xaxis_title="Tahun", yaxis_title=target_col, template="plotly_white")
                    st.plotly_chart(fig, use_container_width=True)

                    # Menampilkan tabel data prediksi
                    st.write("### Detail Angka Prediksi")
                    df_prediksi_tabel = df_prediksi.drop(columns=['Keterangan'])
                    df_prediksi_tabel['Tahun'] = df_prediksi_tabel['Tahun'].astype(str) # Agar tidak pakai koma ribuan di tahun
                    
                    # Tampilkan metrik pertumbuhan
                    nilai_terakhir_historis = df_historis.iloc[-1]['Nilai']
                    nilai_akhir_prediksi = df_prediksi.iloc[-1]['Nilai']
                    persentase_tumbuh = ((nilai_akhir_prediksi - nilai_terakhir_historis) / nilai_terakhir_historis) * 100

                    col1, col2 = st.columns([1, 2])
                    with col1:
                        st.dataframe(df_prediksi_tabel, hide_index=True)
                    with col2:
                        st.metric(label=f"Proyeksi Pertumbuhan {target_col} ({tahun_terakhir} - {tahun_terakhir+tahun_prediksi})", 
                                  value=f"{nilai_akhir_prediksi:,.0f}", 
                                  delta=f"{persentase_tumbuh:.2f}%")
                        st.info("💡 **Catatan Analisis:** Model Regresi Linear ini mendeteksi tren dari data historis Anda. Jika Anda ingin menguji skenario SCH-Hub (lonjakan tiba-tiba), Anda perlu menambahkan kolom variabel intervensi (dummy variable) pada dataset Anda.")

        except Exception as e:
            st.error(f"Terjadi kesalahan saat memproses data. Pastikan format CSV sesuai. Detail Error: {e}")

# --- FOOTER ---
st.markdown("---")
st.caption("Dikembangkan berdasarkan Opini Ilmiah: Hilirisasi Kelapa; SCH-Hub; Rantai Pasok Terintegrasi; Sulawesi Barat.")
