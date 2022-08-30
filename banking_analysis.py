from enum import auto
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

st.title("Cashback Credit Card Recommender")
st.write("""Identify Which Credit Card Is Best For You!""")

costco_card = st.sidebar.selectbox("Are you a Costco Member?", ("Yes", "No"))
pc_preferred = st.sidebar.selectbox("Do you shop at Loblaw-based companies?", ("Yes", "No"))
esso_preferred = st.sidebar.selectbox("Do you prefer Esso gas?", ("Yes", "No"))
credit_card_qty = st.sidebar.selectbox("How many credit cards do you prefer?", (1, 2))
col1, col2 = st.columns(2)

if costco_card == "Yes":
    with col1:
        costco = st.number_input("Average Monthly Costco Purchases", 0, 10000)
        costcogas = st.number_input("Average Monthly Costco Gas Spend", 0, 10000)
        gas = st.number_input("Average Monthly Other Gas Spend", 0, 10000)
        grocery = st.number_input("Average Monthly Grocery Spend", 0, 10000)
    with col2:
        restaurants = st.number_input("Average Monthly Spend On Restaurants", 0, 10000)
        transportation = st.number_input("Average Monthly Spend On Transportation", 0, 10000)
        bills = st.number_input("Average Monthly Spend On Recurring Bills", 0, 10000)
        other = st.number_input("Average Monthly Spend On Other Purchases", 0, 10000)
else:
    with col1:
        costco = 0
        costcogas = 0
        gas = st.number_input("Average Monthly Other Gas Spend", 0, 10000)
        grocery = st.number_input("Average Monthly Grocery Spend", 0, 10000)
    with col2:
        restaurants = st.number_input("Average Monthly Spend On Restaurants", 0, 10000)
        transportation = st.number_input("Average Monthly Spend On Transportation", 0, 10000)
        bills = st.number_input("Average Monthly Spend On Recurring Bills", 0, 10000)
        other = st.number_input("Average Monthly Spend On Other Purchases", 0, 10000)

total_amount = (costco + costcogas + gas + grocery + restaurants + transportation + bills + other)
st.write("**Total Average Monthly Spend: $**", total_amount)
st.write("**Total Average Annual Spend: $**", total_amount*12)

#Cashback Calculators
# '''Amex Simply Cashback'''
def amex(Costco=None, CostcoGas=None, GasOther=None, Grocery=None, 
         Other = None, Restaurants=None, Transportation=None, Bills=None):

    gas = GasOther
    other = Other
    restaurants = Restaurants
    transportation = Transportation
    grocery = Grocery * 0 
    bills = Bills
    annual_fee = 99
    monthly_cash = []
    monthly_gas = []
    monthly_restaurant = []
    monthly_transportation = []
    monthly_other = []
    monthly_grocery = []
    monthly_bills = []
    for i in range(12):
        if len(monthly_cash) <= 4:
            cash_gas = 0.1 * gas
            cash_other = 0.1 * other
            cash_restaurant = 0.1 * restaurants
            cash_transportation = 0.1 * transportation
            cash_grocery = 0.1 * grocery
            cash_bills = 0.1 * bills
            cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills)
            monthly_cash.append(cash)
            monthly_gas.append(cash_gas)
            monthly_restaurant.append(cash_restaurant)
            monthly_transportation.append(cash_transportation)
            monthly_other.append(cash_other)
            monthly_grocery.append(cash_grocery)
            monthly_bills.append(cash_bills)
        else:
            cash_gas = 0.02 * gas
            cash_other = 0.02 * other
            cash_restaurant = 0.02 * restaurants
            cash_transportation = 0.02 * transportation
            cash_grocery = 0.02 * grocery
            cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills)
            monthly_cash.append(cash)
            monthly_gas.append(cash_gas)
            monthly_restaurant.append(cash_restaurant)
            monthly_transportation.append(cash_transportation)
            monthly_other.append(cash_other)
            monthly_grocery.append(cash_grocery)
            monthly_bills.append(cash_bills)
    annual_cash = round(sum(monthly_cash)-annual_fee,2)
    annual_gas = round(sum(monthly_gas),2)
    annual_restaurant = round(sum(monthly_restaurant),2)
    annual_transportation = round(sum(monthly_transportation),2)
    annual_other = round(sum(monthly_other),2)
    annual_grocery = round(sum(monthly_grocery),2) 
    annual_bills = round(sum(monthly_bills),2)
    return annual_cash, annual_gas, annual_other, annual_restaurant, annual_transportation, annual_grocery, annual_bills

