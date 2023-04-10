import datetime
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


st.title('Customer Offer App')
st.write("""
### This Application will Recommends/Predict offers for Customers.
""")

st.write("""
## Raw Data
""")
df = pd.read_csv("dataset_raw.csv")
st.write(df)

st.write("""
## Transformed Data
""")
df = pd.read_csv("dataset_missing.csv")
st.write(df)

st.write("""
## Cleaned Data
""")
dfClean = pd.read_csv("dataset_5.csv")
st.write(dfClean)

# Add some matplotlib code !
fig, ax = plt.subplots()
df.hist(
bins=8,
column="customer_age",
grid=False,
figsize=(8, 8),
color="#86bf91",
zorder=2,
rwidth=0.9,
ax=ax,
)
st.write(fig)

fig_age, ax_age = plt.subplots()
dfClean.hist(
bins=8,
column="customer_age",
grid=False,
figsize=(8, 8),
color="#86bf91",
zorder=2,
rwidth=0.9,
ax=ax_age,
)
st.write(fig_age)

st.write("""
## Current Customer
""")

# input
st.sidebar.header('User Inputs')
start_date = st.sidebar.date_input('Contract Start Date', datetime.date(2010, 1, 31))
end_date = st.sidebar.date_input('Contract End Date', datetime.date(2010, 1, 31))
contract_amount = st.sidebar.slider('Contract Amount', 0.0, 300.0, 10.0)
previous_offer = st.sidebar.selectbox('Previous Offer',('Data', 'Call', 'Home'))
addons_amount = st.sidebar.slider('Contract Addons Amount', 0.0, 100.0, 0.0)
cancelled_contract = st.sidebar.selectbox('Canceled Contract',('True', 'False'))
age = st.sidebar.slider('Customer Age', 18, 80, 18)
location = st.sidebar.selectbox('Customer Location', ('Ontario', 'BC', 'AB'))
admin = st.sidebar.selectbox('Is Primary Sub',('True', 'False'))
hard_type = st.sidebar.selectbox('Type Of Hardware',('iOS', 'Android'))

# data=[start_date, end_date, contract_amount, previous_offer, addons_amount, cancelled_contract, age, location, admin, hard_type]
# columns=['Start Date', 'end date', 'contract amount', 'previous offer', 'addons amount', 'cancelled contract', 'age', 'location', 'admin', 'hard type']

data_input = [{
    'Start Date': start_date, 'End Date': end_date, 'Contract Amount': contract_amount, 'Previous Offer': previous_offer,
    'Addons Amount': addons_amount, 'Cancelled Contract': cancelled_contract, 'Age': age, 'Location': location, 
    'Admin': admin, 'Hard Type': hard_type
}]

dataFR = pd.DataFrame(data_input)
st.write(dataFR)


st.write("""
## Prediction
""")

st.write("""
## Offer Result
""")


