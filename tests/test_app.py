import numpy as np
from app import compute

def test_compute():
    x = np.arange(10)
    expected = x ** 2
    result = compute()
    assert np.array_equal(result, expected)