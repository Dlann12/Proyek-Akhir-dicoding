import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

# Load data
dataday_df = pd.read_csv("data/day.csv")
datahour_df = pd.read_csv("data/hour.csv")

# Convert date column
dataday_df["dteday"] = pd.to_datetime(dataday_df["dteday"])
datahour_df["dteday"] = pd.to_datetime(datahour_df["dteday"])

# Mapping season names
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
datahour_df["season_name"] = datahour_df["season"].map(season_mapping)

# Total count per season
season_count = datahour_df.groupby("season_name")["cnt"].sum().reset_index()
fig_season = px.pie(
    season_count,
    values="cnt",
    names="season_name",
    title="Distribusi Pengguna Berdasarkan Musim",
)

# Total count per hour
hourly_count = datahour_df.groupby("hr")["cnt"].sum().reset_index()
fig_hour = px.line(
    hourly_count,
    x="hr",
    y="cnt",
    markers=True,
    title="Peminjaman Sepeda Berdasarkan Jam",
)

# Streamlit App
st.title("Dashboard Bike Sharing")
st.subheader("Analisis Data Bike Sharing")

st.header("Kapan musim dengan persentase user tertinggi?")
st.plotly_chart(fig_season)

st.header("Kapan waktu/jam peminjaman sepeda mencapai angka tertinggi?")
st.plotly_chart(fig_hour)

st.header("Kesimpulan")
st.write(
    "1. Musim dengan persentase pengguna tertinggi adalah Fall (Musim Gugur), kemungkinan karena cuaca yang lebih nyaman."
)
st.write(
    "2. Waktu dengan peminjaman tertinggi adalah pukul 07:00 - 09:00 pagi dan 17:00 - 19:00 sore, menunjukkan pola penggunaan untuk perjalanan kerja atau sekolah."
)

# Watermark & Profile Picture
st.sidebar.image("1111.jpg", use_container_width=True)
st.sidebar.title(
    "Proyek Akhir Belajar Analisis Data dengan Python: Analisis Bike Sharing")
st.sidebar.write("Nama: Arief Setiawan")
st.sidebar.write(
    "Email: [mc189d5y1641@student.devacademy.id](mailto:mc189d5y1641@student.devacademy.id)")
st.sidebar.write("Id Dicoding: MC189D5Y1641")
