"""
property_analyzer.py
--------------------
A simple module for analyzing real estate investment properties.
"""

class PropertyAnalyzer:
    def __init__(self, purchase_price, annual_rent, annual_expenses, down_payment, property_value=None):
        self.purchase_price = purchase_price
        self.annual_rent = annual_rent
        self.annual_expenses = annual_expenses
        self.down_payment = down_payment
        self.property_value = property_value if property_value else purchase_price

    def net_operating_income(self):
        """NOI = Annual Rent - Annual Expenses"""
        return self.annual_rent - self.annual_expenses

    def cap_rate(self):
        """Cap Rate (%) = (NOI / Property Value) * 100"""
        noi = self.net_operating_income()
        return round((noi / self.property_value) * 100, 2)

    def cash_flow(self, mortgage_payment=0):
        """Cash Flow = NOI - Annual Mortgage Payment"""
        noi = self.net_operating_income()
        return noi - mortgage_payment

    def roi(self, mortgage_payment=0):
        """ROI (%) = (Annual Cash Flow / Down Payment) * 100"""
        cash_flow = self.cash_flow(mortgage_payment)
        return round((cash_flow / self.down_payment) * 100, 2)

    def summary(self, mortgage_payment=0):
        """Returns a formatted summary of all metrics"""
        return {
            "Purchase Price": f"${self.purchase_price:,.2f}",
            "Property Value": f"${self.property_value:,.2f}",
            "Annual Rent": f"${self.annual_rent:,.2f}",
            "Annual Expenses": f"${self.annual_expenses:,.2f}",
            "NOI": f"${self.net_operating_income():,.2f}",
            "Cap Rate": f"{self.cap_rate()}%",
            "Cash Flow": f"${self.cash_flow(mortgage_payment):,.2f}",
            "ROI": f"{self.roi(mortgage_payment)}%"
        }
