import datetime
import streamlit as st


st.title('Customer Offer Predictor')
st.write("""
### This Application predict best offer for the customer
""")

st.sidebar.header('User Inputs')
st.sidebar.date_input('Contract Start Date', datetime.date(2019, 7, 6))
st.sidebar.date_input('Contract End Date', datetime.date(2019, 7, 6))
st.sidebar.slider('Contract Amount', 0.0, 300.0, 10.0)
st.sidebar.slider('Contract Addons', 0.0, 100.0, (25.0, 75.0))
st.sidebar.slider('Contract Addons Amount', 0.0, 100.0, (25.0, 75.0))
st.sidebar.slider('Canceled Contract', 0.0, 100.0, (25.0, 75.0))
st.sidebar.slider('Customer Age', 0.0, 100.0, (25.0, 75.0))
st.sidebar.selectbox('Customer Location', ('Ontario', 'BC', 'AB'))
st.sidebar.selectbox('Is Primary Sub',('True', 'False'))
st.sidebar.slider('Joined Since', 0.0, 100.0, (25.0, 75.0))
st.sidebar.selectbox('Type Of Hardware',('iOS', 'Android'))
st.sidebar.selectbox('Previous Offer',('1', '2', '3'))
