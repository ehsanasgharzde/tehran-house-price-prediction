import numpy
import pandas
import seaborn
import matplotlib
import matplotlib.pyplot


FROMPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\results\combination\results-combined.xlsx"
TOPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\results\heatmap-plots"

algortihms = {
    "Bayesian Ridge": "bayesian-ridge",
    "Elastic Net": "elastic-net",
    "Gradient Boosting Regressor": "gradient-boost",
    "Kernel Ridge": "kernel-ridge",
    "Lasso": "lasso",
    "LGBM Regressor": "lgbm",
    "Linear Regression": "linear-regression",
    "SGD Regressor": "stochastic-gradient-descent",
    "SV Regressor": "support-vector-machine",
    "XGB Regressor": "xg-boost",
}


mcol = ["area", "floor", "meterage", "age", "room", "parking", "storeroom", "elevator", "price"]
pcol = ["area", "floor", "meterage", "age", "room", "parking", "storeroom", "elevator", "prediction"]

dataset = pandas.read_excel(FROMPATH)

main = dataset.loc[:, mcol]
predicted = dataset.loc[:, pcol]

for name, path in algortihms.items():
    correlation = main.corr()

    matplotlib.pyplot.rcParams["figure.figsize"] = (10, 10)

    heatmap = seaborn.heatmap(correlation, annot=True)
    heatmap.set_title("Main", fontdict={"fontsize": 12}, pad=12)

    matplotlib.pyplot.savefig(f"{TOPATH}\{path}\heatmap-plot-main.png", dpi=300)
    matplotlib.pyplot.close()


    correlation = predicted.corr()
    
    matplotlib.pyplot.rcParams["figure.figsize"] = (10, 10)

    heatmap = seaborn.heatmap(correlation, annot=True)
    heatmap.set_title(name, fontdict={"fontsize": 12}, pad=12)

    matplotlib.pyplot.savefig(f"{TOPATH}\{path}\heatmap-plot-predicted.png", dpi=300)
    matplotlib.pyplot.close()
