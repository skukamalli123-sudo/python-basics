class Abcd:
    def __init__(self):
        print("i am constractor")
        self.a = 10
        self.b = 20
    def hi(self):
        print("hi....")
    def addition(self):
        print(self.a + self.b)

abcd = Abcd()
abcd.addition()