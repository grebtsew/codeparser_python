from parser_python3 import parser_python3
import imp
import os
import subprocess

class generate_requirements_file():

    parser_result_token_list = []
    import_list = []
    all_files = []
    all_file_names = []
    path = None
    install_test = False

    def reset_var(self):
        self.parser_result_token_list = []
        self.import_list = []
        self.all_file_names = []
        self.all_files = []
        self.install_test = False

    def __init__(self, path=None):
        self.path = path
        self.reset_var()

    def start(self, install_test=False):
        # Create parser
        self.install_test = install_test
        py_parser = parser_python3()
        self.all_files = py_parser.all_files(path=self.path)
        self.all_file_names = py_parser.all_files(path=self.path,soft=True)

        print("")
        print("Parse all files")
        print("")

        # Get all files
        for s in self.all_files:
            #For each file
            self.parser_result_token_list.append(py_parser.parse_file(s))

        print("")
        print("Get imports")
        print("")


        # Convert imports
        self.update_imports()

        print("")
        print("Generate requirements file")
        print("")

        # Generate requirements file
        self.generate()

        # Show result
        print("")
        print("Resulting imports that will be written to requirements.txt : ")
        for imp in self.import_list:
            print(imp)
        print("")


    def update_imports(self):
        '''
        Update import list and check that not same imports are added.
        '''
        k = 0
        for file in self.parser_result_token_list:

            print("Imports from file : " + self.all_files[k])
            k += 1
            for i in range(len(file[0])):
                # Is an import row
                if(file[0][i][1] == "import"):

                    # last element
                    if(len(file[0]) <= i+1):
                        continue

                    # Check for from
                    if(i-2 >= 0):

                        # if from check if its a file or other import
                        if file[0][i-2][1] != "from":
                            self.add_to_import_list(file[0][i+1][1])
                        else:

                            #is file
                            if not self.is_a_file(file[0][i-1][1]):
                                self.add_to_import_list(file[0][i-1][1])
                            #is an existing package
                                if self.package_exist(file[0][i-1][1]):
                                    self.add_to_import_list(file[0][i-1][1])
                                elif self.package_exist(file[0][i+1][1]):
                                    self.add_to_import_list(file[0][i+1][1])
                    else:
                            self.add_to_import_list(file[0][i+1][1])

    def is_a_file(self, package):
        return str(package+".py") in self.all_file_names

    def package_exist(self, package):
        try:
            imp.find_module(package)
            # package exist
            return True
        except ImportError:
            return False

    def add_to_import_list(self, element):
        print(element)
        if element not in self.import_list:
            if self.install_test:
                print("Install test of package : " + element)
                if self.test_package(element):
                    self.import_list.append(element)
            else:
                self.import_list.append(element)

    def generate(self):
        '''
        Generate new requirements file and write imports
        '''
        print("Creates requirements.txt")
        with open('requirements.txt', 'w+') as out:
            if(len(self.import_list) <= 0):
                print("No imports found.")
                return
            for impor in self.import_list:
                out.write(impor + '\n')
            print("requirements.txt created successfully!")
            print("Always check the result, and add your current versions if needed!")

    def test_requirements(self):
        subprocess.check_call("pip install -r requirements.txt",shell=True)

    def test_package(self, package):
        try:
            subprocess.check_call("pip install "+ package ,shell=True)
            return True
        except:
            return False
