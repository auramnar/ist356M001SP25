import random
import geopandas as gpd
import pandas as pd
import streamlit as st
import plotly.express as px
import streamlit_folium as sf
import folium

st.title('Streamlit Geopandas Examples')
st.caption('This is a simple example of how to use Streamlit to create visualizations with Geopandas')

# Load the GeoPandas data
st.write("## Saint Lucia Choropleth")
#read geospatial data about Saint Lucia from a GeoJSON file into a Geopandas GeoDataFrame named gdf
gdf = gpd.read_file("./6-viz/data/stlucia.geojson")
# create a new column named 'Amount'. For each row (representing a region in Saint Lucia), it assigns a random integer between 50 and 275
gdf['Amount'] = gdf.apply(lambda row: random.randint(50,275), axis=1)
st.write(gdf)
# choropleth map using the .explore() method leveraging Folium)
sf.folium_static(gdf.explore(gdf['Amount']))

# Syracuse Wards Choropleth
wards_df = gpd.read_file("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/city-of-syracuse/wards.geojson")
wards_df['amount'] = wards_df.apply(lambda row: random.randint(1,50), axis=1)

st.write('## City of Syracuse Wards - Choropleth')
st.write(wards_df)
sf.folium_static(wards_df.explore(wards_df['amount']))

stlucia_df = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/st-lucia/parishes.csv")
stlucia_df['Amount'] = stlucia_df.apply(lambda row: random.randint(50,500), axis=1)

# Class Schedule Map
st.write("# Folium - Class Schedule")
classesdf = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/master/delimited/class-schedule.csv")
gdf = gpd.GeoDataFrame(classesdf, geometry=gpd.points_from_xy(classesdf['Lon'], classesdf['Lat']))
st.write(gdf)
schine = (43.03986, -76.13375)
# Create a Folium map centered on Schine Student Center
m = folium.Map(location=schine, zoom_start=17)
#use the .explore() method , but this time to create a point map.
mout = gdf.explore(popup="Course",lat="Lat", lon="Lon", m=m, marker_type="marker")
sf.folium_static(mout)


st.write("# Mapbox - Plotly Express")
st.write('## Saint Lucia Parishes - Scatter')
# creates an interactive scatter map using Plotly Express
fig = px.scatter_mapbox(stlucia_df,  lat="Lat", lon="Lng", zoom=10, color = 'Parish', hover_name = 'Parish', size = 'Amount',  mapbox_style="open-street-map")
st.plotly_chart(fig)

st.write('## Saint Lucia Parishes - Density')
fig = px.density_mapbox(stlucia_df, lat='Lat', lon='Lng', z='Amount', radius=10, center=dict(lat=13.9, lon=-60.97), zoom=10, mapbox_style="open-street-map")
st.plotly_chart(fig)
