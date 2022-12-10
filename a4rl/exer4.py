from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


numRuns = 10

X, y = load_iris(return_X_y=True)

for i in range(numRuns):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    gnb = GaussianNB()
    y_pred = gnb.fit(X_train, y_train).predict(X_test)

    print("numero de previsões falhadas em %d = %d" % (X_test.shape[0], (y_test != y_pred).sum()))
    

