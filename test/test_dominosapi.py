import unittest
from api.dominosapi import DominosAPI

class TestDominosAPI(unittest.TestCase):
    def test_callapi(self):
        menu = DominosAPI.callapi(self)
        self.assertIsNotNone(menu, "The result should not be None")
        

if __name__ == '__main__':
    unittest.main()