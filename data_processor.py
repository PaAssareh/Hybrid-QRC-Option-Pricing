import numpy as np
import perceval as pcvl

def generate_simple_market_data():
    """Generates a single market scenario: [S, K, T, r, sigma]"""
    # Standard values: Spot=100, Strike=100, Time=1yr, rate=5%, vol=20%
    return np.array([100, 100, 1.0, 0.05, 0.2])

def encode_to_phases(data_vector):
    """Converts financial numbers into angles (0 to 2*pi) for the laser."""
    # Simple normalization logic
    phases = [(val % 10) * np.pi / 5 for val in data_vector]
    return phases

# Test it
data = generate_simple_market_data()
encoded_phases = encode_to_phases(data)
print(f"Market Data: {data}")
print(f"Encoded Phases for Quantum Circuit: {encoded_phases}")
