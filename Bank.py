import sys
print('WELCOME TO BB BANK '.center(100))
class Bank:
    def __init__(self):
        self.name = 'bbb'
        self.bbb()
    def bbb1(self):
      user = input('ussd bank code: ')  
      if user == '*919#':
         self.bbb2()
      else:
         print('invalid ussd code')
         self.bbb1()

    def bbb2 (self):
            print('''
            1.sign in 
            2.sign up
            3. Exit
            ''') 
            user = input('user option: ')
            if user =='1': 
               self.sign_in()
            elif user == '2':
                self.sign_up()
            elif user =='3':
                sys.exit   
    # def sign_in(self):                  
            


        
        