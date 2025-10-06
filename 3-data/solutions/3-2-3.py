import requests
import pandas as pd
import streamlit as st

st.title("Excel to JSON")

uploaded_file = st.file_uploader("Upload an EXCEL file", type=["xlsx"])

if uploaded_file: # only execute if file successfully uploaded
    df = pd.read_excel(uploaded_file.getvalue()) # Get the values that panda can process
    st.dataframe(df)
    
    
    # Convert dataframe to JSON format
    json_file = df.to_json(orient="records", index=False) # exclude row labels
    # Extract filename and create a new JSON filename
    # orient="records": Specifies the JSON format to be a list of dictionaries, 
    #where each dictionary represents a row and uses column names as keys
    #index=False: Excludes the pandas DataFrame's index numbers
    json_filename = uploaded_file.name.split(".")[0] + ".json"
    # .split(".")[0]: Splits the name at the dot (.) and takes the first part (e.g., "data")
    download = st.download_button(f"Download {json_filename}", data=json_file, file_name=json_filename)
    # JSON file generated  user can download it via the st.download_button
    
