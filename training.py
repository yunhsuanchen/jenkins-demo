import pandas as pd

from sklearn.tree import DecisionTreeClassifier

def train_model(train_df, test_df):
	X_train = [] #train_df.drop("Prediction_Class", axis = 1)
	Y_train = [] #train_df["Prediction_Class"]
	X_test = [] #test_df.drop("Id", axis = 1).copy()

	decision_tree = DecisionTreeClassifier()

	return [decision_tree, X_train, Y_train, X_test]