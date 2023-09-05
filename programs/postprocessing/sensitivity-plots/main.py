import numpy
import pandas
import seaborn
import matplotlib
import matplotlib.pyplot


FROMPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\results\combination\sensitivities-combined.xlsx"
TOPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\results\sensitivity-plots"

dataset = pandas.read_excel(FROMPATH)

xcol = ["area", "floor", "meterage", "age", "room", "parking", "storeroom", "elevator"]
address = ["bayesian-ridge", "elastic-net", "gradient-boosting-regressor", "kernel-ridge", "lasso", "lgbm-regressor", "linear-regression", "sgd-regressor", "sv-regressor", "xg-boost-regressor"]
algorithms = dataset.algorithm.tolist()

i = 0
for algorithm in algorithms:
    X = xcol

    Y = dataset.loc[dataset.algorithm == algorithm]
    Y = Y.loc[:, xcol]
    Y = Y.values.tolist()[0]


    matplotlib.pyplot.rcParams["figure.figsize"] = (10, 10)
    matplotlib.pyplot.bar(X, Y, label=f"{algorithm} Sensitivity")
    matplotlib.pyplot.xticks(rotation=45)
    matplotlib.pyplot.savefig(f"{TOPATH}\{address[i]}-sensitivity-plot.png", dpi=300)
    matplotlib.pyplot.close()

    i += 1

