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
    st.write("Gunakan data historis untuk memprediksi tren produksi komoditas kelapa di masa depan.")

    st.markdown("---")
    st.subheader("⚙️ Pengaturan Model AI")
    # Menu Dropdown untuk memilih Algoritma
    pilihan_algoritma = st.selectbox(
        "Pilih Algoritma Prediksi:",
        [
            "1. Linear Regression (Garis lurus, cocok untuk tren stabil & data terbatas)",
            "2. Polynomial Regression (Melengkung, cocok untuk tren eksponensial/akselerasi)",
            "3. Random Forest Regressor (Decision Tree, cocok untuk CSV dengan banyak variabel)"
        ]
    )
    st.markdown("---")

    # Membuat dua tab: Input Manual dan Upload CSV
    tab1, tab2 = st.tabs(["✍️ Input Manual (5 Tahun Terakhir)", "📁 Unggah File CSV"])

    # ==========================================
    # TAB 1: INPUT MANUAL
    # ==========================================
    with tab1:
        st.subheader("Input Data Tonase Produksi (2021 - 2025)")
        st.write("Masukkan total produksi kelapa (dalam Ton) untuk 5 tahun terakhir pada kolom di bawah ini:")

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
            y = df_historis['Produksi (Ton)'].values # Menggunakan 1D array untuk y agar kompatibel dengan RF

            # Logika Pemilihan Model
            if "Linear Regression" in pilihan_algoritma:
                model = LinearRegression()
            elif "Polynomial Regression" in pilihan_algoritma:
                # Degree 2 membuat garis bisa melengkung 1 kali
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
            st.subheader(f"📊 Proyeksi Produksi (Model: {pilihan_algoritma.split('(')[0]})")
            
            # Peringatan Edukasi jika menggunakan RF pada data sedikit
            if "Random Forest" in pilihan_algoritma:
                st.warning("⚠️ **Karakteristik Random Forest:** Algoritma berbasis pohon tidak bisa menebak angka lebih tinggi dari batas maksimal data latihnya. Pada data 1 Dimensi (hanya Tahun & Tonase), hasilnya akan terlihat **mendatar (flat)**. Model ini baru akan bersinar jika Anda mengunggah CSV dengan banyak variabel (Luas Lahan, Cuaca, dll).")

            fig = px.line(df_gabungan, x='Tahun', y='Produksi (Ton)', color='Keterangan', 
                          markers=True, text='Produksi (Ton)',
                          color_discrete_map={"Historis (Input Manual)": "#2E86C1", "Prediksi ML": "#E67E22"})
            
            fig.update_traces(texttemplate='%{text:,.0f}', textposition='top left')
            fig.update_layout(xaxis_title="Tahun", yaxis_title="Total Tonase", template="plotly_white")
            st.plotly_chart(fig, use_container_width=True)

    # ==========================================
    # TAB 2: UNGGAH CSV
    # ==========================================
    with tab2:
        st.subheader("Unggah Dataset Kompleks")
        st.write("Unggah data dengan kolom `Tahun`, `Produksi_Ton`, `Luas_Lahan`, dll.")
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
                    
                    # Memilih fitur pendukung (X) jika ada lebih dari 2 kolom
                    fitur_pendukung = st.multiselect("Pilih Variabel Pendukung (Opsional, untuk Random Forest):", [c for c in kolom_metrik if c != target_col])
                    
                    tahun_pred_csv = st.slider("Prediksi Berapa Tahun ke Depan? (CSV)", min_value=1, max_value=20, value=5, key="slider_csv")

                    if st.button("Jalankan Prediksi AI (Data CSV)"):
                        from sklearn.linear_model import LinearRegression
                        from sklearn.preprocessing import PolynomialFeatures, MinMaxScaler
                        from sklearn.pipeline import make_pipeline
                        from sklearn.ensemble import RandomForestRegressor
                        
                        # Menyiapkan fitur X (Tahun + Variabel Pendukung jika ada)
                        kolom_X = ['Tahun'] + fitur_pendukung
                        X = df_cleaned[kolom_X].values
                        y = df_cleaned[target_col].values

                        scaler_X = MinMaxScaler()
                        X_scaled = scaler_X.fit_transform(X)

                        if "Linear Regression" in pilihan_algoritma:
                            model = LinearRegression()
                        elif "Polynomial Regression" in pilihan_algoritma:
                            model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
                        elif "Random Forest" in pilihan_algoritma:
                            model = RandomForestRegressor(n_estimators=100, random_state=42)

                        model.fit(X_scaled, y) # Melatih model (y tidak perlu discale agar mudah dibaca)

                        # Menyiapkan X masa depan
                        tahun_terakhir_csv = int(df_cleaned['Tahun'].max())
                        
                        # Jika ada fitur pendukung, kita asumsikan nilainya konstan (menggunakan nilai tahun terakhir)
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
                        st.subheader(f"📊 Proyeksi {target_col} (Model: {pilihan_algoritma.split('(')[0]})")
                        fig2 = px.line(df_gabung_csv, x='Tahun', y='Nilai', color='Keterangan', 
                                      markers=True, text='Nilai',
                                      color_discrete_map={"Historis": "blue", "Prediksi ML": "orange"})
                        
                        fig2.update_traces(texttemplate='%{text:,.0f}', textposition='top left')
                        fig2.update_layout(xaxis_title="Tahun", yaxis_title=target_col, template="plotly_white")
                        st.plotly_chart(fig2, use_container_width=True)

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
