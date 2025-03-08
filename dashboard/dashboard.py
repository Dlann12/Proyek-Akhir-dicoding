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

# Mapping weather situation
weather_mapping = {
    1: "Clear/Few Clouds",
    2: "Mist/Cloudy",
    3: "Light Snow/Rain",
    4: "Heavy Rain/Snow",
}
datahour_df["weather_name"] = datahour_df["weathersit"].map(weather_mapping)

# Sidebar filter for weather
selected_weather = st.sidebar.selectbox(
    "Pilih Kondisi Cuaca:", 
    datahour_df["weather_name"].unique()
)

# Filter data based on selected weather
filtered_data = datahour_df[datahour_df["weather_name"] == selected_weather]

# Total count per season (after filtering)
season_count = filtered_data.groupby("season_name")["cnt"].sum().reset_index()
fig_season = px.pie(
    season_count,
    values="cnt",
    names="season_name",
    title=f"Distribusi Pengguna Berdasarkan Musim ({selected_weather})",
)

# Total count per hour (after filtering)
hourly_count = filtered_data.groupby("hr")["cnt"].sum().reset_index()
fig_hour = px.line(
    hourly_count,
    x="hr",
    y="cnt",
    markers=True,
    title=f"Peminjaman Sepeda Berdasarkan Jam ({selected_weather})",
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
    f"1. Musim dengan persentase pengguna tertinggi saat {selected_weather} adalah {season_count.sort_values('cnt', ascending=False).iloc[0]['season_name']}."
)
st.write(
    "2. Waktu dengan peminjaman tertinggi tetap berada di sekitar pukul 07:00 - 09:00 pagi dan 17:00 - 19:00 sore."
)

# Watermark & Profile Picture
st.sidebar.markdown("### Pembuat: Fadlan Dwi Febrio")
profile_pic = Image.open("pp.png")
st.sidebar.image(profile_pic, caption="MC189D5Y1615", width=150)
st.sidebar.write("Email: mc189d5y1615@student.devacademy.id")
