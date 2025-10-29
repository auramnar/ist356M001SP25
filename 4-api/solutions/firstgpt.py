'''
FirstGPT


'''

import requests
import streamlit as st

def get_text_responses(query:str) -> str:
    '''
    Call Genai and return a response.
    '''
    url = "https://cent.ischool-iot.net/api/genai/generate"
    data = {"query": query}
    headers = {
        "X-API-KEY": "???",
    }
    response = requests.post(url, data =data, headers=headers)
    response.raise_for_status()
    return response.json()


st.title("FirstGPT")

text = st.text_input("Enter a text to get a response:")
if text:
    response = get_text_responses(text)
    st.write(response)





'''
'''
curl -X 'POST' \
  'https://cent.ischool-iot.net/api/genai/generate?model=llama3%3Alatest&temperature=0.7&max_tokens=1000' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: ????' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'query=%22What%20are%20your%20capabilities%3F%22'

'''


import requests
import streamlit as st


def get_text_completion(query: str)-> str:
    url = "https://cent.ischool-iot.net/api/genai/generate"
    data = {text: query}
    headers={'X-API-KEY': '????}
    response = requests.post(url, headers=headers, data=data)   
    response.raise_for_status()
    result = response.json()    
    return result


st.title("First GPT App")
text = st.text_area("Enter your prompt here:")
if text:
    with st.spinner("Generating response..."):
        response = get_text_completion(text)
        st.write(response)



'''
    
