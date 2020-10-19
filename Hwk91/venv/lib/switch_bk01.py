class SwitchCase:

    def __init__(self):
        self.a = 0
        self.b = 0

    # begin math switcher functions
    def add(self, a, b):
        return self.a + self.b

    def sub(a, b):
        return self.a - self.b

    def mul(a, b):
        return self.a * self.b

    def div(a, b):
        return self.a / self.b

    def sqr(a, b=2):
        return pow(a, b)

    # end math switcher functions

    def switch(self, dayOfWeek):
        default = "Invalid option"
        return getattr(self, 'case_' + str(dayOfWeek), lambda: default)()
    def case_1(self):
        return self.a + self.b
    def case_2(self,):
        return "2.) -"
    def case_3(self,):
        return "3.) *"
    def case_4(self,):
        return "4.) /"
    def case_5(self,):
        return "5.) ^"

    # menu
    def menu(self, dayOfWeek):
        default = "Invalid option"
        return getattr(self, 'item_' + str(dayOfWeek), lambda: default)()
    def item_1(self):
        return "1.) +"
    def item_2(self,):
        return "2.) -"
    def item_3(self,):
        return "3.) *"
    def item_4(self,):
        return "4.) /"
    def item_5(self,):
        return "5.) ^"


    def menu(self, sw):
        # menus
        print("Calculator type your operation: ")
        print(sw.item_1())
        print(sw.item_2())
        print(sw.item_3())
        print(sw.item_4())
        print(sw.item_5())
    # end def menu():

    def operation(self, ch, switcher):
        self.a = int(input("Enter A:"))
        self.b = int(input("Enter B:"))

        #return switcher.get(ch, "Invalid option chosen")
        return switcher.switch(ch)
# end def operation(ch):

def main():
    sw = SwitchCase()
    sw.menu(sw)
    ch = input("Enter Choice(1-4): ")
    ans = sw.operation(ch, sw)
    print(ans)


if __name__ == '__main__':
    main()