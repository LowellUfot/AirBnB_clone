#!/usr/bin/python3
""" this module is for the python console for the hbnb project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ command processor console class for the airbnb"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
