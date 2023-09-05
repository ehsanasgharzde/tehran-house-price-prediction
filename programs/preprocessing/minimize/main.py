import pandas

FROMPATH = r"../../../files/tehran-areas-house-price.xlsx"
TOPATH = r"../../../files/tehran-areas-house-price-minimized.xlsx"

dataset = pandas.read_excel(FROMPATH)

dataset.loc[:, ["price"]] = dataset.loc[:, ["price"]].apply(lambda x: x / 100000000)
dataset.loc[:, ["price"]] = dataset.loc[:, ["price"]].apply(pandas.to_numeric)

dataset.to_excel(TOPATH, index=False)