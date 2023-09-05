import numpy
import pandas
import seaborn
import matplotlib
import matplotlib.pyplot
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import BayesianRidge
from sklearn.linear_model import SGDRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import ElasticNet
from xgboost.sklearn import XGBRegressor
from sklearn.linear_model import Lasso
from lightgbm import LGBMRegressor
from sklearn.svm import SVR


FROMPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\results\combination\results-combined.xlsx"
TOPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\results\plots"

algortihms = {
    "Bayesian Ridge": [BayesianRidge(), "bayesian-ridge"],
    "Elastic Net": [ElasticNet(), "elastic-net"],
    "Gradient Boosting Regressor": [GradientBoostingRegressor(), "gradient-boost"],
    "Kernel Ridge": [KernelRidge(), "kernel-ridge"],
    "Lasso": [Lasso(), "lasso"],
    "LGBM Regressor": [LGBMRegressor(), "lgbm"],
    "Linear Regression": [LinearRegression(), "linear-regression"],
    "SGD Regressor": [SGDRegressor(), "stochastic-gradient-descent"],
    "SV Regressor": [SVR(), "support-vector-machine"],
    "XGB Regressor": [XGBRegressor(), "xg-boost"],
}


xcol = ["area", "floor", "meterage", "age", "room", "parking", "storeroom", "elevator"]
ycol = [["price"], ["prediction"]]

dataset = pandas.read_excel(FROMPATH)


for name, regressor in algortihms.items():
    Y = dataset.loc[dataset.algorithm == name]
    Y = Y.loc[:, ycol[0]]
    Y = Y.price.tolist()

    fig, axs = matplotlib.pyplot.subplots()
    axs.plot(Y)
    axs.set_title("Main")

    fig.savefig(f"{TOPATH}\{regressor[1]}\sklearn-models-plot-main.png", dpi=300)
    matplotlib.pyplot.close()

    fig, axs = matplotlib.pyplot.subplots()
    axs.plot(Y)

    y = dataset.loc[dataset.algorithm == name]
    y = y.loc[:, ycol[1]]
    y = y.prediction.tolist()

    axs.plot(y)
    axs.set_title(name)

    fig.savefig(f"{TOPATH}\{regressor[1]}\sklearn-models-plot-compare.png", dpi=300)
    matplotlib.pyplot.close()
