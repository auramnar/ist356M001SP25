import streamlit as st

# Initialize session state variables if they don't exist
#When the script runs for the very first time, the keys 'length' and 'width' will not exist in st.session_state. 
#This conditional check ensures they are initialized to 0. 
# This prevents errors later when inputs try to read their default value from the session state
# Initialize the session state

if 'length' not in st.session_state: #edit
    st.session_state.length = 0
if 'width' not in st.session_state: #edit
    st.session_state.width = 0

st.title("Area and Perimeter .") # Title of the app
# User inputs for length and width
# set their value directly from st.session_state.length and st.session_state.width. 
# This is how the app remembers the last entered values, especially after a "Clear" operation that triggers a rerun.
length = st.number_input("Enter the length", value = st.session_state.length) #edit default from session state
width = st.number_input("Enter the width", value = st.session_state.width) #edit

# Buttons for calculation and clearing
btn_clicked = st.button("Calculate")
btn_clear = st.button("Clear") # reset inputs and session state

# Calculation and output
if btn_clicked:
    area = length * width
    perimeter = 2 * (length + width)
    st.write(f"Area: {area}")
    st.write(f"Perimeter: {perimeter}")

   
# Clear button logic. Reset inputs and session state 
# set to None type to represent the absence of a value
if btn_clear:
    st.session_state.length = None
    st.session_state.width = None
    st.rerun()
