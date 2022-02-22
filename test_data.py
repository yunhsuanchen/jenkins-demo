import unittest
from data import get_data

class TestLoadData(unittest.TestCase):

    def test_get_data(self):
        data = get_data()  # Act

        assert(data is 1)

if __name__ == '__main__':
    unittest.main()