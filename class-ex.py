class Abcd:
    # constructor wot the parameter name and email
    def __init__(self,name,email):
        print(" i am constructor")
        self.firstname = name
        #self.firstname is instance variable

        self.email = email 

    def print_all_info(self):
        print("hi",len(self.firstname))
        print(self.email.upper())
        print(self.email[0:1])
        marks = 100
        salary = 10000
        msg = f"my name is {self.firstname} and my salary is {salary} and marks is {marks}" 
        print(msg)
abcd = Abcd("hello world","asdf@gmail.com")
abcd.print_all_info()
