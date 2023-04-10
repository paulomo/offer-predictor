from faker import Faker
import pandas as pd
import numpy as np
import random
import decimal

faker = Faker()
# Faker.seed(0)

name = []
start_date = []
end_date = []
monthly_amount = []
contract_addon = []
addon_amount = []
primary_subscriber = []
previous_contract = []
canceled_contract = []
hardware_type = []
customer_age = []
credit_card_on_account = []
postal_code = []
internet_only = []
call_only = []
internet_only = []
on_contract = []


def create_dataset(number):
  for x in range(number):
    name.append(faker.name())
    start_date.append(faker.date_between_dates('-2y', 'now'))
    end_date.append(faker.date_between_dates('-1y', 'now'))
    monthly_amount.append(float(random.randrange(255, 1389))/10)
    contract_addon.append(np.random.randint(0, 2)) # 0 for no and 1 for yes
    addon_amount.append(float(random.randrange(155, 389))/10)
    primary_subscriber.append(np.random.randint(0, 2)) # 0 for no and 1 for yes
    previous_contract.append(np.random.randint(0, 2)) # 0 for no and 1 for yes
    canceled_contract.append(np.random.randint(0, 2)) # 0 for no and 1 for yes
    hardware_type.append(np.random.randint(0, 2)) # 0 for iOS and 1 for Android
    customer_age.append(np.random.randint(18, 60))
    credit_card_on_account.append(np.random.randint(0, 2)) # 0 for no credit in account and 1 for credit card in account
    postal_code.append(faker.postalcode())
    internet_only.append(np.random.randint(0, 2)) # 0 for no and 1 for yes
    call_only.append(np.random.randint(0, 2)) # 0 for no and 1 for yes
    on_contract.append(np.random.randint(0, 2)) # 0 for no and 1 for yes


create_dataset(1000)

df = pd.DataFrame(zip(
    name,
    start_date,
    end_date,
    monthly_amount,
    contract_addon,
    addon_amount,
    primary_subscriber,
    previous_contract,
    canceled_contract,
    hardware_type,
    customer_age,
    credit_card_on_account,
    postal_code,
    internet_only,
    call_only,
    internet_only,
    on_contract,
  ), columns=[
    'name',
    'start_date',
    'end_date',
    'monthly_amount',
    'contract_addon',
    'addon_amount',
    'primary_subscriber',
    'previous_contract',
    'canceled_contract',
    'hardware_type',
    'customer_age',
    'credit_card_on_account',
    'postal_code',
    'internet_only',
    'call_only',
    'internet_only',
    'on_contract'
    ])

df.to_csv("c:/tmp/courses.csv")