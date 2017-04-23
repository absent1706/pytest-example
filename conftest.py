from __future__ import print_function
# import unittest
import pytest

@pytest.fixture(scope='session')
def selenium(request):
    print('BEGIN fixture')
    # yield 123
    request.addfinalizer(lambda: print('END fixture'))
    return 123

