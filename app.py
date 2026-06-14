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

# --- HALAMAN 3: PREDIKSI MASA DEPAN ---
elif menu == "Prediksi & Proyeksi Ekonomi":
    st.header("📈 Prediksi Peningkatan Nilai Tambah (2025 - 2030)")
    st.write("Simulasi perbandingan pertumbuhan nilai ekonomi komoditas kelapa antara skenario *Business as Usual* (dijual mentah/kopra) dengan implementasi *SCH-Hub* (hilirisasi dengan lonjakan nilai tambah hingga **1500%**).")

    # Membuat Data Simulasi (Mock Data)
    tahun = np.arange(2025, 2031)
    
    # Skenario 1: Tanpa Hilirisasi (Pertumbuhan lambat 5% per tahun)
    nilai_awal = 100 # Indeks nilai awal (miliar Rupiah misalnya)
    skenario_mentah = [nilai_awal * (1.05 ** i) for i in range(len(tahun))]
    
    # Skenario 2: Dengan SCH-Hub (Lonjakan eksponensial menuju 1500% di tahun ke-5)
    # Mencapai ~15x lipat pada tahun 2030
    skenario_hilirisasi = [nilai_awal * (1 + (14 * (i / 5)**1.5)) for i in range(len(tahun))]

    df_prediksi = pd.DataFrame({
        "Tahun": tahun,
        "Penjualan Mentah/Kopra (BAU)": skenario_mentah,
        "Ekosistem SCH-Hub (Hilirisasi)": skenario_hilirisasi
    })

    # Plotly Chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_prediksi["Tahun"], y=df_prediksi["Penjualan Mentah/Kopra (BAU)"],
                             mode='lines+markers', name='Tanpa Hilirisasi (BAU)', line=dict(color='red', dash='dash')))
    fig.add_trace(go.Scatter(x=df_prediksi["Tahun"], y=df_prediksi["Ekosistem SCH-Hub (Hilirisasi)"],
                             mode='lines+markers', name='Dengan SCH-Hub (Hilirisasi)', line=dict(color='green', width=3)))

    fig.update_layout(title="Proyeksi Pertumbuhan Nilai Tambah Komoditas Kelapa Sulbar",
                      xaxis_title="Tahun",
                      yaxis_title="Indeks Nilai Ekonomi",
                      template="plotly_white")
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.success("📝 **Kesimpulan Prediksi:** Implementasi SCH-Hub tidak hanya menekan kebocoran ekonomi lokal (*local economic leakage*), tetapi juga menggeser kurva pertumbuhan secara radikal, menciptakan resiliensi daya saing ekonomi Sulawesi Barat secara inklusif dan berkelanjutan.")

# --- FOOTER ---
st.markdown("---")
st.caption("Dikembangkan berdasarkan Opini Ilmiah: Hilirisasi Kelapa; SCH-Hub; Rantai Pasok Terintegrasi; Sulawesi Barat.")
