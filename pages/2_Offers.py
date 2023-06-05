import datetime
import pandas as pd
import pickle

# import matplotlib.pyplot as plt
import streamlit as st

st.title("Customer Offer")
st.write(
    """
### This Application will Recommends/Predict offers for Customers.
"""
)

# ===============================================================================================

# input
col1, col2, col3 = st.columns(3)
with col1:
    start_date = st.date_input("Contract Start Date", datetime.date(2010, 1, 31))
    end_date = st.date_input("Contract End Date", datetime.date(2010, 1, 31))
    contract_amount = st.slider("Contract Amount", 0.0, 300.0, 10.0)

with col2:
    previous_offer = st.selectbox("Previous Offer", ("Call", "Home"))
    addons_amount = st.slider("Contract Addons Amount", 0.0, 100.0, 0.0)
    cancelled_contract = st.selectbox("Canceled Contract", ("True", "False"))

with col3:
    age = st.slider("Customer Age", 18, 80, 18)
    location = st.selectbox("Customer Location", ("Ontario", "BC", "AB"))
    admin = st.selectbox("Is Primary Sub", ("True", "False"))
    hard_type = st.selectbox("Type Of Hardware", ("iOS", "Android"))


# ================================================================================================

st.write(
    """
### The Current Customer
"""
)

data_input = [
    {
        "Start Date": start_date,
        "End Date": end_date,
        "Contract Amount": contract_amount,
        "Previous Offer": previous_offer,
        "Addons Amount": addons_amount,
        "Cancelled Contract": cancelled_contract,
        "Age": age,
        "Location": location,
        "Admin": admin,
        "Hard Type": hard_type,
    }
]

dataFR = pd.DataFrame(data_input)
st.write(dataFR)

# ============================================================================================================

# Prepare input
pre_offer = 1 if previous_offer == "Call" else 0
can_contract = 1 if cancelled_contract == "True" else 0
# st.write(pre_offer)
# st.write(can_contract)

st.write(
    """
### Submit To Predict The Offer
"""
)

model = pickle.load(open("./finalized_model.sav", "rb"))
if st.button("Submit To Predict"):
    make_prediction = model.predict([[]])

st.write(
    """
#### The Offer is 
"""
)


# =================================================================================================


st.write(
    """

"""
)

st.write(
    """

"""
)

st.write(
    """

"""
)

st.write(
    """

"""
)

st.write(
    """

"""
)

st.write(
    """

"""
)
st.write(
    """

"""
)

st.write(
    """

"""
)

st.write(
    """

"""
)

st.write(
    """
## Raw Data
"""
)
df = pd.read_csv("dataset_raw.csv")
st.write(df)

st.write(
    """
## Transformed Data
"""
)
df = pd.read_csv("dataset_missing.csv")
st.write(df)

st.write(
    """
## Cleaned Data
"""
)
dfClean = pd.read_csv("dataset_5.csv")
st.write(dfClean)

# Add some matplotlib code !
# fig, ax = plt.subplots()
# df.hist(
# bins=8,
# column="customer_age",
# grid=False,
# figsize=(8, 8),
# color="#86bf91",
# zorder=2,
# rwidth=0.9,
# ax=ax,
# )
# st.write(fig)

# fig_age, ax_age = plt.subplots()
# dfClean.hist(
# bins=8,
# column="customer_age",
# grid=False,
# figsize=(8, 8),
# color="#86bf91",
# zorder=2,
# rwidth=0.9,
# ax=ax_age,
# )
# st.write(fig_age)