# '''Amex Simply Cashback No Restaurant'''
def amex_no_restaurant(Costco=None, CostcoGas=None, GasOther=None, Grocery=None, 
                       Other = None, Restaurants=None, Transportation=None, Bills=None):

    gas = GasOther
    other = Other
    restaurants = Restaurants * 0
    transportation = Transportation
    grocery = Grocery * 0 
    bills = Bills
    annual_fee = 99
    monthly_cash = []
    monthly_gas = []
    monthly_restaurant = []
    monthly_transportation = []
    monthly_other = []
    monthly_grocery = []
    monthly_bills = []
    for i in range(12):
        if len(monthly_cash) <= 4:
            cash_gas = 0.1 * gas
            cash_other = 0.1 * other
            cash_restaurant = 0.1 * restaurants
            cash_transportation = 0.1 * transportation
            cash_grocery = 0.1 * grocery
            cash_bills = 0.1 * bills
            cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills)
            monthly_cash.append(cash)
            monthly_gas.append(cash_gas)
            monthly_restaurant.append(cash_restaurant)
            monthly_transportation.append(cash_transportation)
            monthly_other.append(cash_other)
            monthly_grocery.append(cash_grocery)
            monthly_bills.append(cash_bills)
        else:
            cash_gas = 0.02 * gas
            cash_other = 0.02 * other
            cash_restaurant = 0.02 * restaurants
            cash_transportation = 0.02 * transportation
            cash_grocery = 0.02 * grocery
            cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills)
            monthly_cash.append(cash)
            monthly_gas.append(cash_gas)
            monthly_restaurant.append(cash_restaurant)
            monthly_transportation.append(cash_transportation)
            monthly_other.append(cash_other)
            monthly_grocery.append(cash_grocery)
            monthly_bills.append(cash_bills)
    annual_cash = round(sum(monthly_cash)-annual_fee,2)
    annual_gas = round(sum(monthly_gas),2)
    annual_restaurant = round(sum(monthly_restaurant),2)
    annual_transportation = round(sum(monthly_transportation),2)
    annual_other = round(sum(monthly_other),2)
    annual_grocery = round(sum(monthly_grocery),2) 
    annual_bills = round(sum(monthly_bills),2)
    return annual_cash, annual_gas, annual_other, annual_restaurant, annual_transportation, annual_grocery, annual_bills

# '''BMO Cashback World Elite'''
def bmo(Costco=None, CostcoGas=None, GasOther=None, Grocery=None, 
        Other = None, Restaurants=None, Transportation=None, Bills=None):

    gas = GasOther
    other = Other
    restaurants = Restaurants
    transportation = Transportation
    grocery = Grocery 
    bills = Bills
    annual_fee = 120
    monthly_cash = []
    monthly_gas = []
    monthly_restaurant = []
    monthly_transportation = []
    monthly_other = []
    monthly_grocery = []
    monthly_bills = []
    for i in range(12):
        if len(monthly_cash) <= 3:
            cash_gas = 0.1 * gas
            cash_other = 0.1 * other
            cash_restaurant = 0.1 * restaurants
            cash_transportation = 0.1 * transportation
            cash_grocery = 0.1 * grocery
            cash_bills = 0.1 * bills
            cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills)
            monthly_cash.append(cash)
            monthly_gas.append(cash_gas)
            monthly_restaurant.append(cash_restaurant)
            monthly_transportation.append(cash_transportation)
            monthly_other.append(cash_other)
            monthly_grocery.append(cash_grocery)
            monthly_bills.append(cash_bills)
        else:
            cash_gas = 0.03 * gas
            cash_other = 0.01 * other
            cash_restaurant = 0.01 * restaurants
            cash_transportation = 0.04 * transportation
            cash_grocery = 0.05 * grocery
            cash_bills = 0.2 * bills
            cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills)
            monthly_cash.append(cash)
            monthly_gas.append(cash_gas)
            monthly_restaurant.append(cash_restaurant)
            monthly_transportation.append(cash_transportation)
            monthly_other.append(cash_other)
            monthly_grocery.append(cash_grocery)
            monthly_bills.append(cash_bills)
    annual_cash = round(sum(monthly_cash)-annual_fee,2)
    annual_gas = round(sum(monthly_gas),2)
    annual_restaurant = round(sum(monthly_restaurant),2)
    annual_transportation = round(sum(monthly_transportation),2)
    annual_other = round(sum(monthly_other),2)
    annual_grocery = round(sum(monthly_grocery),2) 
    annual_bills = round(sum(monthly_bills),2)
    return annual_cash, annual_gas, annual_other, annual_restaurant, annual_transportation, annual_grocery, annual_bills

