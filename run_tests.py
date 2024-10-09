import unittest
import xmlrunner
import os


if __name__ == '__main__':
    test_suite = unittest.TestLoader().discover(os.path.join('src','tests'))
    xmlrunner.XMLTestRunner(output='test-reports').run(test_suite)