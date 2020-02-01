import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

def preprocess():
    data = pd.read_csv("../Relevant_Data/final.csv")
    reduced = data.loc[:, np.isin(data.columns, ['Season', 'Team0', 'Team1'], invert=True)]
    reduced = reduced.sample(reduced.shape[0], random_state=0).reset_index(drop=True)
    nan_cols = list(reduced.isnull().any().index[reduced.isnull().any()])
    reduced = reduced.loc[:, np.isin(reduced.columns, nan_cols, invert=True)]

    X = reduced.loc[:, reduced.columns != "Winner"]
    y = pd.DataFrame(reduced.loc[:, "Winner"])

    X_train = X.loc[0:39999, :] # 80% ish
    y_train = y.loc[0:39999, :]
    X_test = X.loc[40000:, :] # 20% ish
    y_test = y.loc[40000:, :]

    stddev = X_train.std()
    mean = X_train.mean()
    X_train = (X_train - mean)/stddev
    X_test = (X_test - mean)/stddev

    pca = PCA(0.99)
    pca.fit(X_train)
    X_train = pd.DataFrame(pca.transform(X_train))
    X_test = pd.DataFrame(pca.transform(X_test))

    X_train.to_csv("X_train.csv", index=False)
    X_test.to_csv("X_test.csv", index=False)
    y_train.to_csv("y_train.csv", index=False)
    y_test.to_csv("y_test.csv", index=False)

    return mean, stddev, pca



def logistic_regression():
    X_train = pd.read_csv("X_train.csv")
    y_train = pd.read_csv("y_train.csv")

    logr = LogisticRegression()
    logr.fit(X_train, y_train)
    return logr

def random_forest():
    X_train = pd.read_csv("X_train.csv")
    y_train = pd.read_csv("y_train.csv")

    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    return rf

def decision_tree():
    X_train = pd.read_csv("X_train.csv")
    y_train = pd.read_csv("y_train.csv")

    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)
    return dt

def knn():
    X_train = pd.read_csv("X_train.csv")
    y_train = pd.read_csv("y_train.csv")

    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)
    return knn


def accuracy(model):
    X_test = pd.read_csv("X_test.csv")
    y_test = pd.read_csv("y_test.csv")

    score = model.score(X_test, y_test)
    return score

def predict(x_vect, mean, stddev, model):
    x = (x_vect - mean) / stddev
    y = model.predict(x)
    return y


mean, stddev, pca = preprocess()
logr = logistic_regression()
rf = random_forest()
dt = decision_tree()
knn = knn()

print(accuracy(logr))
print(accuracy(rf))
print(accuracy(dt))
print(accuracy(knn))
x_vect = np.asarray([])

# print(predict(x_vect, mean, stddev, logr))