# '''Scotia Momentum Visa Infinite'''
def scotia(Costco=None, CostcoGas=None, GasOther=None, Grocery=None, 
    Other = None, Restaurants=None, Transportation=None, Bills=None):

    gas = GasOther
    other = Other
    restaurants = Restaurants
    transportation = Transportation
    grocery = Grocery 
    bills = Bills
    annual_fee = 120
    monthly_cash = []
    monthly_gas = []
    monthly_restaurant = []
    monthly_transportation = []
    monthly_other = []
    monthly_grocery = []
    monthly_bills = []
    for i in range(12):
        if len(monthly_cash) <= 3:
            cash_gas = 0.1 * gas
            cash_other = 0.1 * other
            cash_restaurant = 0.1 * restaurants
            cash_transportation = 0.1 * transportation
            cash_grocery = 0.1 * grocery
            cash_bills = 0.1 * bills
            cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills)
            monthly_cash.append(cash)
            monthly_gas.append(cash_gas)
            monthly_restaurant.append(cash_restaurant)
            monthly_transportation.append(cash_transportation)
            monthly_other.append(cash_other)
            monthly_grocery.append(cash_grocery)
            monthly_bills.append(cash_bills)
        else:
            cash_gas = 0.02 * gas
            cash_other = 0.01 * other
            cash_restaurant = 0.01 * restaurants
            cash_transportation = 0.04 * transportation
            cash_grocery = 0.04 * grocery
            cash_bills = 0.04 * bills
            cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills)
            monthly_cash.append(cash)
            monthly_gas.append(cash_gas)
            monthly_restaurant.append(cash_restaurant)
            monthly_transportation.append(cash_transportation)
            monthly_other.append(cash_other)
            monthly_grocery.append(cash_grocery)
            monthly_bills.append(cash_bills)
    annual_cash = round(sum(monthly_cash)-annual_fee,2)
    annual_gas = round(sum(monthly_gas),2)
    annual_restaurant = round(sum(monthly_restaurant),2)
    annual_transportation = round(sum(monthly_transportation),2)
    annual_other = round(sum(monthly_other),2)
    annual_grocery = round(sum(monthly_grocery),2) 
    annual_bills = round(sum(monthly_bills),2)
    return annual_cash, annual_gas, annual_other, annual_restaurant, annual_transportation, annual_grocery, annual_bills

# '''TD Cashback Visa Infinite'''
def td(Costco=None, CostcoGas=None, GasOther=None, Grocery=None, 
    Other = None, Restaurants=None, Transportation=None, Bills=None):

    gas = GasOther
    other = Other
    restaurants = Restaurants
    transportation = Transportation
    grocery = Grocery 
    bills = Bills
    annual_fee = 120
    monthly_cash = []
    monthly_gas = []
    monthly_restaurant = []
    monthly_transportation = []
    monthly_other = []
    monthly_grocery = []
    monthly_bills = []
    for i in range(12):
        if len(monthly_cash) <= 3:
            cash_gas = 0.1 * gas
            cash_other = 0.1 * other
            cash_restaurant = 0.1 * restaurants
            cash_transportation = 0.1 * transportation
            cash_grocery = 0.1 * grocery
            cash_bills = 0.1 * bills
            cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills)
            monthly_cash.append(cash)
            monthly_gas.append(cash_gas)
            monthly_restaurant.append(cash_restaurant)
            monthly_transportation.append(cash_transportation)
            monthly_other.append(cash_other)
            monthly_grocery.append(cash_grocery)
            monthly_bills.append(cash_bills)
        else:
            cash_gas = 0.03 * gas
            cash_other = 0.01 * other
            cash_restaurant = 0.01 * restaurants
            cash_transportation = 0.01 * transportation
            cash_grocery = 0.03 * grocery
            cash_bills = 0.03 * bills
            cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills)
            monthly_cash.append(cash)
            monthly_gas.append(cash_gas)
            monthly_restaurant.append(cash_restaurant)
            monthly_transportation.append(cash_transportation)
            monthly_other.append(cash_other)
            monthly_grocery.append(cash_grocery)
            monthly_bills.append(cash_bills)
    annual_cash = round(sum(monthly_cash)-annual_fee,2)
    annual_gas = round(sum(monthly_gas),2)
    annual_restaurant = round(sum(monthly_restaurant),2)
    annual_transportation = round(sum(monthly_transportation),2)
    annual_other = round(sum(monthly_other),2)
    annual_grocery = round(sum(monthly_grocery),2) 
    annual_bills = round(sum(monthly_bills),2)
    return annual_cash, annual_gas, annual_other, annual_restaurant, annual_transportation, annual_grocery, annual_bills

# '''CIBC Dividend Cashback'''
def cibc(Costco=None, CostcoGas=None, GasOther=None, Grocery=None, 
    Other = None, Restaurants=None, Transportation=None, Bills=None):

    gas = GasOther
    other = Other
    restaurants = Restaurants
    transportation = Transportation
    grocery = Grocery 
    bills = Bills
    annual_fee = 120
    monthly_cash = []
    monthly_gas = []
    monthly_restaurant = []
    monthly_transportation = []
    monthly_other = []
    monthly_grocery = []
    monthly_bills = []
    for i in range(12):
        if len(monthly_cash) <= 3:
            cash_gas = 0.1 * gas
            cash_other = 0.1 * other
            cash_restaurant = 0.1 * restaurants
            cash_transportation = 0.1 * transportation
            cash_grocery = 0.1 * grocery
            cash_bills = 0.1 * bills
            cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills)
            monthly_cash.append(cash)
            monthly_gas.append(cash_gas)
            monthly_restaurant.append(cash_restaurant)
            monthly_transportation.append(cash_transportation)
            monthly_other.append(cash_other)
            monthly_grocery.append(cash_grocery)
            monthly_bills.append(cash_bills)
        else:
            cash_gas = 0.04 * gas
            cash_other = 0.01 * other
            cash_restaurant = 0.02 * restaurants
            cash_transportation = 0.01 * transportation
            cash_grocery = 0.04 * grocery
            cash_bills = 0.02 * bills
            cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills)
            monthly_cash.append(cash)
            monthly_gas.append(cash_gas)
            monthly_restaurant.append(cash_restaurant)
            monthly_transportation.append(cash_transportation)
            monthly_other.append(cash_other)
            monthly_grocery.append(cash_grocery)
            monthly_bills.append(cash_bills)
    annual_cash = round(sum(monthly_cash)-annual_fee,2)
    annual_gas = round(sum(monthly_gas),2)
    annual_restaurant = round(sum(monthly_restaurant),2)
    annual_transportation = round(sum(monthly_transportation),2)
    annual_other = round(sum(monthly_other),2)
    annual_grocery = round(sum(monthly_grocery),2) 
    annual_bills = round(sum(monthly_bills),2)
    return annual_cash, annual_gas, annual_other, annual_restaurant, annual_transportation, annual_grocery, annual_bills

