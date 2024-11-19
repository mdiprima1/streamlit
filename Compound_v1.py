import streamlit as st

# Title of the app
#st.title("The Benefits of Compounding")

# User inputs
start_amount = st.number_input("Initial Investment Amount (USD):", min_value=0, value=10000, step=1000)
monthly_savings = st.number_input("Monthly Savings (USD):", min_value=0, value=300, step=100)
annual_return = st.slider("Annual Return Rate (%):", min_value=0.0, max_value=50.0, value=10.0, step=0.5)
years = st.slider("Number of Years:", min_value=1, max_value=70, value=20, step=1)  # Max years set to 70

# Calculate the total amount with compounding
monthly_return_rate = (1 + annual_return / 100) ** (1 / 12) - 1
months = years * 12
total_amount = start_amount

for month in range(months):
    total_amount = total_amount * (1 + monthly_return_rate) + monthly_savings

# Display the total amount with a line break before it, without decimals
st.markdown(f"<br><h1 style='text-align: center; font-size: 36px;'><strong>Total Amount After {years} Years:<br> ${total_amount:,.0f}</strong></h1>", unsafe_allow_html=True)