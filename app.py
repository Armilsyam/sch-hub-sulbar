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
    st.header("Integrasi Digital dan Ekonomi Sirkular")
    st.markdown("Menuju Sulawesi Barat yang Berdaya Saing Global melalui optimalisasi seluruh bagian komoditas kelapa (*Zero Waste*) dan keterhubungan digital.")

    st.markdown("---")
    
    # BAGIAN 1: ALUR HILIRISASI (EKONOMI SIRKULAR)
    st.subheader("🔄 Alur Hilirisasi Komoditas (Peningkatan Nilai Tambah)")
    st.write("Mengubah kelapa butiran mentah menjadi deretan produk bernilai jual tinggi:")

    # Fungsi untuk membuat baris alur agar rapi
    def buat_alur(bahan_mentah, produk_hilir, emoji_bahan, emoji_produk):
        col1, col2, col3 = st.columns([2, 1, 3])
        with col1:
            st.info(f"{emoji_bahan} **{bahan_mentah}**")
        with col2:
            st.markdown("<h2 style='text-align: center; margin-top: -10px;'>➔</h2>", unsafe_allow_html=True)
        with col3:
            st.success(f"{emoji_produk} **{produk_hilir}**")
            
    st.write("") # Spacer
    buat_alur("Daging Kelapa", "Virgin Coconut Oil (VCO) & Desiccated Coconut", "🥥", "🧪")
    buat_alur("Sabut Kelapa", "Cocofiber & Kerajinan Ekspor", "🟫", "🧶")
    buat_alur("Tempurung", "Activated Carbon (Arang Aktif) / Briket", "🌑", "🔥")
    buat_alur("Air Kelapa", "Nata de Coco", "💧", "🧊")

    st.markdown("---")

    # BAGIAN 2: 5 PILAR STRATEGIS DENGAN SCH-APP SEBAGAI PUSAT
    st.subheader("📱 5 Pilar Strategis Berpusat pada SCH-APP")
    st.write("Aplikasi cerdas **SCH-APP** bertindak sebagai ekosistem penghubung (*Hub*) dari hulu ke hilir.")

    st.write("") # Spacer

    # Membuat tata letak Hub (Kiri - Tengah - Kanan)
    col_kiri, col_tengah, col_kanan = st.columns([1, 1.5, 1])

    with col_kiri:
        st.metric("Pilar 1", "Reformasi Kelembagaan", "Korporatisasi Petani")
        st.write("")
        st.write("")
        st.metric("Pilar 2", "Rantai Pasok Terhubung", "Memotong Perantara")

    with col_tengah:
        # Membuat kotak visual untuk SCH-APP di tengah
        st.markdown("""
        <div style="background-color: #f0f2f6; padding: 40px 20px; border-radius: 20px; text-align: center; border: 3px solid #2E86C1; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <h1 style="color: #2E86C1; margin-bottom: 0;">📱 SCH-APP</h1>
            <h4 style="margin-top: 5px;">Digital Hub</h4>
            <hr style="margin: 10px 0;">
            <p style="font-size: 14px; color: #555;">Pusat kendali yang mengintegrasikan Data Petani, Proses Produksi, dan Permintaan Pasar secara <i>Real-Time</i>.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_kanan:
        st.metric("Pilar 3", "Lapangan Kerja Baru", "Sektor Sirkular")
        st.write("")
        st.write("")
        st.metric("Pilar 4", "Stimulus Investasi", "Fasilitas Manufaktur")

    st.write("") # Spacer

    # Pilar 5 diletakkan di tengah bawah untuk keseimbangan visual
    _, col_bawah_tengah, _ = st.columns([1, 1.5, 1])
    with col_bawah_tengah:
        st.metric("Pilar 5", "Inovasi Produksi", "Smart Farming Terapan")

    st.markdown("---")
    st.caption("Pondasi Ekonomi Sulbar (2025): Sektor Pertanian & Perkebunan mendominasi 47,71%. Target: Mendorong Sektor Industri Pengolahan melalui komoditas unggulan non-sawit.")

# --- HALAMAN 3: PREDIKSI MASA DEPAN (MACHINE LEARNING) ---
elif menu == "Prediksi & Proyeksi Ekonomi":
    st.header("📈 Prediksi Berbasis Machine Learning")
    st.write("Gunakan data historis untuk memprediksi tren produksi komoditas kelapa di masa depan menggunakan algoritma *Linear Regression*.")

    # Membuat dua tab: Input Manual dan Upload CSV
    tab1, tab2 = st.tabs(["✍️ Input Manual (5 Tahun Terakhir)", "📁 Unggah File CSV"])

    # ==========================================
    # TAB 1: INPUT MANUAL
    # ==========================================
    with tab1:
        st.subheader("Input Data Tonase Produksi (2021 - 2025)")
        st.write("Masukkan total produksi kelapa (dalam Ton) untuk 5 tahun terakhir pada kolom di bawah ini:")

        # Membuat 5 kolom sejajar untuk input tahunan
        col_thn1, col_thn2, col_thn3, col_thn4, col_thn5 = st.columns(5)
        
        with col_thn1:
            ton_2021 = st.number_input("Tahun 2021", min_value=0, value=45000, step=1000)
        with col_thn2:
            ton_2022 = st.number_input("Tahun 2022", min_value=0, value=47000, step=1000)
        with col_thn3:
            ton_2023 = st.number_input("Tahun 2023", min_value=0, value=48500, step=1000)
        with col_thn4:
            ton_2024 = st.number_input("Tahun 2024", min_value=0, value=51000, step=1000)
        with col_thn5:
            ton_2025 = st.number_input("Tahun 2025", min_value=0, value=52000, step=1000)

        tahun_prediksi_manual = st.slider("Prediksi Berapa Tahun ke Depan? (Manual)", min_value=1, max_value=10, value=5, key="slider_manual")

        if st.button("Jalankan Prediksi AI (Data Manual)", type="primary"):
            from sklearn.linear_model import LinearRegression
            
            # Menyusun data dari input manual menjadi DataFrame
            tahun_historis = [2021, 2022, 2023, 2024, 2025]
            data_tonase = [ton_2021, ton_2022, ton_2023, ton_2024, ton_2025]
            
            df_historis = pd.DataFrame({
                'Tahun': tahun_historis,
                'Produksi (Ton)': data_tonase,
                'Keterangan': 'Historis (Input Manual)'
            })

            # Pemodelan Regresi
            X = df_historis[['Tahun']].values
            y = df_historis[['Produksi (Ton)']].values
            
            model = LinearRegression()
            model.fit(X, y) # Melatih model dengan 5 titik data manual

            # Prediksi masa depan
            tahun_terakhir = 2025
            X_masa_depan = np.array([[tahun_terakhir + i] for i in range(1, tahun_prediksi_manual + 1)])
            prediksi_masa_depan = model.predict(X_masa_depan)

            # Menyusun DataFrame hasil prediksi
            df_prediksi = pd.DataFrame({
                'Tahun': X_masa_depan.flatten(),
                'Produksi (Ton)': prediksi_masa_depan.flatten(),
                'Keterangan': 'Prediksi ML'
            })

            df_gabungan = pd.concat([df_historis, df_prediksi])

            # Visualisasi Plotly
            st.markdown("---")
            st.subheader("📊 Proyeksi Produksi Komoditas Kelapa")
            fig = px.line(df_gabungan, x='Tahun', y='Produksi (Ton)', color='Keterangan', 
                          markers=True, text='Produksi (Ton)',
                          color_discrete_map={"Historis (Input Manual)": "#2E86C1", "Prediksi ML": "#E67E22"})
            
            # Merapikan tampilan teks angka pada grafik
            fig.update_traces(texttemplate='%{text:,.0f}', textposition='top left')
            fig.update_layout(xaxis_title="Tahun", yaxis_title="Total Tonase", template="plotly_white")
            
            st.plotly_chart(fig, use_container_width=True)

    # ==========================================
    # TAB 2: UNGGAH CSV (Fitur Sebelumnya)
    # ==========================================
    with tab2:
        st.subheader("Unggah Dataset Kompleks")
        uploaded_file = st.file_uploader("Unggah File Dataset (Format .csv)", type=["csv"], key="file_csv")
        
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                st.success("Dataset berhasil dimuat!")
                st.dataframe(df.head())

                if 'Tahun' not in df.columns:
                    st.error("Error: Dataset harus memiliki kolom bernama 'Tahun'.")
                else:
                    df_cleaned = df.fillna(df.mean(numeric_only=True))
                    kolom_metrik = [col for col in df_cleaned.columns if col != 'Tahun']
                    target_col = st.selectbox("Pilih Metrik yang Ingin Diprediksi:", kolom_metrik)
                    
                    tahun_pred_csv = st.slider("Prediksi Berapa Tahun ke Depan? (CSV)", min_value=1, max_value=20, value=5, key="slider_csv")

                    if st.button("Jalankan Prediksi AI (Data CSV)"):
                        from sklearn.linear_model import LinearRegression
                        from sklearn.preprocessing import MinMaxScaler
                        
                        X = df_cleaned[['Tahun']].values
                        y = df_cleaned[[target_col]].values

                        scaler_X = MinMaxScaler()
                        scaler_y = MinMaxScaler()

                        X_scaled = scaler_X.fit_transform(X)
                        y_scaled = scaler_y.fit_transform(y)

                        model = LinearRegression()
                        model.fit(X_scaled, y_scaled)

                        tahun_terakhir_csv = int(df_cleaned['Tahun'].max())
                        X_depan_csv = np.array([[tahun_terakhir_csv + i] for i in range(1, tahun_pred_csv + 1)])
                        X_depan_scaled = scaler_X.transform(X_depan_csv)
                        
                        prediksi_scaled = model.predict(X_depan_scaled)
                        prediksi_asli = scaler_y.inverse_transform(prediksi_scaled)

                        df_hist_csv = pd.DataFrame({'Tahun': df_cleaned['Tahun'], 'Nilai': df_cleaned[target_col], 'Keterangan': 'Historis'})
                        df_pred_csv = pd.DataFrame({'Tahun': X_depan_csv.flatten(), 'Nilai': prediksi_asli.flatten(), 'Keterangan': 'Prediksi ML'})
                        
                        df_gabung_csv = pd.concat([df_hist_csv, df_pred_csv])

                        fig2 = px.line(df_gabung_csv, x='Tahun', y='Nilai', color='Keterangan', 
                                      markers=True, title=f"Proyeksi {target_col}",
                                      color_discrete_map={"Historis": "blue", "Prediksi ML": "orange"})
                        
                        fig2.update_layout(xaxis_title="Tahun", yaxis_title=target_col, template="plotly_white")
                        st.plotly_chart(fig2, use_container_width=True)

            except Exception as e:
                st.error(f"Terjadi kesalahan saat memproses CSV. Detail: {e}")

# --- FOOTER ---
st.markdown("---")
st.caption("Dikembangkan berdasarkan Opini Ilmiah: Hilirisasi Kelapa; SCH-Hub; Rantai Pasok Terintegrasi; Sulawesi Barat.")
