import unittest
from cli.pizzapromptcli import PizzaPrompt

class TestCLI(unittest.TestCase):
    
    def test_start(self):
        PizzaPrompt.do_start(self, "start")
        
    def test_menu(self):
        PizzaPrompt.do_menu(self, "menu")
    
    def test_cancel(self):
        PizzaPrompt.do_cancel(self, "cancel")
        
    def test_quit(self):
        PizzaPrompt.do_quit(self, "quit")
        

if __name__ == '__main__':
    unittest.main()