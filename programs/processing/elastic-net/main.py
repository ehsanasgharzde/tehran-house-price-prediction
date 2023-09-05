import pandas
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split


FROMPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\files\tehran-areas-house-price-minimized.xlsx"
TOPATH = r"C:\Users\Klap.ir\Desktop\price-prediction-machine-learning-python\results\regression\elastic-net.xlsx"

dataset = pandas.read_excel(FROMPATH)


xcol = ["area", "floor", "meterage", "age", "room", "parking", "storeroom", "elevator"]
ycol = ["price"]

X = dataset.loc[:, xcol]
Y = dataset.loc[:, ycol]

xtrain, xtest, ytrain, ytest = train_test_split(X, Y, test_size=0.2, train_size=0.8, random_state=35)

MODEL = ElasticNet()

MODEL.fit(xtrain, ytrain)

prediction = MODEL.predict(xtest)
accuracy = MODEL.score(xtest, ytest)

print(prediction)
print(accuracy)

result = pandas.DataFrame({
    "algorithm": ["Elastic Net" for i in range(len(xtest))],
    "area": list(map(lambda x: x[1], xtest.area.items())),
    "floor": list(map(lambda x: x[1], xtest.floor.items())),
    "meterage": list(map(lambda x: x[1], xtest.meterage.items())),
    "age": list(map(lambda x: x[1], xtest.age.items())),
    "room": list(map(lambda x: x[1], xtest.room.items())),
    "parking": list(map(lambda x: x[1], xtest.parking.items())),
    "storeroom": list(map(lambda x: x[1], xtest.storeroom.items())),
    "elevator": list(map(lambda x: x[1], xtest.elevator.items())),
    "price": list(map(lambda y: y[1], ytest.price.items())),
    "prediction": [prediction[i] for i in range(len(xtest))],
    "accuracy": [accuracy for i in range(len(xtest))],
})

result.to_excel(TOPATH, index=False)