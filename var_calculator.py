# src/var_calculator.py
import numpy as np

class RiskMetrics:
    @staticmethod
    def calculate_var(returns, confidence_level=0.95):
        var = np.percentile(returns, (1 - confidence_level) * 100)
        return var

    @staticmethod
    def calculate_es(returns, confidence_level=0.95):
        var = RiskMetrics.calculate_var(returns, confidence_level)
        es = returns[returns <= var].mean()
        return es
