#import sys sys.path.append('/pizzaprompt/shared')
import cmd
from api.dominosapi import DominosAPI

class PizzaPrompt(cmd.Cmd):
    prompt = 'PizzaPrompt>> '
    intro = 'Welcome to PizzaPrompt. Type "help" for available commands.'

    def do_start(self, line):
        """Start the Order, please choose your order options: """

    def do_menu(self, line):
        """Available Menu List: """
        print("Available Menu List:")
        api = DominosAPI()
        menu = api.callapi()
        for value in menu:
            print(value._meta.name)
    
    def do_cancel(self, line):
        """Cancel the Order."""
        print("Order Cancelled...")
        return True
    
    def do_quit(self, line):
        """Exit the PizzaPrompt."""
        return True
    
    def postcmd(self, stop, line):
        print() 
        return stop

if __name__ == "__main__":
    PizzaPrompt().cmdloop()