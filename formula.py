import pandas as pd

def predict_prices(current_year, num_years, inflation_rate, interest_rate, initial_price):
    total_rate = inflation_rate + interest_rate
    prices = [initial_price * (1 + total_rate)**t for t in range(1, num_years + 1)]
    years = [current_year + t for t in range(1, num_years + 1)]
    data = {'Year': years, 'Price': prices}
    df = pd.DataFrame(data)
    return df

def present_worth(F, i, n):
    P = F / ((1 + i) ** n)
    return P

def future_value(P, i, n):
    F = P * ((1 + i) ** n)
    return F

def Annual(PV, i, n):
    AP = PV * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    return AP

def round_to_nearest_half(x):
    return round(x * 2) / 2