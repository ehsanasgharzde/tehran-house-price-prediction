import os
import pandas


# FROMPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\results\regression"
FROMPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\results\sensitivity"
# TOPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\results\combination\results-combined.xlsx"
TOPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\results\combination\sensitivities-combined.xlsx"

files = os.scandir(FROMPATH)
files = [file for file in files]

dataset = pandas.DataFrame({
    "algorithm": [],
    "area": [],
    "floor": [],
    "meterage": [],
    "age": [],
    "room": [],
    "parking": [],
    "storeroom": [],
    "elevator": [],
})

for file in files:
    result = pandas.read_excel(file.path)
    dataset = pandas.concat([dataset, result], axis=0, ignore_index=True)

dataset.to_excel(TOPATH, index=False)