# '''CIBC Dividend Cashback No Restaurant'''
def cibc_no_restaurant(Costco=None, CostcoGas=None, GasOther=None, Grocery=None, 
    Other = None, Restaurants=None, Transportation=None, Bills=None):

    gas = GasOther
    other = Other
    restaurants = Restaurants
    transportation = Transportation * 0
    grocery = Grocery 
    bills = Bills
    annual_fee = 120
    monthly_cash = []
    monthly_gas = []
    monthly_restaurant = []
    monthly_transportation = []
    monthly_other = []
    monthly_grocery = []
    monthly_bills = []
    for i in range(12):
        if len(monthly_cash) <= 3:
            cash_gas = 0.1 * gas
            cash_other = 0.1 * other
            cash_restaurant = 0.1 * restaurants
            cash_transportation = 0.1 * transportation
            cash_grocery = 0.1 * grocery
            cash_bills = 0.1 * bills
            cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills)
            monthly_cash.append(cash)
            monthly_gas.append(cash_gas)
            monthly_restaurant.append(cash_restaurant)
            monthly_transportation.append(cash_transportation)
            monthly_other.append(cash_other)
            monthly_grocery.append(cash_grocery)
            monthly_bills.append(cash_bills)
        else:
            cash_gas = 0.03 * gas
            cash_other = 0.01 * other
            cash_restaurant = 0.01 * restaurants
            cash_transportation = 0.01 * transportation
            cash_grocery = 0.03 * grocery
            cash_bills = 0.03 * bills
            cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills)
            monthly_cash.append(cash)
            monthly_gas.append(cash_gas)
            monthly_restaurant.append(cash_restaurant)
            monthly_transportation.append(cash_transportation)
            monthly_other.append(cash_other)
            monthly_grocery.append(cash_grocery)
            monthly_bills.append(cash_bills)
    annual_cash = round(sum(monthly_cash)-annual_fee,2)
    annual_gas = round(sum(monthly_gas),2)
    annual_restaurant = round(sum(monthly_restaurant),2)
    annual_transportation = round(sum(monthly_transportation),2)
    annual_other = round(sum(monthly_other),2)
    annual_grocery = round(sum(monthly_grocery),2) 
    annual_bills = round(sum(monthly_bills),2)
    return annual_cash, annual_gas, annual_other, annual_restaurant, annual_transportation, annual_grocery, annual_bills

# '''CIBC Costco'''
def cibcCostco(Costco=None, CostcoGas=None, GasOther=None, Grocery=None, 
    Other = None, Restaurants=None, Transportation=None, Bills=None):

    costco = Costco
    costcogas = CostcoGas
    gas = GasOther
    other = Other
    restaurants = Restaurants
    transportation = Transportation
    grocery = Grocery 
    bills = Bills
    annual_fee = 120
    monthly_cash = []
    monthly_gas = []
    monthly_restaurant = []
    monthly_transportation = []
    monthly_other = []
    monthly_grocery = []
    monthly_bills = []
    monthly_costco = []
    monthly_costcogas = []
    for i in range(12):
        cash_costcogas = 0.03 * costcogas
        cash_costco = 0.03 * costco
        cash_gas = 0.02 * gas
        cash_other = 0.01 * other
        cash_restaurant = 0.03 * restaurants
        cash_transportation = 0.01 * transportation
        cash_grocery = 0.01 * grocery
        cash_bills = 0.01 * bills
        cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills + cash_costco + cash_costcogas)
        monthly_cash.append(cash)
        monthly_gas.append(cash_gas)
        monthly_restaurant.append(cash_restaurant)
        monthly_transportation.append(cash_transportation)
        monthly_other.append(cash_other)
        monthly_grocery.append(cash_grocery)
        monthly_bills.append(cash_bills)
        monthly_costco.append(cash_costco)
        monthly_costcogas.append(cash_costcogas)
    annual_cash = round(sum(monthly_cash)-annual_fee,2)
    annual_gas = round(sum(monthly_gas),2)
    annual_restaurant = round(sum(monthly_restaurant),2)
    annual_transportation = round(sum(monthly_transportation),2)
    annual_other = round(sum(monthly_other),2)
    annual_grocery = round(sum(monthly_grocery),2) 
    annual_bills = round(sum(monthly_bills),2)
    annual_costco = round(sum(monthly_costco),2)
    annual_costcogas = round(sum(monthly_costcogas),2)
    return annual_cash, annual_gas, annual_other, annual_restaurant, annual_transportation, annual_grocery, annual_bills, annual_costco, annual_costcogas

