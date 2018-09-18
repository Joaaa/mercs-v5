"""
Integration tests of test_algo_inference
"""


# Standard imports
import os
import numpy as np
import sys
from os.path import dirname


# Custom imports
root_directory = dirname(dirname(dirname(dirname(__file__))))
for dname in {'src'}:
    sys.path.insert(0, os.path.join(root_directory, dname))

from mercs.algo.inference import *
from mercs.utils.utils import encode_attribute

import datasets as ds
from sklearn.preprocessing import Imputer


def test_perform_imputation():
    # Prelims
    train, test = ds.load_nursery()
    query_code = [0, -1, -1, -1, -1, -1, 0, 0, 1]

    imputator = Imputer(missing_values='NaN',
                        strategy='most_frequent',
                        axis=0)
    imputator.fit(train)

    # Actual test
    obs = perform_imputation(test, query_code, imputator)

    assert test.shape == obs.shape
    assert isinstance(obs, np.ndarray)

    boolean_missing = missing_attribute_encoding

    for row in obs[:, boolean_missing].T:
        assert len(np.unique(x)) == 1