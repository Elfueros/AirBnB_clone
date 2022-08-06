#!/usr/bin/python3
"""console : entry point to the commad interpreter
It defines a custom shell to control the airbnb application
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Definition of the custom shell command interpreter
    Attributes:
        /* public class attributes */
        intro (str) : the message that is print at the launch of the console
        prompt (str) : the prompt on every line of the console
        file () : i don't know
    Functions:
        /* public instance methods */
        help()
        quit()
        EOF()
        emptyline()
    """

    intro = "Welcome to HBNB console."
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Command quit : exits the console
        """
        return (True)

    def do_EOF(self, arg):
        """Command EOF : exits the console
        """
        return (True)

    def emptyline(self):
        """does nothing when an empty line is entered
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
