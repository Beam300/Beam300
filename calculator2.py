import sys
class Calculator:
    def __init__(self):
        self.name = 'casnio'
        self.math()

    def math(self): 
        print(f"{self.name} Calculator".center(100)) 

        self.val1 = float(input("enter val1: "))
        self.val2 = float(input("enter val2: "))

        print(f""" 
    
        select your option
        1.  addition
        2.  substration
        """)
        user = input("your option: ")  
        if user =="1":
            self.addition()
        elif  user == "2":
            self.substration()

    def substration(self):
        print(self.val1 - self.val2)

    def addition(self):
        print(self.val1 + self.val2)
        print(f'''press 1 to go to main menu 
                    2 to exit
      ''')
        user = input('Your option')
        if user == '1':
            self.math()
        elif user == '2': 
          self.casnio()
        sys.exit()
        # else:
        #     print('worng input')   

casnio = Calculator()
