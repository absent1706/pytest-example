from __future__ import print_function

# import unittest
# from base import selenium


from mymath import fac

def test_fac_assert_equal(selenium):
    print('begin', selenium)
    assert fac(10) == 55
    print('end', selenium)

def test_fac_assert_true(selenium):
    print('begin', selenium)
    assert fac(10) == 55
    print('end', selenium)

# if __name__ == "__main__":
#     unittest.main()