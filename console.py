#!/usr/bin/python3
import cmd
from models import *
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    valid_classes = ["BaseModel", "User", "State",
                     "City", "Amenity", "Place", "Review"]

    def emptyline(self):
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        quit()

    def do_EOF(self, args):
        """Ctrl + D to exit program"""
        print("")
        return True

    def do_create(self, args):
        """
        Creates a model of a given classname.

        Supports optional arguments for setting attributes on creation.

        Syntax: create <classname> <arg1> <arg2> <arg3>

        Arguments must contain an "=" and be formatted like so:
        string="hello" float=6.36 int=27
        """
        args = args.split(' ')
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] in HBNBCommand.valid_classes:
            cname = args[0]
            kwrg = {}
            for arg in args[1:]:
                try:
                    key = arg.split('=')[0]
                    value = arg.split('=')[1]
                    if value[0] == '"' and value[-1] == '"':
                        value = str(value)
                        value = value.replace("_", " ")
                        value = value[1:-1]
                    elif "." in value:
                        value = float(value)
                    else:
                        value = int(value)
                    setattr(self, key, value)
                    kwrg[key] = value
                except:
                    continue
            new_obj = eval(cname)(**kwrg)
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Usage: show BaseModel 1234-1234-1234"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        for objs_id in all_objs.keys():
            if objs_id == args[1] and args[0] in str(type(all_objs[objs_id])):
                print(all_objs[objs_id])
                return
        print("** no instance found **")

    def do_destroy(self, args):
        """Usage: destroy BaseModel 1234-1234-1234"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        try:
            if all_objs[args[1]] and args[0] in str(type(all_objs[args[1]])):
                storage.delete(all_objs[args[1]])
                storage.save()
                return
        except:
            print("** no instance found **")

    def do_all(self, args):
        """Usage: all Basemodel or all"""
        if args not in HBNBCommand.valid_classes and len(args) != 0:
            print("** class doesn't exist **")
            return
        elif args in HBNBCommand.valid_classes:
            all_objs = {k: v for (k, v) in storage.all().items()
                        if isinstance(v, eval(args))}
        elif len(args) == 0:
            all_objs = storage.all()
        else:
            return
        for objs_id in all_objs.keys():
            print(all_objs[objs_id])

    def do_update(self, args):
        """Use: update <class name> <id> <attribute name> <attribute value>"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if obj_id == args[1]:
                setattr(all_objs[obj_id], args[2], args[3])
                storage.save()
                return
        print("** no instance found **")

    def do_User(self, args):
        """Usages:
        User.all() - displays all objects of class User
        User.count() - displays number of objects of class User
        User.show(<id>) - displays object of class User with id
        User.destroy(<id>) - deletes object of class User with id
        User.update(<id>, <attribute name>, <attribute value>) - update User
        User.update(<id>, <dictionary representation>) - update User
        """
        self.class_exec('User', args)

    def do_BaseModel(self, args):
        """Usages:
        BaseModel.all() - displays all objects of class BaseModel
        BaseModel.count() - displays number of objects of class BaseModel
        BaseModel.show(<id>) - displays object of class BaseModel with id
        BaseModel.destroy(<id>) - deletes object of class BaseModel with id
        BaseModel.update(<id>, <attribute name>, <attribute value>) - update
        BaseModel.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('BaseModel', args)

    def do_State(self, args):
        """Usages:
        State.all() - displays all objects of class State
        State.count() - displays number of objects of class State
        State.show(<id>) - displays object of class State with id
        State.destroy(<id>) - deletes object of class BaseModel with id
        State.update(<id>, <attribute name>, <attribute value>) - update
        State.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('State', args)

    def do_City(self, args):
        """Usages:
        City.all() - displays all objects of class City
        City.count() - displays number of objects of class City
        City.show(<id>) - displays object of class City with id
        City.destroy(<id>) - deletes object of class City with id
        City.update(<id>, <attribute name>, <attribute value>) - update
        City.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('City', args)

    def do_Amenity(self, args):
        """Usages:
        Amenity.all() - displays all objects of class Amenity
        Amenity.count() - displays number of objects of class Amenity
        Amenity.show(<id>) - displays object of class Amenity with id
        Amenity.destroy(<id>) - deletes object of class Amenity with id
        Amenity.update(<id>, <attribute name>, <attribute value>) - update
        Amenity.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Amenity', args)

    def do_Place(self, args):
        """Usages:
        Place.all() - displays all objects of class Place
        Place.count() - displays number of objects of class Place
        Place.show(<id>) - displays object of class Place with id
        Place.destroy(<id>) - deletes object of class Place with id
        Place.update(<id>, <attribute name>, <attribute value>) - update
        Place.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Place', args)

    def do_Review(self, args):
        """Usages:
        Review.all() - displays all objects of class Review
        Review.count() - displays number of objects of class Review
        Review.show(<id>) - displays object of class Review with id
        Review.destroy(<id>) - deletes object of class Review with id
        Review.update(<id>, <attribute name>, <attribute value>) - update
        Review.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Review', args)

    def class_exec(self, cls_name, args):
        """Wrapper function for <class name>.action()"""
        if args[:6] == '.all()':
            self.do_all(cls_name)
        elif args[:6] == '.show(':
            self.do_show(cls_name + ' ' + args[7:-2])
        elif args[:8] == ".count()":
            all_objs = {k: v for (k, v) in storage.all().items()
                        if isinstance(v, eval(cls_name))}
            print(len(all_objs))
        elif args[:9] == '.destroy(':
            self.do_destroy(cls_name + ' ' + args[10:-2])
        elif args[:8] == '.update(':
            if '{' in args and '}' in args:
                new_arg = args[8:-1].split('{')
                new_arg[1] = '{' + new_arg[1]
            else:
                new_arg = args[8:-1].split(',')
            if len(new_arg) == 3:
                new_arg = " ".join(new_arg)
                new_arg = new_arg.replace("\"", "")
                new_arg = new_arg.replace("  ", " ")
                self.do_update(cls_name + ' ' + new_arg)
            elif len(new_arg) == 2:
                try:
                    dict = eval(new_arg[1])
                except:
                    return
                for j in dict.keys():
                    self.do_update(cls_name + ' ' + new_arg[0][1:-3] + ' ' +
                                   str(j) + ' ' + str(dict[j]))
            else:
                return
        else:
            print("Not a valid command")

if __name__ == '__main__':
        HBNBCommand().cmdloop()
