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
