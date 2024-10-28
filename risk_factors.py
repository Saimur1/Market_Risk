# src/risk_factors.py
import numpy as np

class InterestRateModel:
    def __init__(self, r0, kappa, theta, sigma, dt=0.01):
        self.r0 = r0
        self.kappa = kappa
        self.theta = theta
        self.sigma = sigma
        self.dt = dt

    def simulate_path(self, T=1):
        n_steps = int(T / self.dt)
        rates = np.zeros(n_steps)
        rates[0] = self.r0

        for t in range(1, n_steps):
            dr = self.kappa * (self.theta - rates[t-1]) * self.dt + self.sigma * np.sqrt(self.dt) * np.random.normal()
            rates[t] = rates[t-1] + dr

        return rates

class FXRateModel:
    def __init__(self, fx0, mu, sigma, dt=0.01):
        self.fx0 = fx0
        self.mu = mu
        self.sigma = sigma
        self.dt = dt

    def simulate_path(self, T=1):
        n_steps = int(T / self.dt)
        rates = np.zeros(n_steps)
        rates[0] = self.fx0

        for t in range(1, n_steps):
            dS = rates[t-1] * (self.mu * self.dt + self.sigma * np.sqrt(self.dt) * np.random.normal())
            rates[t] = rates[t-1] + dS

        return rates
