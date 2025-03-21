# Set Target Value

# Load Libraries
import numpy as np
import cvxopt

# Price
## Linear Price 
## I reccomend to use 'Close' price for price data

## Log Price
def ln_price(price):
    return np.log(price)

# Return
## Linear Return
def linear_return(price):
    return price.pct_change()

## Log Return
def ln_return(price):
    return ln_price(price).diff()


# Mean
mu = np.mean(ln_return(price))

# Covariance
cov = np.cov(ln_return(price))


# Net Asset Value
## Capital Weight
def capital_weight(price, capital_weight_t_1, linear_return):
    return np.multiply(capital_weight_t_1, (1 + linear_return))

def capital_weight_a(w_t_cap, nav_t):
    return w_t_cap * nav_t

## Net Asset Value (nav)
def net_asset_value(capital_weight, capital):
    return np.dot(np.ones(len(capital_weight)), capital_weight) + capital

def net_asset_value_t(nav_t_1, w_cap_t_1, r_t_lin):
    return nav_t_1 + np.dot(w_cap_t_1, r_t_lin)

def port_ret(nav_t_1, nav_t):
    return (nav_t - nav_t_1) / nav_t_1

def port_ret_a(w_t_1, r_t_lin):
    return np.dot(w_t_1, r_t_lin)

# Cummul_ret
## Full reinvesting
def cum_ret_fr(nav_t_1, r_port):
    return nav_t_1 * (1 + r_port)

## Constant reinvesting
def cum_ret_cr(nav_t_1, r_port):
    return nav_t_1 + r_port


