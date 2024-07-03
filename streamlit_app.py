import streamlit as st
import pandas as pd

# Judul aplikasi
st.title('Infografis Interaktif Desa Pardomuan')

# Data Geografi
st.header('Geografi Kecamatan Sitellu Tali Urang Julu')
st.write('Luas kecamatan: 53,20 km²')

data_luas = {
    'Desa': ['Silima Kuta', 'Ulu Merah', 'Pardomuan', 'Lae Langge Namuseng', 'Cikaok'],
    'Luas (%)': [16.8, 40.2, 19.6, 13.7, 9.7]
}
df_luas = pd.DataFrame(data_luas)
st.write('Luas Area Menurut Desa (%)')
st.bar_chart(df_luas.set_index('Desa'))

# Jarak ke Ibukota Kecamatan
st.header('Jarak ke Ibukota Kecamatan Menurut Desa/Kelurahan')
data_jarak = {
    'Desa': ['Silima Kuta', 'Ulu Merah', 'Pardomuan', 'Lae Langge Namuseng', 'Cikaok'],
    'Jarak (km)': [3, 0, 5, 3, 5]
}
df_jarak = pd.DataFrame(data_jarak)
st.write('Jarak (km)')
st.bar_chart(df_jarak.set_index('Desa'))

# Nama Dusun Menurut Desa
st.header('Nama Dusun Menurut Desa')
data_dusun = {
    'Silima Kuta': ['Dusun I Kuta Kersik', 'Dusun II Kuta Kersik', 'Dusun I Singgabur', 'Dusun II Singgabur'],
    'Ulu Merah': ['Dusun I Ulu Merah', 'Dusun II Ulu Merah', 'Dusun III Maneas'],
    'Pardomuan': ['Dusun I Pardomuan', 'Dusun II Pardomuan', 'Dusun III Lae Mbulan'],
    'Lae Langge Namuseng': ['Dusun I Lae Langge', 'Dusun II Namuseng', 'Dusun III Lae Rambung', 'Dusun IV Lae Bunga'],
    'Cikaok': ['Dusun I Cikaok', 'Dusun II Lebbuh', 'Dusun III Sosor', 'Dusun IV Persabahen']
}

for desa, dusun in data_dusun.items():
    st.subheader(desa)
    for d in dusun:
        st.write(d)
