import cmd, sys
from turtle import *

class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the AirBnB shell.   Type help or ? to list commands.\n'
    prompt = '(malik)'
    file = None

    # ----- basic AirBnB commands -----
    def do_amenity  (self, arg):
        
       
    def do_city(self, arg):
       
    def do_place(self, arg):
        
    def do_state(self, arg):
       
    def do_airbnb(self, arg): 
        
    def do_create(self, arg):
        
    def do_show (self, arg):
        
    def do_basemodel(self, arg):
        
    def do_eof(self, arg):
        
    def do_review(self, arg):

    def do_user(self, arg):

    def do_all(self, arg):

    def do_destroy(self, arg):

    def do_update(self, arg):
        
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