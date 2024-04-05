## Dataset 1

mask_D1 = (mask_google & mask_gw) | (mask_else & mask_mw)

X_train, X_test, y_train, y_test = train_test_split(
    X[mask_D1], y[mask_D1], test_size=0.33, random_state=42)

clf = LinearSVC(C=1)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

import sklearn.metrics as sm
sm.f1_score(y_true=y_test, y_pred=y_pred)


## Dataset 2

mask_D2 = mask_google

X_train, X_test, y_train, y_test = train_test_split(
    X[mask_D2], y[mask_D2], test_size=0.33, random_state=42)

clf = LinearSVC(C=1)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

import sklearn.metrics as sm
sm.f1_score(y_true=y_test, y_pred=y_pred)