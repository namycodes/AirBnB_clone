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
        tuple_matcher = list_match[0]
        if not tuple_matcher[2]:
            if tuple_matcher[1] == "count":
                instance_objs = storage.all()
                print(len([
                    v for _, v in instance_objs.items()
                    if type(v).__name__ == tuple_matcher[0]]))
                return "\n"
            return "{} {}".format(tuple_matcher[1], tuple_matcher[0])
        else:
            args = tuple_matcher[2].split(", ")
            if len(args) == 1:
                return "{} {} {}".format(
                    tuple_matcher[1], tuple_matcher[0],
                    re.sub("[\"\']", "", tuple_matcher[2]))
            else:
                match_json = re.findall(r"{.*}", tuple_matcher[2])
                if (match_json):
                    return "{} {} {} {}".format(
                        tuple_matcher[1], tuple_matcher[0],
                        re.sub("[\"\']", "", args[0]),
                        re.sub("\'", "\"", match_json[0]))
                return "{} {} {} {} {}".format(
                    tuple_matcher[1], tuple_matcher[0],
                    re.sub("[\"\']", "", args[0]),
                    re.sub("[\"\']", "", args[1]), args[2])

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
