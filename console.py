#!/usr/bin/python3
"""
This python module defines a simple command interpreter
to be used as a console for managing the AirBnB project
"""
import cmd
import re
from models import storage
from models.review import Review
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models import BaseModel


available_classes = {'BaseModel': BaseModel, 'User': User,
                   'Amenity': Amenity, 'City': City, 'State': State,
                   'Place': Place, 'Review': Review}

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

    def emptyline(self):
        """Overides the built in command for handling empty lines"""
        pass

    def do_help(self, arg):
        """To get help on a command type help <command>"""
        return super().do_help(arg)
    
    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_obj = available_classes[arg]()
                new_obj.save()
                print(new_obj.id)
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self,arg):
        """Prints string representation on an instance"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return False
        if args[0] not in available_classes.keys():
            print("** class doesn't exist **")
            return False
        if len(args) < 2 and args[1]:
            print("** instance id missing **")
            return False
        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        print(req_instance)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
