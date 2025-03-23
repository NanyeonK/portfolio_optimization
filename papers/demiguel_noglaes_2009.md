---
title: Portfolio Selection with Robust Estimation 
tags: [portfolio, optimization, robust, estimation]
style: fill
color: warning
description: DeMiguel, Nogales (2009) Portfolio Selection with Robust Estimation, Operations Research, 57(3), 560-577
external_url: 
---

# Background
* Following the mean-variance framework, investor who considers the mean and variance of returns of assets hold the portfolio which position in the efficient frontier that Markowitz (1952) introduced.
* Traditionaly, sample mean and variance are used to estimate the mean and variance of returns, but they are sensitive to outliers and non-normality.
* Sample mean and variance of returns are estimated from historical data, which are subject to estimation errors.
* Robust estimation methods are proposed to mitigate the estimation errors and the sensitivity to outliers and non-normality.

# Motivation
* The difficulty of estimating the mean and variance of returns from historical data (Merton, 1980), recent studies focus only minimizing variance portfolio.
* Jaganattan and Ma (2003) say that the estimation errors of the sample mean is too large to be ignored.
* The mean-variance portfolio does not depend on sample mean estimates, but it still highly susceptible to estimation errors.
* This is surprising because minimum variance portfolios are based on the sample covariance matrix, which is the maximum likelihood estimate (MLE) for normally distributed returns.
* MLE is not efficient when the returns are not normally distributed.
* In portfolio selection, there is extensive evidence that the empirical distribution of returns deviates from a normal distribution

# Contribution
* Propose a method for minimizing portfolio risk through a single nonlinear program using robust estimates (portfolio optimization and robust estimation in a single step)
* Analytically characterize the proposed portfolio in particular, show that the portfolio weights are less sensitive to changes in the asset return distribution
* Comparative analysis of the behavior of proposed portfolios in simulated and empirical data
    * Proposed portfolios are less sensitive to estimation errors and outliers (more stable than mimum-variance portfolios)
    * Maintaining or slightly improving the higher out-of-sample performance of traditional minimum variance portfolios

# Gaps from literature
* Literatures propose a __two-step__ approach (first computing a robust estimate of the covariance matrix and then constructing a portfolio based on it), this study proposes an approach to perform robust estimation and portfolio optimization in a __single step__


# Literature Review
- Classic
    - Markowitz (1952)[] - mean-variance framework
    - Merton (1980)[] - difficulty of estimating the mean and variance of returns

- Methods 
    - Huber (1964)[] - robust estimation
    - Law (1986)[] - robust statistics: the approach based on influence functions
    - Rousseeuw and Leroy (1987) - robust regression and outlier detection

- Porftolio optimization and estimation errors problems
    - Michaud (1989)[] - estimation errors can reduce the optimal portfolio's performance
    - Chopra and Ziemba (1993) [] - how estimation errors in mean, variance, and covariance affect portfolio selection
    - Jaganattan and Ma (2003)[] - pros, and constraints of minimum variance portfolios

- 2-step approach
    - Perret-Gentil and Victoria-Feser (2004) - use S-estimators
    - Vaz-de Melo and Camara (2003) - use M-estimators
    - Cavadini et al. (2001) - use equivariant location and scale M-estimators
    - Welsch and Zhou (2007) - use minimum covariance determinant estimator and winsorization

- Alternative approaches
    - Jorion (1986)
    - Black and Litterman (1992)
    - Pástor and Stambaugh (2000)

# Methodology
## Review traditional literatures
### Simulate Mean-variance and Minimum-variance portfolios
* mean-variance portfolio is sensitive to estimation errors
* minimum-variance portfolio is less sensitive to estimation errors
* When the estimation window includes deviation data, portfolio weights vary significantly
* The rapid growth rate of the squared function makes the sample variance (and therefore the minimum variance portfolio) very sensitive to deviations from normality.

## Robust estimation
* w is the vector of portfolio weights
* $\rho$ is the convex symmetric function with a unique minimum at zero
* $m$ is the m-estimator of the portfolio returns
* r_t is the vector of returns


### M-estimators
$$ s = \frac{1}{T} \Sigma_(t=1)^T \rho (w^T r_t -m)$$

Set the Huber loss function
$$ \rho (r) = \begin{cases} \frac{1}{2} r^2 & \text{if } |r| \leq c \\  (c|r| - \frac{1}{2} c) & \text{if } |r| > c \end{cases} $$
, where $c$ is a constant

Optimization problem
$$ \min_{(w,m)} \frac{1}{T} \Sigma_(t=1)^T \rho (w^T r_t -m) $$$$
$$ \text{subject to } w^T 1 = 1$$

### S-estimators

Set the Tukey's biweight function
$$ \rho (r) = \begin{cases} \frac{c^2}{6}(1-(1-(r/c)^2)^3) & \text{if } |r| \leq c \\ \frac{c^2}{6} & \text{otherwise}  \end{cases} $$

Optimization problem
$$ \min_{w,m,s} s $$
$$ \text{subject to } \frac{1}{T} \Sigma_(t=1)^T \rho (w^T r_t -m),$$
$$ w^T 1 = 1$$

### Two-step approach
* For the detail about 2-step approach, see Perret-Gentil and Victoria-Feser (2004)[], Vaz-de Melo and Camara (2003)[], Cavadini et al. (2001)[], Welsch and Zhou (2007)[]

### Revisit the example in M-estimators and S-estimators


## Define infuence functions
* see Hampel et al. (1986) 

# Empirical Analysis

# Conclusions
* Ro