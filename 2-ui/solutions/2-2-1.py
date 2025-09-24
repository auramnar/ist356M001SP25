import streamlit as st

st.title("Area and Perimeter .")
length = st.number_input("Enter the length")
width = st.number_input("Enter the width")
btn_clicked = st.button("Calculate")



if btn_clicked:
    area = length * width
    perimeter = 2 * (length + width)
    st.write(f"Area: {area}")
    st.write(f"Perimeter: {perimeter}")



# Notes 

import streamlit as st

st.title("Saying Hello.")
name = st.text_input("And you are?")

if name:
    st.write(f"Hello, {name}!")
else:
    st.write("Enter a name")


If I was to write ... st.write(f'Name is {name}')
