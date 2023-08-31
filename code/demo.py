#!/usr/bin/env python3
from generate_data import generate_data
from iv_regression import two_stage_regression
import numpy as np

def estimate_demand_elasticity(price, quantity, weather):
    intercept, *coefs = two_stage_regression(endo = price, instruments = weather, target=quantity)
    return coefs[0] #Coefficient of price

def estimate_supply_elasticity(price, quantity, weather, demand_elasticity):
    instrument = quantity + price * demand_elasticity
    intercept, *coefs = two_stage_regression(endo = price, exo = weather, instruments = instrument, target=quantity)
    return coefs[0] #Coefficient of price

if __name__ == "__main__":
    price, quantity, weather = generate_data()
    demand_elasticity = estimate_demand_elasticity(price, quantity, weather)
    #supply_elasticity = estimate_supply_elasticity(price, quantity, weather, demand_elasticity)
    print(f"{demand_elasticity=}")#, {supply_elasticity=}")
