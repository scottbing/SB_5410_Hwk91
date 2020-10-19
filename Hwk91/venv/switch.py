SQUARE = 2

class SwitchCase:

    # class constructor
    def __init__(self):
        self.a = 0
        self.b = 0
    #end constructor

    # evaluate operator
    def switch(self, oper):
        default = "Invalid option"
        return getattr(self, 'case_' + str(ord(oper)), lambda: default)()
    def case_43(self,):
        return self.a + self.b
    def case_45(self,):
        return self.a - self.b
    def case_42(self,):
        return self.a * self.b
    def case_47(self,):
        return self.a / self.b
    def case_94(self,):
        return pow(self.a, SQUARE)
    #end evaluate operator group


    # menu switch
    def menu(self, menu_option):
        default = "Invalid option"
        return getattr(self, 'item_' + str(menu_option), lambda: default)()
    def item_1(self):
        return "+  --> to add"
    def item_2(self,):
        return "-  --> to subtract"
    def item_3(self,):
        return "*  --> to multiply"
    def item_4(self,):
        return "/  --> to divide"
    def item_5(self,):
        return "^  --> to square"
    #end menu switch group

    # construct menu
    def menu(self, sw):
        # menus
        print("Calculator type your operation character: ")
        print(sw.item_1())
        print(sw.item_2())
        print(sw.item_3())
        print(sw.item_4())
        print(sw.item_5())
    # end def menu():

    # enter data
    def operation(self, ch, switcher):
        if ch == '^':
            self.a = int(input("Enter A:"))
        else:
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
    print("Ans:", ans)
#end def main():


if __name__ == '__main__':
    main()