# '''CIBC Costco No Restaurant'''
def cibcCostco_no_restaurant(Costco=None, CostcoGas=None, GasOther=None, Grocery=None, 
    Other = None, Restaurants=None, Transportation=None, Bills=None):

    costco = Costco
    costcogas = CostcoGas
    gas = GasOther
    other = Other
    restaurants = Restaurants * 0
    transportation = Transportation
    grocery = Grocery 
    bills = Bills
    annual_fee = 120
    monthly_cash = []
    monthly_gas = []
    monthly_restaurant = []
    monthly_transportation = []
    monthly_other = []
    monthly_grocery = []
    monthly_bills = []
    monthly_costco = []
    monthly_costcogas = []
    for i in range(12):
        cash_costcogas = 0.03 * costcogas
        cash_costco = 0.03 * costco
        cash_gas = 0.02 * gas
        cash_other = 0.01 * other
        cash_restaurant = 0.03 * restaurants
        cash_transportation = 0.01 * transportation
        cash_grocery = 0.01 * grocery
        cash_bills = 0.01 * bills
        cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills + cash_costco + cash_costcogas)
        monthly_cash.append(cash)
        monthly_gas.append(cash_gas)
        monthly_restaurant.append(cash_restaurant)
        monthly_transportation.append(cash_transportation)
        monthly_other.append(cash_other)
        monthly_grocery.append(cash_grocery)
        monthly_bills.append(cash_bills)
        monthly_costco.append(cash_costco)
        monthly_costcogas.append(cash_costcogas)
    annual_cash = round(sum(monthly_cash)-annual_fee,2)
    annual_gas = round(sum(monthly_gas),2)
    annual_restaurant = round(sum(monthly_restaurant),2)
    annual_transportation = round(sum(monthly_transportation),2)
    annual_other = round(sum(monthly_other),2)
    annual_grocery = round(sum(monthly_grocery),2) 
    annual_bills = round(sum(monthly_bills),2)
    annual_costco = round(sum(monthly_costco),2)
    annual_costcogas = round(sum(monthly_costcogas),2)
    return annual_cash, annual_gas, annual_other, annual_restaurant, annual_transportation, annual_grocery, annual_bills, annual_costco, annual_costcogas

# '''Simplii Financial Cashback'''
def simplii(Costco=None, CostcoGas=None, GasOther=None, Grocery=None, 
    Other = None, Restaurants=None, Transportation=None, Bills=None):

    gas = GasOther 
    other = Other
    restaurants = Restaurants
    transportation = Transportation
    grocery = Grocery 
    bills = Bills
    annual_fee = 0
    monthly_cash = []
    monthly_gas = []
    monthly_restaurant = []
    monthly_transportation = []
    monthly_other = []
    monthly_grocery = []
    monthly_bills = []
    for i in range(12):
        if len(monthly_cash) <= 4:
            cash_gas = 0.1 * gas * 0 
            cash_other = 0.1 * other * 0 
            cash_restaurant = 0.1 * restaurants 
            cash_transportation = 0.1 * transportation * 0 
            cash_grocery = 0.1 * grocery * 0 
            cash_bills = 0.1 * bills * 0 
            cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills)
            monthly_cash.append(cash)
            monthly_gas.append(cash_gas)
            monthly_restaurant.append(cash_restaurant)
            monthly_transportation.append(cash_transportation)
            monthly_other.append(cash_other)
            monthly_grocery.append(cash_grocery)
            monthly_bills.append(cash_bills)
        else:
            cash_gas = 0.015 * gas 
            cash_other = 0.01 * other * 0 
            cash_restaurant = 0.04 * restaurants
            cash_transportation = 0.01 * transportation * 0 
            cash_grocery = 0.015 * grocery
            cash_bills = 0.02 * bills * 0 
            cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills)
            monthly_cash.append(cash)
            monthly_gas.append(cash_gas)
            monthly_restaurant.append(cash_restaurant)
            monthly_transportation.append(cash_transportation)
            monthly_other.append(cash_other)
            monthly_grocery.append(cash_grocery)
            monthly_bills.append(cash_bills)
    annual_cash = round(sum(monthly_cash)-annual_fee,2)
    annual_gas = round(sum(monthly_gas),2)
    annual_restaurant = round(sum(monthly_restaurant),2)
    annual_transportation = round(sum(monthly_transportation),2)
    annual_other = round(sum(monthly_other),2)
    annual_grocery = round(sum(monthly_grocery),2) 
    annual_bills = round(sum(monthly_bills),2)
    return annual_cash, annual_gas, annual_other, annual_restaurant, annual_transportation, annual_grocery, annual_bills

