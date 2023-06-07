# Implementing the Black-Scholes Formula in Python

import numpy as np
from scipy.stats import norm

# define variables
r = 0.01
S = 30
K = 40
T = 240/365
sigma = 0.30

def blackScholes(r, S, K, T, sigma, type="C"):
    "Calculate BS option price for a call or put."
    d1 = (np.log(S/k) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)