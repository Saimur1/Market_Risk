# src/stress_test.py
class StressTest:
    def __init__(self, portfolio, interest_rate_shock, fx_shock):
        self.portfolio = portfolio
        self.interest_rate_shock = interest_rate_shock
        self.fx_shock = fx_shock

    def run_scenario(self):
        for asset, props in self.portfolio.assets.items():
            impact = 0
            if "interest_rate" in props["risk_factors"]:
                impact += self.interest_rate_shock * 0.5
            if "fx" in props["risk_factors"]:
                impact += self.fx_shock * 0.3
            print(f"Asset: {asset}, Expected Loss Impact: {impact}")