# '''PC Financial World Elite'''
def pc(Costco=None, CostcoGas=None, GasOther=None, Grocery=None, 
    Other = None, Restaurants=None, Transportation=None, Bills=None):

    gas = GasOther 
    other = Other
    restaurants = Restaurants
    transportation = Transportation
    grocery = Grocery 
    bills = Bills
    annual_fee = 0
    monthly_cash = []
    monthly_gas = []
    monthly_restaurant = []
    monthly_transportation = []
    monthly_other = []
    monthly_grocery = []
    monthly_bills = []
    for i in range(12):   
        cash_gas = 0.03 * gas 
        cash_other = 0.01 * other 
        cash_restaurant = 0.01 * restaurants
        cash_transportation = 0.01 * transportation
        cash_grocery = 0.03 * grocery
        cash_bills = 0.01 * bills
        cash = (cash_gas + cash_other + cash_restaurant + cash_transportation + cash_grocery + cash_bills)
        monthly_cash.append(cash)
        monthly_gas.append(cash_gas)
        monthly_restaurant.append(cash_restaurant)
        monthly_transportation.append(cash_transportation)
        monthly_other.append(cash_other)
        monthly_grocery.append(cash_grocery)
        monthly_bills.append(cash_bills)
    annual_cash = round(sum(monthly_cash)-annual_fee,2)
    annual_gas = round(sum(monthly_gas),2)
    annual_restaurant = round(sum(monthly_restaurant),2)
    annual_transportation = round(sum(monthly_transportation),2)
    annual_other = round(sum(monthly_other),2)
    annual_grocery = round(sum(monthly_grocery),2) 
    annual_bills = round(sum(monthly_bills),2)
    return annual_cash, annual_gas, annual_other, annual_restaurant, annual_transportation, annual_grocery, annual_bills

#Recommendation Calculations
# '''Credit Card Recommendation Function (1 Card)'''
def cc_rec_one(costo_card = None, pc_preffered = None, esso_preferred = None, restaurants = None, total_amount = None, 
           amex = None, bmo = None, cibc = None, td = None, scotia = None, simplii = None, 
           costco = None, pc = None, amex_no_restaurant = None, costco_no_restaurant = None):
    
    amex_val = amex 
    bmo_val = bmo 
    cibc_val = cibc 
    td_val = td 
    scotia_val = scotia 
    pc_val = pc 
    simplii_val = simplii
    values = (amex_val, bmo_val, cibc_val, td_val, scotia_val, pc_val, simplii_val)
    max_val = max(values)
    index_max_val = values.index(max_val)
    val_dic = {0: 'Amex Simply Cash Preferred', 1: 'BMO World Elite', 2: 'CIBC Dividend Cash', 3: 'TD Visa Infite Cash', 
                4: 'Scotiabank Momentum Visa Infinite', 5: 'PC Financial World Elite', 6: 'Simplii Financial'}
    cc_1 = max_val
    cc_1_name = val_dic[index_max_val]
    total_cashback = cc_1
    percent_return = (total_cashback/(total_amount*12))*100

    if costco_card == "Yes":
        cc_1 = costco
        cc_1_name = 'Costco CIBC'
        total_cashback = cc_1
        percent_return = (total_cashback/(total_amount*12))*100
    
    return st.write('**Best Card:**', cc_1_name), \
           st.write('**Total Estimated Annual Cashback $:**',round(total_cashback,2)), \
           st.write('**Average Estimated Annual Cashback %:**', round(percent_return,2))
            

