from parser_python3 import parser_python3
import imp
import os
import subprocess

'''
This file contains code to investigate if file need to be fixed:
comment/code ratio
func and class names
'''

class file_investigator():

    parser_result_token_list = []
    class_list = []
    func_list = []
    all_files = []
    all_file_names = []
    path = None

    def reset_var(self):
        self.parser_result_token_list = []
        self.class_list = []
        self.func_list = []
        self.all_file_names = []
        self.all_files = []
        self.path = None

    def __init__(self, path=None):
        self.path = path
        self.reset_var()

    def start(self):
        # Create parser
        py_parser = parser_python3()
        self.all_files = py_parser.all_files(path=self.path)
        self.all_file_names = py_parser.all_files(path=self.path,soft=True)

        print("")
        print("Investigate all files in folder and subfolder")
        print("")

        # Get all files
        for s in self.all_files:
            #For each file
            self.parser_result_token_list.append(py_parser.parse_file(s))

        # Start investigation
        self.investigate()

    def investigate(self):
        k = 0
        comment_count= 0
        code_count= 0
        for file in self.parser_result_token_list:
            print("------------------------")
            print("Investigate file : " + self.all_files[k])
            k += 1
            for i in range(len(file[0])):

                #Definitions
                if(file[0][i][1] == "class"):
                    print("Class:" + str( file[0][i+1][1]))
                if(file[0][i][1] == "def"):
                    print("Function:" + str( file[0][i+1][1]))

                # Calcs
                if(file[0][i][0] == 1):
                    code_count += 1
                if(file[0][i][0] == 3 or file[0][i][0] == 57):
                    comment_count += 1

            print("Comment/code ratio in file: " + str(comment_count/code_count))
            print("Done with file")
            print("------------------------")
