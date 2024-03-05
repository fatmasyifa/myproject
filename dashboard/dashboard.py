import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Analisis Kualitas Udara di Aotizhongxin")
# Read data
df = pd.read_csv('./data/PRSA_Data_Aotizhongxin_20130301-20170228.csv')
st.title('Dashboard Analisis Kualitas Udara di Aotizhongxin')
st.write('Dashboard ini merupakan media untuk menyampaikan hasil analisis data kualitas udara di Aotizhongxin secara interaktif yang berfokus pada tingkat PM2.5 dan hubungannya dengan berbagai macam kondisi cuaca.')
st.markdown("""
- **Name**: Fatimah Fatma Syifa
- **Email**: fatmasyifa32@gmail.com
- **Dicoding ID**: fatmasyifa

Dashboard ini menunjukkan analisis data kualitas udara yang berfokus pada tingkat PM2.5 dari Aotizhongxin yang bertujuan untuk mengungkap kecenderungan, variasi per musim, dan kualitas udara yang diakibatkan perbedaan kondisi cuaca. Analisis ini berguna untuk studi lingkungan dan memantau kesehatan masyarakat.
""")

# Missing data analysis
st.title("Missing Data Analysis")
cols_to_plot = ['PM2.5', 'PM10']
data_missing = df[cols_to_plot].isnull()
data_missing['year'] = df['year']
data_missing_2013 = data_missing[data_missing['year'] == 2013]
st.pyplot(sns.heatmap(data_missing_2013.drop('year', axis=1).T, cmap='viridis', cbar=False))


# Time series analysis
st.title("Time Series Analysis")
data_imputed = df.fillna(method='ffill')
data_imputed['date'] = pd.to_datetime(data_imputed[['year', 'month', 'day', 'hour']])
data_time_series = data_imputed[['date', 'PM2.5', 'NO2']].set_index('date').resample('M').mean()
st.line_chart(data_time_series)


# Plot Seasonal Trends
seasonal_trends = data_imputed.groupby('month')['PM2.5'].mean()
st.bar_chart(seasonal_trends)


# Summary Statistics
st.title("Summary Statistics")
summary_statistics = data_imputed.describe()
st.write(summary_statistics)


# Correlation Matrix
st.title("Correlation Matrix")
correlation_matrix = data_imputed[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']].corr()
st.write(correlation_matrix)