# '''Credit Card Recommendation Function (2 Cards)'''
def cc_rec_two(costo_card = None, pc_preffered = None, esso_preferred = None, restaurants = None, total_amount = None, 

           amex = None, bmo = None, cibc = None, td = None, scotia = None, simplii = None, 
           costco = None, pc = None, amex_no_restaurant = None, costco_no_restaurant = None, cibc_no_restaurant=None):
    
    restaurant_percentage = restaurants/total_amount
    if restaurant_percentage >= 0.20:
        cc_1 = simplii
        cc_1_name = 'Simplii Financial'
    else:
        cc_1 = amex
        cc_1_name = 'Amex Simply Cash Preferred'

    if costo_card == "Yes":
        cc_2 = costco
        cc_2_name = 'Costco CIBC'  
    elif pc_preffered or esso_preferred == "Yes":
        amex_val = amex 
        bmo_val = bmo 
        cibc_val = cibc 
        td_val = td 
        scotia_val = scotia 
        pc_val = pc 
        values = (amex_val, bmo_val, cibc_val, td_val, scotia_val, pc_val)
        max_val = max(values)
        index_max_val = values.index(max_val)
        val_dic = {0: 'Amex Simply Cash Preferred', 1: 'BMO World Elite', 2: 'CIBC Dividend Cash', 3: 'TD Visa Infite Cash', 4: 'Scotiabank Momentum Visa Infinite', 5: 'PC Financial World Elite'}
        cc_2 = max_val
        cc_2_name = val_dic[index_max_val]
    else:
        amex_val = amex 
        bmo_val = bmo 
        cibc_val = cibc 
        td_val = td 
        scotia_val = scotia 
        values_2 = (amex_val, bmo_val, cibc_val, td_val, scotia_val)
        max_val_2 = max(values_2)
        index_max_val_2 = values_2.index(max_val_2)
        val_dic_2 = {0:'Amex Simply Cash Preferred', 1: 'BMO World Elite', 2: 'CIBC Dividend Cash', 3: 'TD Visa Infite Cash', 4: 'Scotiabank Momentum Visa Infinite'}
        cc_2 = max_val_2
        cc_2_name = val_dic_2[index_max_val_2]
    total_cashback = cc_1 + cc_2
    percent_return = (total_cashback/(total_amount*12))*100

    if cc_2_name == 'Amex Simply Cash Preferred':
        amex_val_no_restaurant = amex_no_restaurant 
        bmo_val = bmo 
        cibc_val = cibc 
        td_val = td 
        scotia_val = scotia 
        pc_val = pc 
        values = (amex_val_no_restaurant, bmo_val, cibc_val, td_val, scotia_val, pc_val)
        max_val = max(values)
        index_max_val = values.index(max_val)
        val_dic = {0: 'Amex Simply Cash Preferred', 1: 'BMO World Elite', 2: 'CIBC Dividend Cash', 3: 'TD Visa Infite Cash', 4: 'Scotiabank Momentum Visa Infinite', 5: 'PC Financial World Elite'}
        cc_2 = max_val
        cc_2_name = val_dic[index_max_val]
        total_cashback = cc_1 + cc_2
        percent_return = (total_cashback/(total_amount*12))*100
    
    if (cc_1_name == 'Simplii Financial' or cc_1_name == 'Amex Simply Cash Preferred')  and cc_2_name == 'Costco CIBC':
        cc_2 = costco_no_restaurant
        total_cashback = cc_1 + cc_2
        percent_return = (total_cashback/(total_amount*12))*100
    
    if cc_2_name == 'CIBC Dividend Cash':
        amex_val_no_restaurant = amex_no_restaurant 
        bmo_val = bmo 
        cibc_val_no_restarant = cibc_no_restaurant
        td_val = td 
        scotia_val = scotia 
        pc_val = pc 
        values = (amex_val_no_restaurant, bmo_val, cibc_val_no_restarant, td_val, scotia_val, pc_val)
        max_val = max(values)
        index_max_val = values.index(max_val)
        val_dic = {0: 'Amex Simply Cash Preferred', 1: 'BMO World Elite', 2: 'CIBC Dividend Cash', 3: 'TD Visa Infite Cash', 4: 'Scotiabank Momentum Visa Infinite', 5: 'PC Financial World Elite'}
        cc_2 = max_val
        cc_2_name = val_dic[index_max_val]
        total_cashback = cc_1 + cc_2
        percent_return = (total_cashback/(total_amount*12))*100

    return st.write('**Best Cards:**', cc_1_name, 'and', cc_2_name), \
           st.write('**Total Estimated Annual Cashback: $**',round(total_cashback,2)), \
           st.write('**Average Estimated Annual Cashback %:**', round(percent_return,2))

# '''Calculating Casback for Each Credit Card'''
amex_annual_cash, amex_annual_gas, amex_annual_other, \
amex_annual_restaurant, amex_annual_transportation, amex_annual_grocery, \
amex_annual_bills = \
    amex(Costco=costco, CostcoGas=costcogas, GasOther=gas, Grocery=grocery, 
         Other=other, Restaurants=restaurants, Transportation=transportation, Bills=bills)

amex_no_restaurant_annual_cash, amex_no_restaurant_annual_gas, \
amex_no_restaurant_annual_other, amex_no_restaurant_annual_restaurant, amex_no_restaurant_annual_transportation, \
amex_no_restaurant_annual_grocery, amex_no_restaurant_annual_bills  = \
    amex_no_restaurant(Costco=costco, CostcoGas=costcogas, 
                       GasOther=gas, Grocery=grocery, Other=other, Restaurants=restaurants, 
                       Transportation=transportation, Bills=bills)

bmo_annual_cash, bmo_annual_gas, bmo_annual_other, \
bmo_annual_restaurant, bmo_annual_transportation, bmo_annual_grocery, \
bmo_annual_bills = bmo(Costco=costco, CostcoGas=costcogas, GasOther=gas, Grocery=grocery, 
            Other=other, Restaurants=restaurants, Transportation=transportation, Bills=bills)

cibc_annual_cash, cibc_annual_gas, cibc_annual_other, \
cibc_annual_restaurant, cibc_annual_transportation, cibc_annual_grocery, \
cibc_annual_bills = cibc(Costco=costco, CostcoGas=costcogas, GasOther=gas, Grocery=grocery, 
            Other=other, Restaurants=restaurants, Transportation=transportation, Bills=bills)

cibc_no_restaurant_annual_cash, cibc_no_restaurant_annual_gas, \
cibc_no_restaurant_annual_other, cibc_no_restaurant_annual_restaurant, \
cibc_no_restaurant_annual_transportation, cibc_no_restaurant_annual_grocery, \
cibc_no_restaurant_annual_bills = cibc_no_restaurant(Costco=costco, CostcoGas=costcogas, GasOther=gas, Grocery=grocery, 
            Other=other, Restaurants=restaurants, Transportation=transportation, Bills=bills)

