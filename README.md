# Instrumental Variables
Run `demo.py` to estimate the slope of the demand curve specified in `generate_data.py`.

Using default parameters, the estimate should be very, very close to the true value of $5$.

## Some Explication
Consider the regression problem $y=X\beta + \epsilon$.

Linear constraints, such as those arising from an equilibriating process or other system of simultaneous equations, may lead to correlations between some columns of $X$ and the residual $\epsilon$.

The solution to this is to introduce instruments $\xi$ not occuring in the original regression problem under consideration that are correlated with $X$ but not $\epsilon$. Asymptotic consistency replaces requirements on the covariance structure of $X$ and $\xi$ outlined in [1].

Projecting the endogenous columns of $X$ onto $\xi$ and then fitting the regression model decorrelates the features from $\epsilon$ and leads to valid regression analysis that can then be used (cautiously!) for causal inference.

## References
[1] James Hamilton, Time Series Analysis, Chapter 9.2, page 241.
