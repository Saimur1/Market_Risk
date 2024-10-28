# src/portfolio.py
class Portfolio:
    def __init__(self):
        self.assets = {
            "domestic_bond": {"type": "bond", "risk_factors": ["interest_rate"]},
            "domestic_stock": {"type": "equity", "risk_factors": ["market"]},
            "foreign_stock": {"type": "equity", "risk_factors": ["market", "fx"]},
        }

    def get_risk_factors(self):
        """Return a dictionary of assets and their risk factors."""
        return self.assets
