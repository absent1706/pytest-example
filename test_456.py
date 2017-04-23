from __future__ import print_function

# import unittest
# from base import selenium


from mymath import fib

def test_fib_assert_equal(selenium):
    print('begin', selenium)
    selenium.AAA()
    assert fib(10) == 55
    print('end', selenium)

def test_fib_assert_true(selenium):
    print('begin', selenium)
    assert fib(10) == 55
    print('end', selenium)

# if __name__ == "__main__":
#     unittest.main()