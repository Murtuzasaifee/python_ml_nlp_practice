import streamlit as st
import pandas as pd
import numpy as np

## Title of application
st.title('Hello World!')

## Text
st.text('This is a text')

#Create a Simple Dataframe

df = pd.DataFrame({
    "frist column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
})

st.write("Here is the dataframe")
st.write(df)


# Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.write("Here is a line chart")
st.line_chart(chart_data)