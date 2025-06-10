import unittest
from cli.pizzapromptcli import PizzaPrompt

class TestCLI(unittest.TestCase):
    
    def test_start(self):
        PizzaPrompt.do_start(self, "start")
        self.assertTrue("Test Successful")
        
    def test_menu(self):
        PizzaPrompt.do_menu(self, "menu")
        self.assertTrue("Test Successful")
    
    def test_cancel(self):
        PizzaPrompt.do_cancel(self, "cancel")
        self.assertTrue("Test Successful")
        
    def test_quit(self):
        PizzaPrompt.do_quit(self, "quit")
        self.assertTrue("Test Successful")
        

if __name__ == '__main__':
    unittest.main()