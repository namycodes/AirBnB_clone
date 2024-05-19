#!/usr/bin/python3
"""
This python module defines a simple command interpreter
to be used as a console for managing the AirBnB project
"""
import cmd
import re
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for the cmd functions"""

    prompt = "(hbnb) "

    def precmd(self, line):
        """Handles what happens before the line on the command line is read"""
        
        if not line:
            return '\n'
        linePattern = re.compile(r"(\w+)\.(\w+)\((.*)\)")
        list_match = linePattern.findall(line)
        if not list_match:
            return super().precmd(line)
        match_tuple = list_match[0]
        if not match_tuple[2]:
            if match_tuple[1] == "count":
                instance_objs = storage.all()
                print(len([
                    v for _, v in instance_objs.items()
                    if type(v).__name__ == match_tuple[0]]))
                return "\n"
            return "{} {}".format(match_tuple[1], match_tuple[0])

    def do_quit(self, arg):
        """quit: Terminates the terminal"""
        return True

    def do_EOF(self, arg):
        """EOF: end of file- Exits the program"""
        print("")
        return True

    def emptyline(self, arg):
        """Overides the built in command for handling empty lines"""
        pass

    def do_help(self, arg):
        """To get help on a command type help <command>"""
        return super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
