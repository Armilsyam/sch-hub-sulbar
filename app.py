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
menu = st.sidebar.radio("Pilih Halaman:", ["Latar Belakang & Analisis", "Konsep SCH-Hub", "Prediksi & Proyeksi Ekonomi", "Buku Saku (FAQ)"])

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

# --- HALAMAN 3: PREDIKSI MASA DEPAN (MACHINE LEARNING) ---
elif menu == "Prediksi & Proyeksi Ekonomi":
    st.header("📈 Prediksi Berbasis Machine Learning")
    st.write("Gunakan data historis untuk memprediksi tren produksi komoditas kelapa di masa depan.")

    st.markdown("---")
    st.subheader("⚙️ Pengaturan Model AI")
    pilihan_algoritma = st.selectbox(
        "Pilih Algoritma Prediksi:",
        [
            "1. Linear Regression (Garis lurus, cocok untuk tren stabil & data terbatas)",
            "2. Polynomial Regression (Melengkung, cocok untuk tren eksponensial/akselerasi)",
            "3. Random Forest Regressor (Decision Tree, cocok untuk CSV dengan banyak variabel)"
        ]
    )
    st.markdown("---")

    # Fungsi khusus untuk menghasilkan teks interpretasi otomatis
    def buat_interpretasi(nilai_awal, nilai_akhir, tahun_awal, tahun_akhir, nama_metrik, nama_model):
        selisih = nilai_akhir - nilai_awal
        persentase = (selisih / nilai_awal) * 100
        
        st.write("### 🤖 Interpretasi Hasil Prediksi")
        
        # Logika Kondisional berdasarkan tren
        if persentase > 5:
            st.success(f"**Tren Positif (Naik {persentase:.2f}%):** Berdasarkan model **{nama_model}**, {nama_metrik} diproyeksikan mengalami **peningkatan** sebesar **{selisih:,.0f}** dari tahun {tahun_awal} ({nilai_awal:,.0f}) ke tahun {tahun_akhir} ({nilai_akhir:,.0f}).")
            st.write("💡 **Insight Bisnis:** Tren pasokan yang naik ini sangat mendukung kelayakan investasi pembangunan pabrik SCH-Hub. Ketersediaan bahan baku diproyeksikan aman untuk memenuhi kapasitas produksi hilirisasi.")
        elif persentase < -5:
            st.error(f"**Tren Negatif (Turun {abs(persentase):.2f}%):** Berdasarkan model **{nama_model}**, {nama_metrik} diproyeksikan mengalami **penurunan** sebesar **{abs(selisih):,.0f}** dari tahun {tahun_awal} ({nilai_awal:,.0f}) ke tahun {tahun_akhir} ({nilai_akhir:,.0f}).")
            st.write("⚠️ **Rekomendasi Kebijakan:** Waspada ancaman kelangkaan bahan baku! Pemerintah daerah harus segera mengaktifkan pilar **'Inovasi Produksi (Smart Farming)'** dan peremajaan pohon kelapa untuk membalikkan tren ini sebelum klaster industri beroperasi.")
        else:
            st.warning(f"**Tren Stagnan (Berubah {persentase:.2f}%):** Berdasarkan model **{nama_model}**, {nama_metrik} diproyeksikan cenderung **stagnan/stabil** dari tahun {tahun_awal} ke tahun {tahun_akhir}.")
            st.write("🔍 **Insight Bisnis:** Pasokan relatif aman namun tidak tumbuh signifikan. Untuk menopang target lonjakan nilai tambah ekonomi 1500%, intensifikasi pertanian wajib dilakukan agar produktivitas per hektar meningkat.")

    tab1, tab2 = st.tabs(["✍️ Input Manual (5 Tahun Terakhir)", "📁 Unggah File CSV"])

    # ==========================================
    # TAB 1: INPUT MANUAL
    # ==========================================
    with tab1:
        st.subheader("Input Data Tonase Produksi (2021 - 2025)")
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
            from sklearn.preprocessing import PolynomialFeatures
            from sklearn.pipeline import make_pipeline
            from sklearn.ensemble import RandomForestRegressor
            
            tahun_historis = [2021, 2022, 2023, 2024, 2025]
            data_tonase = [ton_2021, ton_2022, ton_2023, ton_2024, ton_2025]
            
            df_historis = pd.DataFrame({'Tahun': tahun_historis, 'Produksi (Ton)': data_tonase, 'Keterangan': 'Historis (Input Manual)'})
            X = df_historis[['Tahun']].values
            y = df_historis['Produksi (Ton)'].values 

            nama_model_terpilih = pilihan_algoritma.split('(')[0].strip()

            if "Linear Regression" in pilihan_algoritma:
                model = LinearRegression()
            elif "Polynomial Regression" in pilihan_algoritma:
                model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
            elif "Random Forest" in pilihan_algoritma:
                model = RandomForestRegressor(n_estimators=100, random_state=42)

            model.fit(X, y)

            tahun_terakhir = 2025
            X_masa_depan = np.array([[tahun_terakhir + i] for i in range(1, tahun_prediksi_manual + 1)])
            prediksi_masa_depan = model.predict(X_masa_depan)

            df_prediksi = pd.DataFrame({'Tahun': X_masa_depan.flatten(), 'Produksi (Ton)': prediksi_masa_depan.flatten(), 'Keterangan': 'Prediksi ML'})
            df_gabungan = pd.concat([df_historis, df_prediksi])

            st.markdown("---")
            st.subheader(f"📊 Proyeksi Produksi (Model: {nama_model_terpilih})")
            
            if "Random Forest" in pilihan_algoritma:
                st.warning("⚠️ **Karakteristik Random Forest:** Pada data 1 Dimensi (hanya Tahun & Tonase), hasilnya akan terlihat mendatar (flat). Model ini optimal untuk CSV dengan banyak variabel pendukung.")

            fig = px.line(df_gabungan, x='Tahun', y='Produksi (Ton)', color='Keterangan', 
                          markers=True, text='Produksi (Ton)',
                          color_discrete_map={"Historis (Input Manual)": "#2E86C1", "Prediksi ML": "#E67E22"})
            
            fig.update_traces(texttemplate='%{text:,.0f}', textposition='top left')
            fig.update_layout(xaxis_title="Tahun", yaxis_title="Total Tonase", template="plotly_white")
            st.plotly_chart(fig, use_container_width=True)

            # MEMANGGIL FUNGSI INTERPRETASI OTOMATIS
            nilai_akhir_historis = df_historis['Produksi (Ton)'].iloc[-1]
            nilai_akhir_prediksi = df_prediksi['Produksi (Ton)'].iloc[-1]
            tahun_akhir_prediksi = df_prediksi['Tahun'].iloc[-1]
            
            buat_interpretasi(nilai_akhir_historis, nilai_akhir_prediksi, tahun_terakhir, tahun_akhir_prediksi, "Produksi Kelapa (Ton)", nama_model_terpilih)

    # ==========================================
    # TAB 2: UNGGAH CSV
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
                    target_col = st.selectbox("Pilih Metrik yang Ingin Diprediksi (Target / y):", kolom_metrik)
                    fitur_pendukung = st.multiselect("Pilih Variabel Pendukung (Opsional):", [c for c in kolom_metrik if c != target_col])
                    tahun_pred_csv = st.slider("Prediksi Berapa Tahun ke Depan? (CSV)", min_value=1, max_value=20, value=5, key="slider_csv")

                    if st.button("Jalankan Prediksi AI (Data CSV)"):
                        from sklearn.linear_model import LinearRegression
                        from sklearn.preprocessing import PolynomialFeatures, MinMaxScaler
                        from sklearn.pipeline import make_pipeline
                        from sklearn.ensemble import RandomForestRegressor
                        
                        kolom_X = ['Tahun'] + fitur_pendukung
                        X = df_cleaned[kolom_X].values
                        y = df_cleaned[target_col].values

                        scaler_X = MinMaxScaler()
                        X_scaled = scaler_X.fit_transform(X)
                        nama_model_terpilih = pilihan_algoritma.split('(')[0].strip()

                        if "Linear Regression" in pilihan_algoritma:
                            model = LinearRegression()
                        elif "Polynomial Regression" in pilihan_algoritma:
                            model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
                        elif "Random Forest" in pilihan_algoritma:
                            model = RandomForestRegressor(n_estimators=100, random_state=42)

                        model.fit(X_scaled, y) 

                        tahun_terakhir_csv = int(df_cleaned['Tahun'].max())
                        X_depan_list = []
                        nilai_terakhir_pendukung = df_cleaned[fitur_pendukung].iloc[-1].values if fitur_pendukung else []
                        
                        for i in range(1, tahun_pred_csv + 1):
                            baris_baru = [tahun_terakhir_csv + i] + list(nilai_terakhir_pendukung)
                            X_depan_list.append(baris_baru)
                            
                        X_depan_csv = np.array(X_depan_list)
                        X_depan_scaled = scaler_X.transform(X_depan_csv)
                        prediksi_asli = model.predict(X_depan_scaled)

                        df_hist_csv = pd.DataFrame({'Tahun': df_cleaned['Tahun'], 'Nilai': df_cleaned[target_col], 'Keterangan': 'Historis'})
                        df_pred_csv = pd.DataFrame({'Tahun': X_depan_csv[:, 0], 'Nilai': prediksi_asli, 'Keterangan': 'Prediksi ML'})
                        df_gabung_csv = pd.concat([df_hist_csv, df_pred_csv])

                        st.markdown("---")
                        st.subheader(f"📊 Proyeksi {target_col} (Model: {nama_model_terpilih})")
                        fig2 = px.line(df_gabung_csv, x='Tahun', y='Nilai', color='Keterangan', 
                                      markers=True, text='Nilai',
                                      color_discrete_map={"Historis": "blue", "Prediksi ML": "orange"})
                        
                        fig2.update_traces(texttemplate='%{text:,.0f}', textposition='top left')
                        fig2.update_layout(xaxis_title="Tahun", yaxis_title=target_col, template="plotly_white")
                        st.plotly_chart(fig2, use_container_width=True)

                        # MEMANGGIL FUNGSI INTERPRETASI OTOMATIS
                        nilai_akhir_historis = df_hist_csv['Nilai'].iloc[-1]
                        nilai_akhir_prediksi = df_pred_csv['Nilai'].iloc[-1]
                        tahun_akhir_prediksi = df_pred_csv['Tahun'].iloc[-1]
                        
                        buat_interpretasi(nilai_akhir_historis, nilai_akhir_prediksi, tahun_terakhir_csv, int(tahun_akhir_prediksi), target_col, nama_model_terpilih)

            except Exception as e:
                st.error(f"Terjadi kesalahan saat memproses CSV. Detail: {e}")
    # --- HALAMAN 4: BUKU SAKU (FAQ) ---
