from tesseract import evaluation, temporal, metrics 

# Load time index (X and y were loaded earlier in the notebook)
T = libs.utils.load_time_index(dataset_path)

splits = temporal.time_aware_train_test_split(
    X, y, T, train_size=12, test_size=1, granularity='month')

# Perform a time-aware evaluation
clf = LinearSVC(C=1)
results = evaluation.fit_predict_update(clf, *splits)
metrics.print_metrics(results)

# Create plots
from pylab import *

pendleblue='#1f8fff'
pendleyellow='#ffa600'

# '#FF9999', '#FFDD99', '#AAEEEE'
plot(results['precision'], marker='o', color=pendleyellow)
plot(results['recall'], marker='o', color='red')
plot(results['f1'], marker='o', color=pendleblue)
legend(['Precision', 'Recall', 'F1'])
# You may use xlim to limit the months
# xlim([0,23])
xlabel('Testing period (month)')
ylabel('Performance')
grid(axis = 'y')

# you can use "savefig" to save the figures in png, or add comparisons. 
show()