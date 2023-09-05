import pandas
import SALib
from SALib.analyze import morris
from SALib.sample.morris import sample
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


FROMPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\files\tehran-areas-house-price-minimized.xlsx"
TOPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\results\sensitivity\linear-regression-sensitivity.xlsx"

dataset = pandas.read_excel(FROMPATH)

xcol = ["area", "floor", "meterage", "age", "room", "parking", "storeroom", "elevator"]
ycol = ["price"]

X = dataset.loc[:, xcol]
Y = dataset.loc[:, ycol]

inputs = {
    'num_vars': 8,
    'names': ["area", "floor", "meterage", "age", "room", "parking", "storeroom", "elevator"],
    'bounds': [[dataset.area.min(), dataset.area.max()],
               [dataset.floor.min(), dataset.floor.max()],
               [dataset.meterage.min(), dataset.meterage.max()],
               [dataset.age.min(), dataset.age.max()],
               [dataset.room.min(), dataset.room.max()],
               [dataset.parking.min(), dataset.parking.max()],
               [dataset.storeroom.min(), dataset.storeroom.max()],
               [dataset.elevator.min(), dataset.elevator.max()]]
        }

xtrain, xtest, ytrain, ytest = train_test_split(X, Y, test_size=0.2, train_size=0.8, random_state=35)
values = sample(inputs, N=930, num_levels=4, optimal_trajectories=None)

MODEL = LinearRegression()

MODEL.fit(xtrain, ytrain)

prediction = MODEL.predict(values)

ANALYSIS = morris.analyze(inputs, values, prediction, conf_level=0.95, num_levels=4, num_resamples=100)

result = pandas.DataFrame({
    "algorithm": ["Linear Regression"],
    "area": [ANALYSIS["mu_star"][0]],
    "floor": [ANALYSIS["mu_star"][1]],
    "meterage": [ANALYSIS["mu_star"][2]],
    "age": [ANALYSIS["mu_star"][3]],
    "room": [ANALYSIS["mu_star"][4]],
    "parking": [ANALYSIS["mu_star"][5]],
    "storeroom": [ANALYSIS["mu_star"][6]],
    "elevator": [ANALYSIS["mu_star"][7]],
})

result.to_excel(TOPATH, index=False)
