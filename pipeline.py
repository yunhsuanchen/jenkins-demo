import pandas as pd

from sklearn.tree import DecisionTreeClassifier

from data import get_data
from preprocessing import preprocess_data
from training import train_model
from evaluation import evaluate_model_offline

get_data()

train_df, test_df = preprocess_data()

decision_tree, X_train, Y_train, X_test = train_model(train_df, test_df)

evaluate_model_offline(decision_tree, X_train, Y_train, X_test)