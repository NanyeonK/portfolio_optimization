# Import Libraries
import numpy as np
import cvx

# Transaction cost constraint
def slip_cost(bid, ask):
    return (bid - ask) / (ask + bid)

#def nav_tran(w_c, c, )

def net_asset_value(capital_weight, capital):
    return np.dot(np.ones(len(capital_weight)), capital_weight) + capital

# Basic constraint
## Long-only constraint (no shorting)
## w >= 0

# Capital budget constraint
## 1^T w + c = 1
def capital_budget(w, c):
    if np.dot(np.ones(len(w)), w) + c <= 1:
        return np.dot(np.ones(len(w)), w) + c 
    return 


