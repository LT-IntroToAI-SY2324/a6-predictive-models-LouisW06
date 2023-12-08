import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("part4-classification/suv_data.csv")
data['Gender'].replace(['Male','Female'],[0,1],inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

# Step 1: Print the values for x and y
print(x)
print(y)
# Step 2: Standardize the data using StandardScaler, 
scaler = StandardScaler().fit(x)
# Step 3: Transform the data
x = scaler.transform(x)
# Step 4: Split the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y)

# Step 5: Fit the data
model = linear_model.LogisticRegression().fit(x_train, y_train)
print("Accuracy:", model.score(x_test, y_test))
print("*************")
print("Testing Results:")
print("")
print(y_test)
for index in range(len(x_test)):
    x = x_test[index]
    x = x.reshape(-1, 3)
    print(x)
    y_pred = int(model.predict(x))

    if y_pred == 0:
        y_pred = "Not purchased"
    else:
        y_pred = "Purchased"

    
    actual = y_test[index]
    if actual == 0:
        actual = "Not purchased"
    else:
        actual = "Purchased"
    print("Prediction: " + y_pred + " Actual: " + actual)
    print("")