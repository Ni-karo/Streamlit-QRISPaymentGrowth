import streamlit as st
import pandas as pd
import altair as alt

# konfigurasi halaman
st.set_page_config(
    page_title="Perkembangan Pengguna QRIS di Indonesia",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)

"""
# Perkembangan Pengguna QRIS di Indonesia

Analisis pertumbuhan pengguna QRIS berdasarkan kelompok usia (data diambil tahun 2025)
[Jelajahi set data kami!](https://github.com/Ni-karo/Streamlit-QRISPaymentGrowth/blob/main/QrisPayment.csv)
"""
"""
## Ringkasan
"""
cols = st.columns(4, gap="medium")
with cols[0].container(border=False, height="stretch"):
    html_content = """
    <div style="
        background-color: rgba(179, 191, 255, 0.5);
        padding: 15px; 
        border-radius: 5px;
        height: 140px;
    ">
        <h2 style="margin: 0; padding: 0;">85.3%</h2>
        <p style="font-size: medium; margin: 0; padding: 0;">pengguna QRIS termasuk dalam kelompok usia Gen Z.</p>
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

with cols[1].container(border=False, height="stretch"):
    html_content = """
    <div style="
        background-color: rgba(179, 191, 255, 0.5);
        padding: 15px; 
        border-radius: 5px;
        height: 140px;
    ">
        <h2 style="margin: 0; padding: 0;">75.8%</h2>
        <p style="font-size: medium; margin: 0; padding: 0;">menggunakan QRIS karena kemudahan dan kecepatan.</p>
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

with cols[2].container(border=False, height="stretch"):
    html_content = """
    <div style="
        background-color: rgba(179, 191, 255, 0.5);
        padding: 15px; 
        border-radius: 5px;
        height: 140px;
    ">
        <h2 style="margin: 0; padding: 0;">56.3%</h2>
        <p style="font-size: medium; margin: 0; padding: 0;">pengguna QRIS melaporkan keterbatasan penerimaan pedagang sebagai tantangan.</p>
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

with cols[3].container(border=False, height="stretch"):
    html_content = """
    <div style="
        background-color: rgba(179, 191, 255, 0.5);
        padding: 15px; 
        border-radius: 5px;
        height: 140px;
    ">
        <h2 style="margin: 0; padding: 0;">42%</h2>
        <p style="font-size: medium; margin: 0; padding: 0;">melaporkan keamanan sebagai kekhawatiran utama yang mencegah penggunaan QRIS.</p>
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

"""
## Statistik
"""
# dataset
csv_path = "https://raw.githubusercontent.com/Ni-karo/Streamlit-QRISPaymentGrowth/refs/heads/main/QrisPayment.csv"

@st.cache_data
def load_csv(path):
    return pd.read_csv(path, encoding='utf-8')

df = load_csv(csv_path)
if df.empty:
    st.error("Gagal memuat dataset dari URL. Cek koneksi atau URL.")
    st.stop()

# parameter
query_params = st.query_params

# prefill tickers
prefilled = []
if "usia" in query_params:
    prefilled_raw = query_params.get("usia")
    if isinstance(prefilled_raw, list):
        prefilled_raw = prefilled_raw[0]
    prefilled = [t.strip().upper() for t in prefilled_raw.split(",") if t.strip()]

## tickers
available_tickers = sorted(df["Kelompok_Usia"].astype(str).unique())

def update_query_params():
    """Update the URL query params whenever selection changes."""
    selected = st.session_state.get("selected_tickers", [])
    query_params.clear()
    if selected:
        query_params["usia"] = ",".join(selected)

# row 1
cols = st.columns([1,1,3])

top_left_cell = cols[0].container(border=True, height="stretch")
with top_left_cell:
    "#### Filter"
    
    selected = st.multiselect(
        "Pilih Kelompok Usia:",
        options=available_tickers,
        default=available_tickers,
        key="selected_tickers",
        help="Hanya pilihan tersedia dari dataset yang dapat dipilih.",
        on_change=update_query_params
)
    
with top_left_cell:
    """
    * Gen Z (Lahir 1997 - 2012)
    * Gen Y (Milenial, lahir 1981 - 1996)
    * Gen X (Lahir 1965 - 1980)
    """
    
if not selected:
    top_left_cell.info("Pilih kelompok usia untuk dibandingkan", icon=":material/info:")
    st.stop()

# filter data
filtered = df[df["Kelompok_Usia"].isin(selected)].copy()

if filtered.empty:
    st.warning("Tidak ada baris yang cocok ditemukan dalam CSV untuk ticker yang dipilih.")
    st.stop()

# hitungan series
count_series = filtered['Kelompok_Usia'].value_counts()
df_count = count_series.reset_index()
df_count.columns = ['Kelompok_Usia', 'Jumlah_Responden']
    
# pie chart
with cols[1].container(border=True, height="stretch"):
    chart_donut = (
    alt.Chart(df_count)
    .mark_arc(innerRadius=40)
    .encode(
        theta=alt.Theta(field="Jumlah_Responden", type="quantitative", stack=True), 
        color=alt.Color(field="Kelompok_Usia", type="nominal"),
        tooltip=["Kelompok_Usia", "Jumlah_Responden"]
    )
    .properties(title="Jumlah pengguna QRIS")
    .configure_legend(orient="bottom")
)
    
    st.altair_chart(chart_donut, use_container_width=True)
    
