from fastapi import FastAPI, Query
import pandas as pd
import numpy as np
import json

'''
This FastAPI endpoint:

Loads flight data from GitHub.

Lets a user search for flights by departure or arrival airport code.

Returns the matching flights as JSON
'''


app = FastAPI()

#load data 

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/flights/sample-flights.csv"
df = pd.read_csv(url)

@ app.get("/api/search_flights") # route decorator the endpoint
# When someone visits that endpoint (e.g. http://localhost:8000/api/search_flights?...), the function below will run.
# endpoint function 
# type and code are the query parameters
def search_flights(type: str = Query(..., description="Type of search: 'dep' for departure, 'arr' for arrival"), 
                   code: str = Query(..., description="Airport code to search for")):
    if type == "dep":
        flights = df[df["departure_airport_code"] == code]
    elif type == "arr":
        flights = df[df["arrival_airport_code"] == code]
    else:
        return {} # empty dictionary
    # departure_airport_code
    # arrival_airport_code
    
    # json string
    
    json_flights = flights.to_json(orient="records") # turns into JSON string 
    return json.loads(json_flights) # convert the string in a list of dictionaries


