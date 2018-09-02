import sys
import os
import threading
import time
import types
from subprocess import call
from generate_requirements_file import generate_requirements_file as gen_req


'''
This is our parse controller
This class controlls the program from the terminal
See commands and usage below
'''

class parse_controller(threading.Thread):

    func_info = (('help, h', 'show how to use all commands'),
                 ('helpsh', 'open python help shell'),
                 ('generate_requirements', 'Generates a requirements file, takes path and if there should use install testing'),
                 ('clear', 'clear terminal'),
                 ('documentation_check','Check that all functions, classes and files has been commented correctly. Also display functions and result.'),
                ('exit', 'exit program and all threads.'))

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        args = None
        input_str = "";
        print ("----- Program -----")
        print (" type help or h to see functions")
        while True:
            input_str = input('Program>')
            input_str_array = input_str.split(' ')
            if self.get_first_arg(input_str_array) is not None:
                if self.run_command(input_str_array):
                    pass
                else:
                    print("No command : " + input_str + " (for help type h)")

    def get_first_arg(self,arr):
        for s in arr:
            if len(s) > 0:
                return s
        return None


    def get_all_arg(self,arr):

        res = list()
        for s in arr:
            if len(s) > 0 :
                res.append(s)
        return res

    def run_command(self,arr):
        arg_arr = self.get_all_arg(arr);
        s = arg_arr[0]
        s = s.lower()

        if s == "help" or s == "h":
            self.call_help()
            return True
        elif s == "helpsh":
            help()
            pass
        elif s == "clear":
            self.call_clear()
            return True
        elif s == "exit":
            self.call_exit()
            return True
        elif s== "generate_requirements":
            self.call_generate_requirements(arg_arr)
            return True
        elif s== "documentation_check":
            self.call_documentation_check()
            return True
        else:
            return False

#
# --------- CALL FUNCTION DOWN HERE -----------
#
    def str2bool(self, v):
        return v.lower() in ("yes", "true", "t", "1")

    def call_documentation_check(self):
        pass

    def call_generate_requirements(self, args):
        if(len(args) == 1):
            inst = gen_req() # initiate requirements generator instance
             # using install test is great to make sure you only add correct packages
             # this will install all packages on your environment though!
            inst.start(install_test=True)
            #inst.test_requirements() # test install requirements
        else:
            if(len(args[1]) < 5):
                inst = gen_req()
            else:
                inst = gen_req(args[1])

            if(len(args) >= 3):
                inst.start(install_test=self.str2bool(args[2]))
            else:
                inst.start(install_test=False)

    def call_exit(self):
        os._exit(1)

    def call_help(self):
        print()
        print("This is program, see functions below. ")
        print()
        print("Help: ")
        for s in self.func_info:
            print( s[0]   + "\t\t" + s[1])
        print()

    def call_clear(self):
        os.system('cls' if os.name=='nt' else 'clear')
