import cmd, sys
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to the AirBnB shell.   Type help or ? to list commands.\n'
    prompt = '(malik)'
    file = None

    # ----- basic AirBnB commands -----
    def do_amenity  (self, arg):
        'Create an Amenity'
        print('Amenity')       
       
    def do_city(self, arg):
        'Create a City'
        print('City')
       
    def do_place(self, arg):
        'Create a Place'
        print('Place')
        
    def do_state(self, arg):
        'Create a State'
        print('State')
       
    def do_airbnb(self, arg): 
        'Create an AirBnB'
        print('AirBnB')
        
    def do_create(self, arg):
        'Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id '
        if arg == '':
            print('** class name missing **')
        elif arg != 'BaseModel':
            print('** class doesn\'t exist **')
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)        
    def do_show (self, arg):
        'Prints the string representation of an instance based on the class name and id'
        if arg == '':
            print('** class name missing **')
        elif arg != 'BaseModel':
            print('** class doesn\'t exist **')
        elif arg.find(' ') == -1:
            print('** instance id missing **')
        elif arg.id != 'BaseModel':
            print('** no instance found **')
        else:
            obj = BaseModel()
            obj.__str__()
            print(obj)

    def do_basemodel(self, arg):
        'Create a BaseModel'
        print('BaseModel')
        
    def do_eof(self, arg):
        'Exit the console'
        print('Thank you for using AirBnB')     
        return -1
        
    def do_review(self, arg):
        'Create a Review'
        print('Review')

    def do_user(self, arg):

            

    def do_all(self, arg):
        'Prints all string representation of all instances based or not on the class name'
        if arg == '':
            print('** class name missing **')
        elif arg != 'BaseModel':
            print('** class doesn\'t exist **')
        else:
            obj = BaseModel()
            obj.__str__()
            for i in obj:
                print(i)
            

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id (save the change into the JSON file).'
        if arg == '':
            print('** class name missing **')
        elif arg != 'BaseModel':
            print('** class doesn\'t exist **')
        elif arg.find(' ') == -1:
            print('** instance id missing **')
        elif arg.id != 'BaseModel':
            print('** no instance found **')
        else:
            obj = BaseModel()
            obj.delete()

    def do_update(self, arg):
        'Updates an instance based on the class name and id by adding or updating attribute'
        if arg == '':
            print('** class name missing **')
        elif arg != 'BaseModel':
            print('** class doesn\'t exist **')
        elif arg.find(' ') == -1:
            print('** instance id missing **')
        elif arg.id != 'BaseModel':
            print('** no instance found **')
        elif arg.find(' ') == -1:
            print('** attribute name missing **')
        elif arg.find(' ') == -1:
            print('** value missing **')
        else:
            arg = arg.split()
            arg[1] = arg[1].replace('"', '')
            arg[2] = arg[2].replace('"', '')
            obj = BaseModel()
            obj.__dict__[arg[1]] = arg[2]
            obj.save()
            obj.__str__()
            print(obj)       
    
        
    def do_quit(self, arg):
        'Prints a farewell message and exits the console'
        print('Thank you for using AirBnB')     
        return -1
  
    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
