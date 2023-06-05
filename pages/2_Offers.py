import datetime
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
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
tab1, tab2 = st.tabs(["Prediction", "Data"])
col1, col2, col3 = tab1.columns(3)
with tab1:
    tab1.header("Prediction")
    with col1:
        start_date = tab1.date_input("Contract Start Date", datetime.date(2010, 1, 31))
        monthly_amount = tab1.selectbox("Monthly Amount", (45, 65))
        end_date = tab1.date_input("Contract End Date", datetime.date(2010, 1, 31))
        contract_amount = tab1.slider("Contract Amount", 0.0, 300.0, 10.0)

    with col2:
        previous_offer = tab1.selectbox("Previous Offer", ("Call", "Home"))
        addons_amount = tab1.slider("Contract Addons Amount", 0.0, 100.0, 0.0)
        cancelled_contract = tab1.selectbox("Canceled Contract", ("True", "False"))

    with col3:
        age = tab1.slider("Customer Age", 18, 80, 18)
        location = tab1.selectbox("Customer Location", ("Ontario", "BC", "AB"))
        admin = tab1.selectbox("Is Primary Sub", ("True", "False"))
        hard_type = tab1.selectbox("Type Of Hardware", ("iOS", "Android"))

# ================================================================================================

tab1.write(
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
tab1.write(dataFR)

# ============================================================================================================

# Prepare input
# feature_cols = ['monthly_amount','contract_addon','addon_amount','primary_subscriber', 'previous_contract', 'canceled_contract', 'hardware_type', 'customer_age', 'credit_card_on_account', 'postal_code', 'internet_only', 'call_only', 'internet_and_call']
pre_offer = 1 if previous_offer == "Call" else 0
can_contract = 1 if cancelled_contract == "True" else 0
# st.write(pre_offer)
# st.write(can_contract)

tab1.write(
    """
### Submit To Predict The Offer
"""
)

model = pickle.load(open("./finalized_model.sav", "rb"))
if tab1.button("Submit To Predict"):
    make_prediction = model.predict([[]])

tab1.write(
    """
#### The Offer is 
"""
)


with tab2:
    tab2.header("Raw Data")
    df = pd.read_csv("dataset_raw.csv")
    tab2.write(df)

    tab2.write(
        """
    ## Transformed Data
    """
    )
    df = pd.read_csv("dataset_missing.csv")
    tab2.write(df)

    tab2.write(
        """
    ## Cleaned Data
    """
    )
    dfClean = pd.read_csv("dataset_5.csv")
    tab2.write(dfClean)

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
