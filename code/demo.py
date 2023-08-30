#!/usr/bin/env python3
from generate_data import generate_data
from iv_regression import two_stage_regression

def estimate_demand_elasticity(price, quantity, weather):
    intercept, *coefs = two_stage_regression(endo = price, instruments = weather, target=quantity)
    return coefs[0] #Coefficient of price

if __name__ == "__main__":
    price, quantity, weather = generate_data()
    print(estimate_demand_elasticity(price, quantity, weather))
