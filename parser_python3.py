from parser_abstract import parser
import tokenize

class parser_python3(parser):

    '''
    parser for python3 code using tokenize
    '''
    next_import = False
    imports = []
    functions = []

    def __init__(self):
        super().__init__()

    def all_files(self, path=None, extension='.py', soft=False):
        '''
        Search for .py extension
        '''
        return super().all_files(path, extension, soft)

    def parse(self, readline):
        result = []
        g = tokenize.generate_tokens(readline)   # tokenize the string
        for toknum, tokval, _, _, _  in g:

            if toknum == 0: # Null
                pass
            elif toknum == 1: # Code & words
                result.append((toknum, tokval))
            elif toknum == 2: # Number
                pass
            elif toknum == 3: # Comments
                result.append((toknum, tokval))
            elif toknum == 4: # New line
                pass
            elif toknum == 5: # Space
                pass
            elif toknum == 6: # Space
                pass
            elif toknum == 53: # Symbols ():_.,
                pass
            elif toknum == 57: # Comments
                result.append((toknum, tokval))
            elif toknum == 58: # New line
                pass
            else:
                print("Unknown token number " + str(toknum) + " is undefiened. Value: " + str(tokval))

        return result
