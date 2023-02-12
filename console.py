import cmd, sys
from turtle import *

class TurtleShell(cmd.Cmd):
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
        'Create a BaseModel'
        print('BaseModel')
        
    def do_show (self, arg):
        'Show a BaseModel'
        print('BaseModel')
        
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
        'Create a User'
        print('User')

    def do_all(self, arg):
        'Prints all string representation of all instances based or not on the class name'
        print('all')

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id'
        print('destroy')

    def do_update(self, arg):
        'Updates an instance based on the class name and id by adding or updating attribute'
        print('update')

    
        
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
    TurtleShell().cmdloop()