# stacked bar chart
df_grouped = filtered.groupby(['Metode_pembayaran', 'Kelompok_Usia']).size().reset_index(name='Total_Users')
with cols[2].container(border=True, height="stretch"):
    chart_stacked = (
        alt.Chart(df_grouped)
        .mark_bar()
        .encode(
            x=alt.X('Metode_pembayaran:N', 
                    title='Metode Pembayaran',
                    axis=alt.Axis(labelAngle=0)
                   ),
            y=alt.Y('Total_Users:Q', title='Jumlah Pengguna'),
            color=alt.Color('Kelompok_Usia:N', title='Kelompok Usia'),
            tooltip=['Metode_pembayaran', 'Kelompok_Usia', 'Total_Users']
        )
        .properties(title="Metode Pembayaran vs. Kelompok Usia")
        # bisa tambahkan .interactive() memungkinkan zoom dan pan
    )

    
    st.altair_chart(chart_stacked, use_container_width=True)

# row 2
"""
## Motivasi, Hambatan, dan Persepsi Pengguna terhadap QRIS
"""

cols = st.columns(2, gap="medium")
# bar 1
with cols[0].container(border=True, height="stretch"):
# Kategori yang diminta
    allowed_reasons = ['Praktis-Cepat', 'Masalah-teknis', 'Other', 'Tidak-ada-e-wallet', 'Merchant-Meneri']
    
    # Agregasi terfilter
    df_reasons = filtered[filtered['Alasan_Menggunakan'].isin(allowed_reasons)]
    df_reasons = df_reasons['Alasan_Menggunakan'].value_counts().reset_index()
    df_reasons.columns = ['Alasan', 'Jumlah_Responden']
    
    # Altair Chart
    chart_reasons = (
        alt.Chart(df_reasons)
        .mark_bar()
        .encode(
            x=alt.X('Alasan:N', title='Alasan Menggunakan QRIS', 
                    sort='-y', # Urutkan X berdasarkan Y (jumlah terbanyak di kiri)
                    axis=alt.Axis(labelAngle=0)),
            y=alt.Y('Jumlah_Responden:Q', title='Jumlah Pengguna'), 
            tooltip=['Alasan', 'Jumlah_Responden']
        )
        .properties(title="Alasan utama responden memilih QRIS")
    )
    st.altair_chart(chart_reasons, use_container_width=True)
  
# bar 2  
with cols[1].container(border=True, height="stretch"):
    # Agregasi
    df_kendala = filtered['Kendala_Qris'].value_counts().reset_index()
    df_kendala.columns = ['Kendala', 'Jumlah_Responden']
    
    # Altair Chart
    chart_kendala = (
        alt.Chart(df_kendala)
        .mark_bar()
        .encode(
            x=alt.X('Kendala:N', title='Kendala Menggunakan QRIS', axis=alt.Axis(labelAngle=0)),
            y=alt.Y('Jumlah_Responden:Q', title='Jumlah Pengguna', sort='-y'),
            tooltip=['Kendala', 'Jumlah_Responden']
        )
        .properties(title="Laporan kesulitan pengguna QRIS")
    )
    st.altair_chart(chart_kendala, use_container_width=True)
   
 
cols = st.columns(2, gap="medium")
# heatmap
with cols[0].container(border=True, height="stretch"):
# Agregasi
    df_heatmap = filtered.groupby(['Kelompok_Usia', 'Tingkat_Efisiensi_QRIS']).size().reset_index(name='Frekuensi')
    df_heatmap['Tingkat_Efisiensi_QRIS'] = df_heatmap['Tingkat_Efisiensi_QRIS'].astype(str)

    # Altair Chart
    chart_heatmap = (
        alt.Chart(df_heatmap)
        .mark_rect()
        .encode(
            x=alt.X('Kelompok_Usia:N', title="Kelompok Usia", axis=alt.Axis(labelAngle=0)),
            y=alt.Y('Tingkat_Efisiensi_QRIS:N', 
                    title="Efisiensi Rate",
                    sort=list(map(str, sorted(df_heatmap['Tingkat_Efisiensi_QRIS'].unique(), reverse=True)))
                   ), 
            color=alt.Color('Frekuensi:Q', title="Jumlah Responden"),
            tooltip=['Kelompok_Usia', 'Tingkat_Efisiensi_QRIS', 'Frekuensi']
        )
        .properties(title="Frekuensi Pemberian Rating Efisiensi QRIS", height=400)
    )
    st.altair_chart(chart_heatmap, use_container_width=True)

# table 
with cols[1].container(border=True, height="stretch"):
    st.dataframe(filtered, use_container_width=True, height=350)
    @st.cache_data
    def convert_df_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')

    csv_data = convert_df_to_csv(filtered)
    
    # Tombol Download
    st.download_button(
        label="⬇️ Unduh Dataset (CSV)",
        data=csv_data,
        file_name='data_persepsi_qris_filtered.csv',
        mime='text/csv',
    )
    

    # run: python -m streamlit run qrisapp.py


