

class user_request():


    text = ""
    answer_list = []

    def __init__(self, text="", answer_list=[]):
        self.text = text
        if(len(answer_list ) <= 1):
            self.answer_list = ["y","n"]
        else:
            self.answer_list = answer_list

    def reset(self,text="", answer_list=[] ):
        self.text = text
        if(len(answer_list ) <= 1):
            self.answer_list = ["y","n"]
        else:
            self.answer_list = answer_list

    def request(self):
        print("")
        print("User Request")
        print("")
        print(self.text)
        print("")
        res = input("Input " + str(self.answer_list) + ": ")
        while res not in self.answer_list:
            res = input("Input " + str(self.answer_list) + ": ")
        return res
