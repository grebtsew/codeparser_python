from parser_python3 import parser_python3
from generate_requirements_file import generate_requirements_file as gen_req

'''
Run and test implementation from this file
'''

def main():
    test_generate_requirements()

def test_parser():
    # Create instance of parser for python3 code
    py_parser = parser_python3()

    # Print the parse result from all files in directories and subdirectories
    for s in py_parser.all_files():
        print(py_parser.parse_file(s))

def test_generate_requirements():
    inst = gen_req() # initiate requirements generator instance

     # using install test is great to make sure you only add correct packages
     # this will install all packages on your environment though!
    inst.start(install_test=True)
    #inst.test_requirements() # test install requirements

if __name__ == "__main__":
    main()
