from abc import ABC, abstractmethod
import os, os.path
import pathlib

class parser(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def all_files(self, path=None, extension=None):
        '''
        returns a list of all python file paths in directory and all subdirectories
        '''
        file_path_list = []
        root_dir = ""

        if(path is not None):
            root_dir = path
        else:
            root_dir = str(pathlib.Path(__file__).parent) + "\\"

        for path, dirs, files in os.walk(root_dir):
            for f in files:
                fullpath = os.path.join(path, f)
                if os.path.splitext(fullpath)[1] == extension:
                    file_path_list.append(fullpath)

        return file_path_list

    def parse_file(self, file_path):
        '''
        Parse a file and return the result
        '''

        # See that file exist


        # Start parse
        parse_result_list = []
        # For each row in file

        '''
        for line in file
            parse_result_list.append(self.parse_line(line))

        return parse_result_list

        '''
        pass

    @abstractmethod
    def parse_line(self, line):
        pass
