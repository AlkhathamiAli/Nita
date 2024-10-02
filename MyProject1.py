import numpy as np
import pandas as pd
import streamlit as st

st.title("Work Hard For Your Project")
st.write("Work Hard For Your Project")

data = pd.DataFrame({
    "Name":["Ali","Abdullah","Ahmad","Hussain"],
    "Marks":[99,95,99,100]
})

st.write("Below is the Dataframe for Marks:")
st.write(data)

chart_data = pd.DataFrame(
    np.random.randn(20,4), columns = ["A","B","C","D"]
)

st.line_chart(chart_data)