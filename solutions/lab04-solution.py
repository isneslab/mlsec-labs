import sklearn.metrics as sm

# It is important to have y as a numpy array before doing this operation for the mask
mask_gw = (np.array(y)==0)
mask_mw = (np.array(y)==1)

## Dataset 1

mask_D1 = (mask_google & mask_gw) | (mask_else & mask_mw)

X_train, X_test, y_train, y_test = train_test_split(
    X[mask_D1], y[mask_D1], test_size=0.33, random_state=42)

clf = LinearSVC(C=1, dual=True, max_iter=10000)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)


print('D1 - Google Play vs Other Markets - F1: {:.2f}'.format(sm.f1_score(y_true=y_test, y_pred=y_pred)))


## Dataset 2

mask_D2 = mask_google

X_train, X_test, y_train, y_test = train_test_split(
    X[mask_D2], y[mask_D2], test_size=0.33, random_state=42)

clf = LinearSVC(C=1, dual=True, max_iter=10000)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

import sklearn.metrics as sm
print('D2 - Google Play only - F1: {:.2f}'.format(sm.f1_score(y_true=y_test, y_pred=y_pred)))