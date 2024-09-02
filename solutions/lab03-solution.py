from tqdm.notebook import tqdm
import matplotlib.pyplot as plt

# ################
## Exercise 1
# ################

# Attacking a single point
tp_mask = (y_pred==1.0) & (y_test==1.0)
X_tps = X_test[tp_mask,:]

test_point = X_tps[0].toarray()
print('Before attack: {}'.format(clf.predict(test_point)))
top_10_benign_idx = np.argsort(clf.coef_[0])[:10]
test_point[:, top_10_benign_idx] = 1.0
print('After attack: {}'.format(clf.predict(test_point)))

# ################
## Exercise 2
# ################

asr = []
for top_n in tqdm(range(11)):
    y_before = []
    y_after = []
    X_tps = X_test[tp_mask,:]
    print('Attacking {} tps with {} top benign...'.format(np.sum(tp_mask), top_n))
    top_10_benign_idx = np.argsort(clf.coef_[0])[:top_n]
    for test_point in X_tps:
        y_before.append(clf.predict(test_point)[0])
        test_point[:, top_10_benign_idx] = 1.0
        y_after.append(clf.predict(test_point)[0])
    y_before = np.array(y_before)
    y_after = np.array(y_after)
    asr.append(np.sum((y_before==1.0) & (y_after==0.0))/len(y_before))


# Plot the security evaluation curve
print('ASR: {}'.format(asr))
plt.xlabel('Pertubation')
plt.ylabel('Attack Success Rate (1-Recall)')
plt.plot(asr, marker='x')
plt.ylim([0,1.1])
plt.grid()