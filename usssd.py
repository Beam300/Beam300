import sys
class Usssd:
    def __init__(self):
        self.name = 'data'
        self.code()

    def code(self):
        print(f"{self.name} usssd".center(100))

        self.val = float(input("enter val: "))
        # self.val2 = float(input("enter val2: "))

        print(f""" 
    
        select your option
        1. daily 
        2.  weekly 
        3. Exit
    
        """)    
        user = (input("your option: ") ) 
        if user =="1":
            self.daily()
        elif user =="2":
            self.weekly()
        elif user == '3':
          sys.exit () 

           
            
    def daily(self):
        print(f"""
       1.  50mb
       2.  100mb
       3.  3gb
        """)

    def weekly(self):
        print(f"""
       1.  250mb
       2.  500mb
       3.  3gb
        """)  
        user = (input("your option: "))
        if user == "daily":  
            print("you have recived you plan")
        
        elif user == '1':  
         print("you have recived you plan")
        elif user == '2':  
         print("you have recived you  500mb plan")
        elif user == '3':  
         print("you have recived you 3gb plan")
         
        else:
            print("""data plan 777
            Airtime 123
            Borrow 321
            """) 
            sys.exit

data = Usssd()           
    
              
        