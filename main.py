from parser_python3 import parser_python3



def main():
    py_parser = parser_python3()


    for s in py_parser.all_files():
        print(s)




if __name__ == "__main__":
    main()
