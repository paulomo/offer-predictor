import datetime
import pandas as pd
# import matplotlib.pyplot as plt
import streamlit as st


st.title('Customer Offer App')
st.write("""
### This Application will Recommends/Predict offers for Customers.
""")


# input
st.sidebar.header('User Inputs')
st.sidebar.date_input('Contract Start Date', datetime.date(2010, 1, 31))
st.sidebar.date_input('Contract End Date', datetime.date(2010, 1, 31))
st.sidebar.slider('Contract Amount', 0.0, 300.0, 10.0)
st.sidebar.selectbox('Previous Offer',('Data', 'Call', 'Home'))
st.sidebar.slider('Contract Addons Amount', 0.0, 100.0, 0.0)
st.sidebar.selectbox('Canceled Contract',('True', 'False'))
st.sidebar.slider('Customer Age', 18, 80, 18)
st.sidebar.selectbox('Customer Location', ('Ontario', 'BC', 'AB'))
st.sidebar.selectbox('Is Primary Sub',('True', 'False'))
st.sidebar.selectbox('Type Of Hardware',('iOS', 'Android'))
st.sidebar.selectbox('Previous Offer',('1', '2', '3'))

st.write("""
## Original Data
""")
df = pd.read_csv("dataset_missing.csv")
st.write(df)

st.write("""
## Cleaned Data
""")
dfClean = pd.read_csv("dataset_5.csv")
st.write(dfClean)

# Add some matplotlib code !
# fig, ax = plt.subplots()
# df.hist(
# bins=8,
# column="Customer Age",
# grid=False,
# figsize=(8, 8),
# color="#86bf91",
# zorder=2,
# rwidth=0.9,
# ax=ax,
# )
# st.write(fig)

st.write("""
## Prediction
""")

st.write("""
## Offer Result
""")


