import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("final-project/Energy_Usage_2010_API.csv")
x = data[["KWH JANUARY 2010","KWH FEBRUARY 2010","KWH MARCH 2010","KWH APRIL 2010","KWH MAY 2010","KWH JUNE 2010"]].values
y = data["COMMUNITY AREA NAME"].values

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .2)

model = LinearRegression().fit(xtrain, ytrain)

coef = np.around(model.coef_, 2)
intercept = round(float(model.intercept_), 2)
r_squared = round(model.score(x, y),2)
print(f"Model's Linear Equation: y={coef[0]}x1 + {coef[1]}x2 + {coef[1]}x3 + {coef[1]}x4 + {coef[1]}x5 + {coef[1]}x6 + {intercept}")
print("R Squared value:", r_squared)

print("***************")
print("Testing Results")
predict = model.predict(xtest)
predict = np.around(predict, 2)

for index in range(len(xtest)):
    actual = ytest[index] # gets the actual y value from the ytest dataset
    predicted_y = predict[index] # gets the predicted y value from the predict variable
    x_coord = xtest[index] # gets the x value from the xtest dataset
    print(f"KWH JANUARY 2010: {x_coord[0]} KWH FEBRUARY 2010: {x_coord[1]} KWH MARCH 2010: {x_coord[2]} KWH APRIL 2010: {x_coord[3]} KWH MAY 2010: {x_coord[4]} KWH JUNE 2010: {x_coord[5]} Actual: {actual} Predicted: {predicted_y}")
    