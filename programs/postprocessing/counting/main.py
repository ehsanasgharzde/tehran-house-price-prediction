import numpy
import pandas
import seaborn
import matplotlib
import matplotlib.pyplot
from collections import Counter


FROMPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\files\tehran-areas-house-price-minimized.xlsx"
TOPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\results\areas"


dataset = pandas.read_excel(FROMPATH)

total = dict()
for i in range(1, (22 + 1)):
    X = dataset.loc[dataset.area == i]
    DISTRICT = X.loc[:, "district"]
    DISTRICT = DISTRICT.tolist()

    DISTRICT = dict(Counter(DISTRICT))

    x = list(map(lambda x: x.strip(), list(DISTRICT.keys())))
    y = list(DISTRICT.values())

    matplotlib.pyplot.rcParams["figure.figsize"] = (10, 10)
    matplotlib.pyplot.bar(x, y, label=f"Area NO. {i}")
    matplotlib.pyplot.xticks(rotation=45)
    matplotlib.pyplot.savefig(f"{TOPATH}\sklearn-models-bar-area-{i}.png", dpi=300)
    matplotlib.pyplot.close()

    total.update({i: len(X)})

    matplotlib.pyplot.cla()


x = list(map(lambda x: str(x), total.keys()))
y = list(total.values())

matplotlib.pyplot.rcParams["figure.figsize"] = (20, 20)
matplotlib.pyplot.bar(x, y, label=f"All Areas")
matplotlib.pyplot.xticks(rotation=45)
matplotlib.pyplot.savefig(f"{TOPATH}\sklearn-models-bar-area-all.png", dpi=300)
matplotlib.pyplot.close()