elif menu == "Buku Saku (FAQ)":
    st.header("📖 Buku Saku Interaktif SCH-Hub")
    st.write("Panduan tanya-jawab sederhana untuk memahami transformasi ekonomi komoditas kelapa di Sulawesi Barat. Klik pada pertanyaan untuk melihat jawaban.")
    st.markdown("---")

    with st.expander("🤔 1. Apa itu SCH-Hub secara sederhana?"):
        st.write("""
        **SCH-Hub (Strategic Coconut Hilirization Hub)** adalah sebuah ekosistem terpadu. Bayangkan ini sebagai sebuah kawasan pabrik pintar yang dilengkapi dengan aplikasi *smartphone*. 
        Tujuannya satu: Menghentikan kebiasaan lama menjual kelapa butiran mentah yang murah, dan menggantinya dengan mengolah kelapa tersebut menjadi berbagai produk mahal di dalam daerah sendiri.
        """)

    with st.expander("🌴 2. Kenapa harus Kelapa? Bukankah sudah ada Kelapa Sawit?"):
        st.write("""
        Perekonomian Sulawesi Barat saat ini sangat bergantung pada sawit (mencapai 91,49% dari industri pengolahan). Ini sangat berbahaya! Jika harga sawit dunia jatuh, ekonomi daerah ikut hancur. 
        
        Kelapa biasa (*Cocos nucifera*) dipilih karena Sulawesi Barat punya lahan kelapa terbesar ke-4 di regional Sulawesi. Ini adalah "harta karun" yang selama ini terabaikan. Kita butuh komoditas andalan kedua agar ekonomi lebih kuat dan stabil.
        """)

    with st.expander("♻️ 3. Apa maksud 'Ekonomi Sirkular' atau 'Zero Waste' di pabrik ini?"):
        st.write("""
        Biasanya, petani hanya mengambil daging kelapa (untuk kopra) dan membuang sisanya. Dalam ekonomi sirkular SCH-Hub, **TIDAK ADA SAMPAH YANG DIBUANG**.
        
        - **Daging Kelapa** diolah menjadi *Virgin Coconut Oil* (VCO) atau kelapa parut kering ekspor.
        - **Air Kelapa** diolah menjadi *Nata de Coco*.
        - **Tempurung (Batok)** dibakar menjadi Arang Aktif yang mahal untuk industri filter air/udara.
        - **Sabut Kelapa** diurai menjadi tali tambang atau media tanam (*cocopeat*).
        """)

    with st.expander("📱 4. Apa fungsi aplikasi SCH-APP bagi petani biasa?"):
        st.write("""
        SCH-APP memutus rantai "tengkulak" yang sering merugikan petani. Melalui aplikasi ini:
        
        1. Petani bisa melihat harga beli standar secara transparan.
        2. Petani bisa langsung menjual hasil panennya ke pabrik SCH-Hub terdekat tanpa perantara.
        3. Pabrik bisa memperkirakan kapan pasokan kelapa akan datang.
        4. Petani mendapat panduan cara merawat pohon (*smart farming*) agar buahnya lebih lebat.
        """)

    with st.expander("💰 5. Dari mana datangnya keuntungan hingga 1500% itu?"):
        st.write("""
        Itu disebut **Nilai Tambah (Hilirisasi)**. 
        
        Jika seorang petani menjual kelapa utuh ke luar provinsi, ia mungkin hanya dapat Rp 2.000 per butir. Namun, jika batok kelapa itu diolah menjadi "Arang Aktif" kelas ekspor, harga batok dari satu kelapa saja bisa bernilai belasan ribu rupiah.
        
        Dengan pabrik yang ada di dalam Sulawesi Barat, seluruh proses ini menciptakan lapangan kerja baru bagi warga lokal dan pajaknya masuk ke pemerintah daerah (mencegah *kebocoran ekonomi lokal*).
        """)

    st.info("💡 **Tips:** Bagikan halaman ini kepada pemangku kepentingan, investor, atau kelompok tani untuk memberikan pemahaman dasar sebelum melihat data analitik yang lebih rumit di halaman lain.")

# --- FOOTER ---
st.markdown("---")
st.caption("Dikembangkan berdasarkan Opini Ilmiah: Hilirisasi Kelapa; SCH-Hub; Rantai Pasok Terintegrasi; Sulawesi Barat.")
