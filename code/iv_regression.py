import sklearn.linear_model
import numpy as np
def two_stage_regression(target, endo=None, exo=None, instruments=None):
    n = len(target)
    def fix_shape(data):
        if data is None or data==[]:
            return np.array([]).reshape(n,0)
        if isinstance(data,list):
            return np.array(data).T
        if len(data.shape) == 1:
            return data.reshape(n,1)
        return data

    endo = fix_shape(endo)
    exo = fix_shape(exo)
    instruments = fix_shape(instruments)

    predetermined = np.hstack([exo, instruments])

    def project(vector,basis,affine=True):
        return sklearn.linear_model.LinearRegression(fit_intercept=affine).fit(basis,vector).predict(basis)

    projected_endo = np.array([project(var, predetermined) for var in endo.T]).T
    regressors = np.hstack([projected_endo, exo])

    model = sklearn.linear_model.LinearRegression().fit(regressors,target)
    return (model.intercept_, *model.coef_)
