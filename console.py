#!/usr/bin/python3
import cmd
import re
class HBNBCommand(cmd.Cmd):
    """Class for the cmd functions"""
    prompt = "(hbnb) "
    def precmd(self,line):
        """Handles what happens before the line on the command line is read"""
        if not line:
            return '\n'
        pattern = re.compile(r"(\w+)\.(\w+)\((.*)\)")
        match_list = pattern.findall(line)
        if not match_list:
            return super().precmd(line)

        match_tuple = match_list[0]
        if not match_tuple[2]:
            if match_tuple[1] == "count":
                instance_objs = storage.all()
                print(len([
                    v for _, v in instance_objs.items()
                    if type(v).__name__ == match_tuple[0]]))
                return "\n"
            return "{} {}".format(match_tuple[1], match_tuple[0])
        else:
            def do_quit(self,arg):
                """quit: Exits the terminal"""
                return True
            def do_EOF(self,arg):
                """EOF: end of file- Exits the program"""
                return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()
