import numpy as np
import scipy as sp
import pandas as pd

# Set random seed
seed = 42
np.random.seed(42)

# Load from csv
training = pd.read_csv("training.csv")
test = pd.read_csv("test.csv")

# Remove first collumn
training = training.iloc[:,1:]
test = test.iloc[:,1:]

# Group genhlth values together
goodHealth = ["excellent","very good", "good"]
badHealth = ["fair","poor"]

def groupHealth(row):
    if row["genhlth"] in goodHealth:
        return 1
    else:
        return 0

training["genhlth"] = training.apply(groupHealth, axis = 1)
test["genhlth"] = test.apply(groupHealth,axis = 1)

# Change gender to 0/1
def changeGender(row):
    if row["gender"] == "m":
        return 1
    else:
        return 0

training["gender"] = training.apply(changeGender, axis = 1)
test["gender"] = test.apply(changeGender,axis = 1)

# Split into x and y
xColumns = ["exerany","hlthplan","smoke100","height","weight","wtdesire","age","gender"]
yColumns = ["genhlth"]

train_x = training[xColumns]
train_y = training[yColumns]

test_x = test[xColumns]
test_y = test[yColumns]

# Train model
from sklearn.svm import SVC
model = SVC(kernel="linear", random_state=seed).fit(train_x,train_y)

# Test model on test data
from sklearn import metrics
pred_y = model.predict(test_x)

acc_score = metrics.accuracy_score(test_y,pred_y)
print('Model accuracy: {:.2f}%'.format(acc_score*100))

# Test model on training data
pred_y = model.predict(train_x)

acc_score = metrics.accuracy_score(train_y,pred_y)
print('Training accuracy: {:.2f}%'.format(acc_score*100))






