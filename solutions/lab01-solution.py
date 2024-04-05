from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import sklearn.ensemble
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/big_dataset.csv')
X = df.drop('mw_family',axis=1)
y = df['mw_family']

# I am splitting the model into training and testing
X_train, X_test, y_train, y_true = train_test_split(
    X, y, test_size=0.2, random_state=22)

# The matplotlib.pyplot library (here referred to with the alias "plt"), is used for plotting
plt.style.use('ggplot')
# changing the xlabel
plt.xlabel('fpr')
# changing the ylabel
plt.ylabel('tpr')

# I am fitting with two kernels
for k in ['linear','rbf']:

    # I am instantiating the linear classifier
    clf = SVC(kernel=k, C=1).fit(X_train, y_train)
    y_test = clf.predict(X_test)
    y_score = clf.fit(X_train, y_train).decision_function(X_test)
    fpr, tpr, thresholds = sklearn.metrics.roc_curve(y_true, y_score, pos_label=1)
    plt.plot(fpr,tpr,label=k)

# Random Forest    
clf = sklearn.ensemble.RandomForestClassifier(n_estimators=100).fit(X_train, y_train)
y_test = clf.predict(X_test)
y_score = clf.fit(X_train, y_train).predict_proba(X_test)[:,1]
fpr, tpr, thresholds = sklearn.metrics.roc_curve(y_true, y_score, pos_label=1)
plt.plot(fpr,tpr,label='rf')


plt.legend()