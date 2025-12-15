import os
import sys

import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import compute


def test_compute_default():
    x = np.arange(10)
    expected = x ** 2
    result = compute()
    assert np.array_equal(result, expected)


def test_compute_custom_n():
    n = 25
    x = np.arange(n)
    expected = x ** 2
    result = compute(n)
    assert np.array_equal(result, expected)
