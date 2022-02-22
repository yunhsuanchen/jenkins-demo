import pandas as pd

def evaluate_model_offline(decision_tree, X_train, Y_train, X_test):
	#decision_tree.fit(X_train, Y_train)
	Y_pred = [] #decision_tree.predict(X_test)
	acc_decision_tree = 26 #round(decision_tree.score(X_train, Y_train) * 100, 2)

	metric1 = {'metric1': [12]}
	metric2 = {'metric2': [20]}

	metric1_df = pd.DataFrame(data=metric1)
	metric2_df = pd.DataFrame(data=metric2)
	metric1_df.to_csv('plot_metric1.csv', index = False)
	metric2_df.to_csv('plot_metric2.csv', index = False)

	print(acc_decision_tree)