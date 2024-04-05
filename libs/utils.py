import datetime
import json
import numpy as np
import pickle
from sklearn.feature_extraction import DictVectorizer

def load_X(dataset_path, reduced=False):
    print("Loading data (feature representation X, and feature names)...")
    # Load the reduced 10k features
    if reduced:
        with open('{}/X-10k.p'.format(dataset_path), 'rb') as f:
            X = pickle.load(f)
        with open('{}/f-10k.p'.format(dataset_path), 'rb') as f:
            feature_names = pickle.load(f)
    else:
        with open('{}/X.json'.format(dataset_path), 'r') as f:
            X = json.load(f)

        # Convert to numpy array and get feature names
        vec = DictVectorizer()
        X = vec.fit_transform(X).astype("float32")
        feature_names = vec.get_feature_names_out()

    return X, feature_names


def load_y(dataset_path):
    print('Loading labels...')
    with open('{}y.json'.format(dataset_path), 'rt') as f:
        y = json.load(f)
    y = np.asarray(y)
    return y


def load_metadata(dataset_path):
    print('Loading metadata...')
    with open('{}meta.json'.format(dataset_path), 'rt') as f:
        metadata = json.load(f)
    return metadata

def load_time_index(dataset_path):
    with open('{}meta.json'.format(dataset_path), 'rt') as f:
        T = json.load(f)
        T = [o['dex_date'] for o in T]
        T = np.array([datetime.datetime.strptime(o, '%Y-%m-%dT%H:%M:%S') if "T" in o
             else datetime.datetime.strptime(o, '%Y-%m-%d %H:%M:%S') for o in T])
    return T