#!/usr/bin/python3
""" this module is for the python console for the hbnb project"""
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import models


class HBNBCommand(cmd.Cmd):
    """ command processor console class for the airbnb"""
    prompt = "(hbnb) "
    __class_list = ["BaseModel", "Amenity", "City", "Place",
                    "Review", "State", "User"]
    __classes = {"BaseModel": BaseModel,
                 "Amenity": Amenity,
                 "City": City,
                 "Place": Place,
                 "Review": Review,
                 "State": State,
                 "User": User}

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id.
        """
        if not line:
            print("** class name missing")
        elif line not in self.__class_list:
            print("** class doesn't exist ** ")
        else:
            model = self.__classes[line]()
            model.save()
            print(model.id)

    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")

    def do_show(self, line):
        """
        Prints the string representation of an
        instance based on the class name and id."""
        if not line:
            print("** class name missing **")
            return
        args = line.split(" ")
        if args[0] not in self.__class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_all = models.storage.all()
            for k, v in obj_all.items():
                name = v.__class__.__name__
                obj_id = v.id
                if name == args[0] and obj_id == args[1]:
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)"""
        if not line:
            print("** class name missing **")
            return
        args = line.split(" ")
        if args[0] not in self.__class_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_all = models.storage.all()
            for k, v in obj_all.items():
                name = v.__class__.__name__
                obj_id = v.id
                if name == args[0] and obj_id == args[1]:
                    del obj_all[k]
                    models.storage.save()
                    return
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name"""
        if not line:
            obj = models.storage.all()
            lis = [obj[item].__str__() for item in obj]
            print(lis)
            return
        if line not in self.__class_list:
            print("** class doesn't exist **")
        else:
            obj = models.storage.all()
            ob_list = []
            for v in obj.values():
                if v.__class__.__name__ == line:
                    ob_list.append(v.__str__())
                    print(ob_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not line:
            print("** class name missing **")
            return
        args = line.split(" ")
        if args[0] not in self.__class_list:
            print("** class doesn't exist **")
            if len(args) < 2:
                print("** instance id missing **")
                obj = models.storage.all()
                for v in obj.values():
                    name = v.__class__.__name__
                    obj_id = v.id
                    if name == args[0] and obj_id == args[1]:
                        if len(args) < 3:
                            print("** attribute name missing **")
                        elif len(args) < 4:
                            print("** value missing **")
                        else:
                            setattr(v, args[2], args[3])
                            models.storage.save()
                        return
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
