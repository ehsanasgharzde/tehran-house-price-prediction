import numpy
import pandas
import seaborn
import matplotlib
import matplotlib.pyplot


FROMPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\files\tehran-areas-house-price-minimized.xlsx"
TOPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\results\features"

dataset = pandas.read_excel(FROMPATH)

xcol = ["area", "floor", "meterage", "age", "room", "parking", "storeroom", "elevator"]


for i in range(1, (22 + 1)):
    X = dataset.loc[dataset.area == i]
    X = X.loc[:, xcol]

    for feature in xcol:
        fig, axs = matplotlib.pyplot.subplots()
        axs.plot(X[feature].tolist())
        axs.set_title(f"Area NO. {i}")

        fig.savefig(fr"{TOPATH}\{i}\{feature}-observation.png", dpi=300)
        matplotlib.pyplot.close()

for feature in xcol:
    fig, axs = matplotlib.pyplot.subplots()
    axs.plot(dataset[feature].tolist())
    axs.set_title("All Areas")

    fig.savefig(fr"{TOPATH}\all\{feature}-observation.png", dpi=300)
    matplotlib.pyplot.close()
