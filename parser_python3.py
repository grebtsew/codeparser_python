from parser_abstract import parser


class parser_python3(parser):

    def __init__(self):
        #print('In the __init__ method of the Sub class before calling __init__ of the Base class')
        super().__init__()
        #print('In the __init__ method of the Sub class after calling __init__ of the Base class')


    def all_files(self, path=None, extension='.py'):
        '''
        Search for .py extension
        '''
        return super().all_files(path, extension)


    def parse(self, file_path):
        pass
