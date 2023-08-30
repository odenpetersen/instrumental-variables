#Scenario is from Hamilton Time Series Chapter 9 (but is used in many other introductory expositions)
import numpy as np
def generate_data(n = 1000,
                  supply_base = 2,       demand_base = 10,
                  supply_elasticity = 1, demand_elasticity = 5,
                  supply_noise = 0.5,    demand_noise = 0.2,      weather_noise = 0.6):
    weather_shocks = np.random.normal(size=n) * weather_noise
    demand_shocks  = np.random.normal(size=n) * demand_noise
    supply_shocks  = np.random.normal(size=n) * supply_noise

    #Equilibrium price using Newton's method
    price = np.zeros(n)
    quantity_supplied, quantity_demanded = -np.inf, np.inf
    while np.max(np.abs(quantity_supplied-quantity_demanded)) > 1e-4: #For linear quantity curves, only one step should be required
        quantity_supplied = supply_base + supply_elasticity * price + supply_shocks + weather_shocks
        quantity_demanded = demand_base - demand_elasticity * price + demand_shocks
        price = price - (quantity_supplied - quantity_demanded) / (supply_elasticity + demand_elasticity)

    quantity = demand_elasticity * price + demand_shocks
    return price, quantity, weather_shocks
