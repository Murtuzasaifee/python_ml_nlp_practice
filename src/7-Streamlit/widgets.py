import streamlit as st
import pandas as pd

st.title("Streamlit Text Input Example")

## Text Input
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}")
st.write("") ## Empty space as padding

## Slide
age = st.slider("How old are you?", 0, 100,25)
st.write(f"You are {age} years old.")
st.write("")

## Select Box
options =  ["Select option", "Option 1", "Option 2", "Option 3"]
select = st.selectbox("Choose option", options)
st.write(f"You selected {select}")
st.write("")

## Dataframe
df = pd.DataFrame({
    "Name": ["John", "Jane", "Doe"],
    "Age": [25, 30, 35]
})
df.to_csv("sample_data.csv")
st.write(df)

## File Uplaoder
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
