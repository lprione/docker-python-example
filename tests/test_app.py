import os
import sys
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import compute


def test_compute():
    x = np.arange(10)
    expected = x ** 2
    result = compute()
    assert np.array_equal(result, expected)