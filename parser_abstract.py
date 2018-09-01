from abc import ABC, abstractmethod
import os, os.path
import pathlib

class parser(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def all_files(self, path=None, extension=None, soft=False):
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
                    if soft:
                        file_path_list.append(f)
                    else:
                        file_path_list.append(fullpath)

        return file_path_list

    def parse_file(self, file_path):
        '''
        Parse a file and return the result
        '''
        content = []
        try:
            with open(file_path) as file:
                content.append( self.parse(file.readline))
        except:
            print("Error in parse_file: "+file_path+" can't be opened!")

        return content

    @abstractmethod
    def parse(self, readline):
        pass
