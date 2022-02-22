import unittest
from data import get_data

class TestLoadData(unittest.TestCase):

    def test_get_data(self):
        data = get_data()  # Act

        assert data == 1, "Data fetched correctly"

if __name__ == '__main__':
    unittest.main()
