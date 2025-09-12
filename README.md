# Real-Estate-Property-Analyzer
# Purpose: Python tool to calculate price per square foot, estimate mortgages, and compare properties quickly.
# Tools: pandas (data handling) matplotlib (visualizations) tkinter or PySimpleGUI (GUI development)

"""
Name: Real Estate Property Analyzer 
Author: Juju Melendez
Purpose: Python tool to calculate price per square foot, estimate mortgages, and compare properties quickly.
Tools: pandas (data handling) matplotlib (visualizations) tkinter or PySimpleGUI (GUI development)
"""
# AI generated code

import matplotlib.pyplot as plt

# Sample property details
price = 320000
sqft = 1600
down_payment = 0.20
interest_rate = 0.06
loan_term = 30  # years

# Calculate price per square foot
price_per_sqft = price / sqft
print(f"Price per square foot: ${price_per_sqft:.2f}")

# Estimate monthly mortgage payment (basic calculation)
loan_amount = price * (1 - down_payment)
monthly_rate = interest_rate / 12
months = loan_term * 12
mortgage_payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
print(f"Estimated monthly mortgage: ${mortgage_payment:.2f}")

# Compare with sample comps
comps = {'Property A': 190, 'Property B': 205, 'Property C': 210, 'Subject Property': price_per_sqft}
plt.bar(comps.keys(), comps.values())
plt.title("Price per Square Foot Comparison")
plt.ylabel("Price per Sq Ft ($)")
plt.show()
