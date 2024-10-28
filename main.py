# main.py
from src.portfolio import Portfolio
from src.risk_factors import InterestRateModel, FXRateModel
from src.var_calculator import RiskMetrics
from src.stress_test import StressTest
import numpy as np

# Initialize portfolio
portfolio = Portfolio()

# Initialize models
ir_model = InterestRateModel(r0=0.05, kappa=0.15, theta=0.04, sigma=0.01)
fx_model = FXRateModel(fx0=1.2, mu=0.02, sigma=0.05)

# Simulate paths
interest_rate_path = ir_model.simulate_path()
fx_rate_path = fx_model.simulate_path()

# Risk calculations
returns = np.random.normal(0, 0.02, 1000)
var = RiskMetrics.calculate_var(returns)
es = RiskMetrics.calculate_es(returns)

# Run stress test
stress_test = StressTest(portfolio, interest_rate_shock=0.02, fx_shock=0.1)
stress_test.run_scenario()

print(f"Simulated VaR: {var}, ES: {es}")
