from fastapi import FastAPI, Query
import pandas as pd
import numpy as np
import json

app = FastAPI()

#load data 

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/flights/sample-flights.csv"
df = pd.read_csv(url)

@ app.get("/api/search_flights")
def search_flights(type: str = Query(..., description="Type of search: 'dep' for departure, 'arr' for arrival"), 
                   code: str = Query(..., description="Airport code to search for")):
    if type == "dep":
        flights = df[df["departure_airport_code"] == code]
    elif type == "arr":
        flights = df[df["arrival_airport_code"] == code]
    else:
        return {}
    # departure_airport_code
    # arrival_airport_code
    
    # json string
    
    json_flights = flights.to_json(orient="records")
    return json.loads(json_flights)


