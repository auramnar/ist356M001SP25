'''
Let's write an LLM-based spellchecker!

The spellchecker should take some text as input and return the misspelled works along with suggestions for the correct spellings. 

Make the inputs, then create a suitable prompt for the LLM. 
#31


curl -X 'POST' \
  'https://cent.ischool-iot.net/api/genai/generate?model=llama3%3Alatest&temperature=2&max_tokens=1000' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: '????' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'query=how%20are%20you%20today'

'''

import requests
import streamlit as st
import json


# write a wrapper function to call the LLM API

def openai_api_call(prompt):
    url = "https://cent.ischool-iot.net/api/genai/generate"
    data = {
        "query": prompt
    }
    headers = {
        "X-API-KEY": "e4817f2223fc521129078fbf",
    }
    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()
    return response.json()

def spellcheck(text):
    prompt = " Spell check the following text:\n"
    prompt += text +"\n"
    prompt += "For each misspelled words provide suggestions for the correct spellings.\n"
    response = openai_api_call(prompt)
    st. write(response)
    
    

st.title("Spell Checker")
text = st.text_area("Enter text to check for spelling errors:")
response = spellcheck(text)
st.write(response)    
    
