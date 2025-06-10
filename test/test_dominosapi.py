import unittest
from api.dominosapi import DominosAPI

class TestDominosAPI(unittest.TestCase):
    def test_callapi(self):
        menu = DominosAPI.callapi(self)
        self.assertIsNotNone(menu, "The result should not be None")
    
    def test_callapi_no_conn(self):
        menu = DominosAPI.callapi(self)
        self.assertIsNotNone(menu, "Test Successful")
        
    def test_callapi_fail(self):
        menu = DominosAPI.callapi(self)
        self.assertIsNotNone(menu, "Test Successful")
        

if __name__ == '__main__':
    unittest.main()