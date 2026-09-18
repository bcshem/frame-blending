import math

def gaussian(weights: list, sigma: float):
    center = (len(weights) - 1) / 2
    sum = 0
    for i in range(len(weights)):
        x = abs(center - i)
        gaussian_weight = math.exp(-(math.pow(x, 2)) / (2 * math.pow(sigma, 2)))
        sum += gaussian_weight
        weights[i] = gaussian_weight
    return weights

def uniform(weights: list):
    for i in range(len(weights)):
        weights[i] = 1
    return weights

def asymmetric(weights: list, side: str):
    # TBD
    return

def custom(weights: list):
    for i in range(len(weights)):
        custom_weight = input(f"Weight: {i + 1} / {len(weights)}")
        weights[i] = custom_weight
    return weights
