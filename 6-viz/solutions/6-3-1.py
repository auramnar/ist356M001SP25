'''
Load in the `final_cuse_parking_violations.csv` in the `data` folder and create a map of the parking violations in Syracuse.

- drop rows without a latitude and longitude
- provide a dropdown to select the status of the violation
- place pins on the map with the street name and the violation description
- color code the pins based on day of the week 
- to make the map more readable take a random sample of 50 rows from the dataframe



'''

import pandas as pd
import streamlit as st
import folium
import streamlit_folium as sf


days  = {
    'Sunday': 'red',
    'Monday': 'orange',
    'Tuesday': 'beige',
    'Wednesday': 'green',
    'Thursday': 'blue',
    'Friday': 'purple',
    'Saturday': 'gray'
}

st.title('Streamlit Park magic')

map = folium.Map(location=[43.0481, -76.1474], zoom_start=15)
df = pd.read_csv('./6-viz/data/final_cuse_parking_violations.csv')
df_dropped = df.dropna()
status = df_dropped['status'].unique()

status = st.selectbox('Select ticket status: ', status)

df_filtered = df_dropped[df_dropped['status'] == status]

df_sample = df_filtered.sample(50)

for i, row in df_sample.iterrows():
    lat, lon = row['coords'].strip("(").strip(")").split(',') # a string, remove parens, and seperate into lon and lat
    lat = float(lat.replace("'", "")) # remove quotes
    lon = float(lon.replace("'", "")) # convert to float 
    color = days[row['dayofweek']] # add color from dictionary
    folium.Marker((lat, lon), popup=row['location'], tooltip=row['location'], icon=folium.Icon(color=color)).add_to(map) # add markers


sf.folium_static(map)
