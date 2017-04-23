from __future__ import print_function

# import unittest
# from base import selenium

from mymath import fac
import time

def test_fac_assert_equal(selenium):
    time.sleep(2)
    print('begin', selenium)
    assert fac(10) == 55
    print('end', selenium)

def test_fac_assert_true(selenium):
    print('begin', selenium)
    time.sleep(2)
    assert fac(10) == 55
    print('end', selenium)

# if __name__ == "__main__":
#     unittest.main()