scotia_annual_cash, scotia_annual_gas, scotia_annual_other, scotia_annual_restaurant, \
scotia_annual_transportation, scotia_annual_grocery, scotia_annual_bills = scotia(Costco=costco, CostcoGas=costcogas, GasOther=gas, Grocery=grocery, 
            Other=other, Restaurants=restaurants, Transportation=transportation, Bills=bills)

td_annual_cash, td_annual_gas, td_annual_other, \
td_annual_restaurant, td_annual_transportation, \
td_annual_grocery, td_annual_bills = td(Costco=costco, CostcoGas=costcogas, GasOther=gas, Grocery=grocery, 
            Other=other, Restaurants=restaurants, Transportation=transportation, Bills=bills)

costco_annual_cash, costco_annual_gas, costco_annual_other, \
costco_annual_restaurant, costco_annual_transportation, \
costco_annual_grocery, costco_annual_bills, \
annual_costco, annual_costcogas = cibcCostco(Costco=costco, CostcoGas=costcogas, GasOther=gas, Grocery=grocery, 
            Other=other, Restaurants=restaurants, Transportation=transportation, Bills=bills)

costco_no_restaurant_annual_cash, costco_no_restaurant_annual_gas, \
costco_no_restaurant_annual_other, costco_no_restaurant_annual_restaurant, \
costco_no_restaurant_annual_transportation, costco_no_restaurant_annual_grocery, \
costco_no_restaurant_annual_bills, costco_no_restaurant_annual_costco, \
costco_no_restaurant_annual_costcogas = cibcCostco_no_restaurant(Costco=costco, CostcoGas=costcogas, GasOther=gas, Grocery=grocery, 
            Other=other, Restaurants=restaurants, Transportation=transportation, Bills=bills)

simplii_annual_cash, simplii_annual_gas, simplii_annual_other, \
simplii_annual_restaurant, simplii_annual_transportation, simplii_annual_grocery, \
simplii_annual_bills = simplii(Costco=costco, CostcoGas=costcogas, GasOther=gas, Grocery=grocery, 
            Other=other, Restaurants=restaurants, Transportation=transportation, Bills=bills)

pc_annual_cash, pc_annual_gas, pc_annual_other, pc_annual_restaurant, \
pc_annual_transportation, annual_grocery, annual_bills = pc(Costco=costco, CostcoGas=costcogas, GasOther=gas, Grocery=grocery, 
            Other=other, Restaurants=restaurants, Transportation=transportation, Bills=bills)

if credit_card_qty == 1 and total_amount > 0:
    cc_1_name = cc_rec_one(costo_card = costco_card, pc_preffered = pc_preferred, esso_preferred = esso_preferred, restaurants = restaurants, total_amount = total_amount, 
       amex = amex_annual_cash, bmo = bmo_annual_cash, cibc = cibc_annual_cash, td = td_annual_cash, scotia = scotia_annual_cash, \
       simplii = simplii_annual_cash, costco = costco_annual_cash, pc = pc_annual_cash, amex_no_restaurant = amex_no_restaurant_annual_cash, 
       costco_no_restaurant = costco_no_restaurant_annual_cash)

if credit_card_qty == 2 and total_amount > 0:
    cc_rec_two(costo_card = costco_card, pc_preffered = pc_preferred, esso_preferred = esso_preferred, restaurants = restaurants, total_amount = total_amount, 
       amex = amex_annual_cash, bmo = bmo_annual_cash, cibc = cibc_annual_cash, td = td_annual_cash, scotia = scotia_annual_cash, simplii = simplii_annual_cash, \
       costco = costco, pc = pc_annual_cash, amex_no_restaurant = amex_no_restaurant_annual_cash, 
       costco_no_restaurant = costco_no_restaurant_annual_cash, cibc_no_restaurant = cibc_no_restaurant_annual_cash)

#Plotting Monthly Spend
if costco_card == "Yes":
    data = {'Costco':costco, 'Costco Gas':costcogas, 'Other Gas':gas, 'Grocery':grocery, 'Restaurants':restaurants,
             'Transportation':transportation, 'Recurring Bills':bills, 'Other':other}
    labels = [key for key,value in data.items() if value!=0]
    sizes = [value for value in data.values() if value!=0]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels,
            shadow=False, startangle=90, autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '', 
            pctdistance=0.85)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig1 = plt.gcf()
    fig1.gca().add_artist(centre_circle)
    plt.title("Average Monthly Spend Breakdown")
    st.pyplot(fig1)
else:
    data = {'Other Gas':gas, 'Grocery':grocery, 'Restaurants':restaurants,
             'Transportation':transportation, 'Recurring Bills':bills, 'Other':other}
    labels = [key for key,value in data.items() if value!=0]
    sizes = [value for value in data.values() if value!=0]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels,
            shadow=False, startangle=90, autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '', 
            pctdistance=0.85)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig1 = plt.gcf()
    fig1.gca().add_artist(centre_circle)
    plt.title("Average Monthly Spend Breakdown")
    st.pyplot(fig1)

