import unittest
import sys

sys.path.append('..')
from main import printusage

class Testing(unittest.TestCase):
    def test_printusage(self):
        result = printusage()
        expectedresult = "Usage:"
        expectedresult += "test.py -i <number of instance> -l <length of play time>"
        expectedresult += "Options:"
        expectedresult += "-i, --inst       : specify number of docker instance to run"
        expectedresult += "-l, --lplay      : specify length of play time to run in minutes"
        expectedresult += "-u, --url        : specify url page or first landing page"
        expectedresult += "self.assertEqual(result,expectedresult)"


if __name__ == '__main__':
    unittest.main()
