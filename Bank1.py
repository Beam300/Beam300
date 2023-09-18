# import mysql.connector as sql 

# mycon = sql.connect(host='127.0.0.1', user='root', password='', database = 'index_db')

import sys
class Page:
    def __init__(self):
        self.name = 'ussd'
        self.main()

    def main(self):
        self.page1()

    def page1(self):
        print(f'Welcome to {self.name} welcome to BB bank'.center(100))
        print("""\nPlease choose an option 
        1. Sign up 
        2. Sign in 
        3. Exit""")

        user = input("User: ")
        if user == "1":
            self.sign_up()
        elif user == "2":
            self.sign_in()
        elif user == "3":
            self.exit()

    def sign_up(self):
    
        print('Sign up page'.center(100))
        user_info = {}
        user_info2 = {}
        x = 1
        for users in range (1):
            info = []
            user_name = input(f"User {x} full name: ")
            
            email = input(f"User {x} email: ")
           
            phone_number = input(f"User {x} phone number: ")
           
            password = input(f"User {x} password: ")
           
            info = [user_name, email, phone_number, password]
            user_info[f"User {x}: "] = info
            x += 1
            # print(user_info)
            print('Please wait...')
           
            print("Loading...")
           
            self.sign_in()
    
    def sign_in(self):
       
        print('Sign in page'.center(100))
        user_info = {}
        user_info2 = {}
        user_info3 = {}
        x = 1
        for users in range (1):
            info = []
            email = input(f"User {x} email: ")
            password = input(f"User {x} password: ")
            info = [email, password]
            user_info[f"User {x}: "] = info
            x += 1
            # print(user_info)
            print('Please wait...')

            print("Loading...")
          
            self.home_page()

    def home_page(self):
       
        print("Home page".center(100))
        print(f"Welcome")
        
        
        print('''1. Buy airtime             4. Check balance 
               2. Buy Data                5. Deposit
              3. Transfer                 6. betting''')
        
        user = input("\nEnter your choice: ")
        if user == "1":
            self.buy_airtime()
        elif user == "2":
            self.buy_data()
        elif user == "3":
            self.transfer()
        elif user == "4":
            self.check_balance()
        elif user == "5":
            self.deposit()


            # Airtime

    def buy_airtime(self):
        print("1. For self 2. For others")
        user = input("Enter your choice: ")

        if user == "1":
            self.for_self()
        elif user == "2":
            self.for_others()


        # Airtime for self

    def for_self(self):

        print("Please choose an amount")
        print('''1. #100 
              2. #200 
              3. #300 
              4. #400 
              5. #500''')

        user = input("Enter your choice: ")

        if user == "1":
           
            print("You have successfully recharge #100.")
        elif user == "2":
           
            print("You have successfully recharge #200.")
        elif user == "3":
          
            print("You have successfully recharge #300.")
        elif user == "4":
           
            print("You have successfully recharge #400.")
        elif user == "5":
            
            print("You have successfully recharge #500.")



            # Airtime for others

    def for_others(self):
       
        number = print("Please enter the recipients phone number")

        self.user2 = input("Recipients number: ")
        self.number()

    def number(self):
      
        print("Please choose a network 1. MTN 2. Airtel 3. GLO")
        

        user = input("\nEnter your choice: ")
        if user == "1":
          
            print('''1. #100 
                    2. #200 
                    3. #300 
                    4. #400
                    5. #500''')

            user = input("Choose your choice: ")
            if user == "1":
             
                print(f"You have successfully recharge #100 for {self.user2}.")
            elif user == "2":
               
                print(f"You have successfully recharge #200 for {self.user2}.")
            elif user == "3":
               
                print(f"You have successfully recharge #300 {self.user2}.")
            elif user == "4":
           
                print(f"You have successfully recharge #400 {self.user2}.")
            elif user == "5":
              
                print(f"You have successfully recharge #500 {self.user2}.")
        elif user == "2":
            print("1. #100 2. #200 3. #300 4. #400 5. #500")

            user = input("\nChoose your choice: ")
            if user == "1":
               
                print(f"\nYou have successfully recharge #100 for {self.user2}.")
            elif user == "2":
              
                print(f"\nYou have successfully recharge #200 for {self.user2}.")
            elif user == "3":
               
                print(f"\nYou have successfully recharge #300 for {self.user2}.")
            elif user == "4":
               
                print(f"\nYou have successfully recharge #400 for {self.user2}.")
            elif user == "5":
              
                print(f"\nYou have successfully recharge #500 for {self.user2}.")
        elif user == "3":
            print("1. #100 2. #200 3. #300 4. #400 5. #500")

            user = input("\nChoose your choice: ")
            if user == "1":
                
                print(f"You have successfully recharge #100 for {self.user2}.")
            elif user == "2":
               
                print(f"\nYou have successfully recharge #200 for {self.user2}.")
            elif user == "3":
             
                print(f"\nYou have successfully recharge #300 for {self.user2}.")
            elif user == "4":
                
                print(f"\nYou have successfully recharge #400 for {self.user2}.")
            elif user == "5":
                
                print(f"\nYou have successfully recharge #500 for {self.user2}.")


        # Data plan

    def buy_data(self):
        print("\n1. For self \n2. For others")
        user = input("\nEnter your choice: ")

        if user == "1":
            self.for_self1()
        elif user == "2":
            self.for_others1()
    

        # Data plan for self

    def for_self1(self):
      
        print("\nPlease choose a plan")
        print("1. Daily 2. Weekly 3. Monthly")
        
        user = input("Choose a plan: ")
        if user == "1":
            self.daily1()
        elif user == "2":
            self.weekly1()
        elif user == "3":
            self.monthly1()


        # Daily

    def daily1(self):
       
        print("1. #100 for 100mb  2. #200 for 200mb  3. #300 for 1gb ")

        user = input("Enter your choice: ")

        if user == "1":
         
            print("\nYou have successfully bought a data paln of 100mb for 1day at #100.")
        elif user == "2":
           
            print("\nYou have successfully bought a data paln of 200mb for 1day at #200.")
        elif user == "3":
           
            print("\nYou have successfully bought a data paln of 1gb for 1day at #300.")


        # weekly

    def weekly1(self):
    
        print("\n1. #300 for 350MB \n2. #200 for 1GB(IG/TT/YT) \n3. #500 for 1.5GB")

        user = input("\nEnter your choice: ")

        if user == "1":
           
            print("\nYou have successfully purchased 350MB for #300")
        elif user == "2":
          
            print("\nYou have successfully purchased 1GB for #200.")
        elif user == "3":
         
            print("\nYou have successfully purchased 1.5GB for #500")


                # Monthly

    def monthly1(self):
       
        print("1. #1,000 for 1.5GB 2. #1200 for 2GB 3. #1,500 for 3GB")

        user = input("Enter your choice: ")

        if user == "1":
           
            print("\nYou have successfully purchased 1.5GB for #1,000")
        elif user == "2":
        
            print("\nYou have successfully purchased 2GB for #1200")
        elif user == "3":
            
            print("\nYou have successfully purchased 3GB for #1,500")
    


            # Data plan for others

    def for_others1(self):
        
        number = print("Please enter the recipients phone number")

        self.user4 = input("Recipients number: ")
        self.recipients_number()


            # recipients number

    def recipients_number(self):
        
        print("\nPlease choose a network\n \n1. MTN \n2. Airtel \n3. GLO")
        
        user = input("\nChoose a network: ")
        if user == "1":
            self.mtn2()
        elif user == "2":
            self.airtel2()
        elif user == "3":
            self.Glo2()
        

        # MTN data plan

    def mtn2(self):
       
        print("\n1. Daily \n2. Weekly \n3. Monthly")

        user = input("\nEnter your choice: ")
        if user == "1":
            self.daily2()
        elif user == "2":
            self.weekly2()
        elif user == "3":
            self.monthly2()


                # daily

    def daily2(self):
       
        print('''1. #100 for 100mb 
                2. #200 for 200mb 
                3. #300 for 1gb''')

        user = input("Enter your choice: ")

        if user == "1":
          
            print(f"You have successfully purchased a data paln of 100mb for 1day at #100 for {self.user4}.")
        elif user == "2":
          
            print(f"You have successfully purchased a data paln of 200mb for 1day at #200 for {self.user4}.")
        elif user == "3":
            
            print(f"You have successfully purchased a data paln of 1gb for 1day at #300 for {self.user4}.")



                    # weekly

    def weekly2(self):
       
        print('''1. #300 for 350MB 
                2. #200 for 1GB(IG/TT/YT) 
                3. #500 for 1.5GB''')

        user = input("Enter your choice: ")

        if user == "1":
           
            print(f"You have successfully purchased 350MB for #300 for {self.user4}.")
        elif user == "2":
            
            print(f"You have successfully purchased 1GB for #200 for {self.user4}.")
        elif user == "3":
            
            print(f"You have successfully purchased 1.5GB for #500 for {self.user4}.")



                    # monthly

    def monthly2(self):
     
        print("\n1. #1,000 for 1.5GB \n2. #1200 for 2GB \n3. #1,500 for 3GB")

        user = input("Enter your choice: ")

        if user == "1":
            
            print(f"You have successfully purchased 1.5GB for #1,000 for {self.user4}.")
        elif user == "2":
            
            print(f"You have successfully purchased 2GB for #1200 for {self.user4}.")
        elif user == "3":
            
            print(f"You have successfully purchased 3GB for #1,500 for {self.user4}.")


                    # Airtel data plan

    def airtel2(self):
        
        print("1. Daily 2. Weekly 3. Monthly")

        user = input("Enter your choice: ")
        if user == "1":
            self.daily3()
        elif user == "2":
            self.weekly3()
        elif user == "3":
            self.monthly3()


                # daily

    def daily3(self):
   
        print('''1. #100 for 100mb  
                2. #200 for 200mb
                3. #300 for 1gb ''')

        user = input("Enter your choice: ")

        if user == "1":
         
            print(f" Congrat You have successfully bought a data paln of 100mb for 1day at #100 for {self.user4}.")
        elif user == "2":
         
            print(f" Congrat You have successfully bought a data paln of 200mb for 1day at #200 for {self.user4}.")
        elif user == "3":
          
            print(f" Congrat You have successfully bought a data paln of 1gb for 1day at #300 for {self.user4}.")


                # Weekly

    def weekly3(self):
       
        print("1. #300 for 350MB 2. #200 for 1GB(IG/TT/YT) 3. #500 for 1.5GB")

        user = input("Enter your choice: ")

        if user == "1":
          
            print(f" Congrat You have successfully purchased 350MB for #300 for {self.user4}.")
        elif user == "2":
          
            print(f" Congrat You have successfully purchased 1GB for #200 for {self.user4}.")
        elif user == "3":
         
            print(f"Congrat You have successfully purchased 1.5GB for #500 for {self.user4}.")



                # monthly

    def monthly3(self):
    
        print('''1. #1,000 for 1.5GB 
                2. #1200 for 2GB 
                3. #1,500 for 3GB''')

        user = input("Enter your choice: ")

        if user == "1":
        
            print(f"You have successfully purchased 1.5GB for #1,000 for {self.user4}.")
        elif user == "2":
          
            print(f"You have successfully purchased 2GB for #1200 for {self.user4}.")
        elif user == "3":
            
            print(f"You have successfully purchased 3GB for #1,500 for {self.user4}.")



                # Glo data plan

    def glo3(self):
       
        print("1. Daily 2. Weekly 3. Monthly")

        user = input("Enter your choice: ")
        if user == "1":
            self.daily4()
        elif user == "2":
            self.weekly4()
        elif user == "3":
            self.monthly4()


                    # daily

    def daily4(self):
       
        print("1. #100 for 100mb for 1day 2. #200 for 200mb for 2day 3. #300 for 1gb for 1day")

        user = input("Enter your choice: ")

        if user == "1":
            
            print(f"Congrat You have successfully bought a data paln of 100mb for 1day at #100 for {self.user4}.")
        elif user == "2":
        
            print(f"Congrat You have successfully bought a data paln of 200mb for 1day at #200 for {self.user4}.")
        elif user == "3":
            
            print(f"Congrat You have successfully bought a data paln of 1gb for 1day at #300 for {self.user4}.")



                    # weekly

    def weekly4(self):
      
        print("\n1. #300 for 350MB 2. #200 for 1GB(IG/TT/YT) 3. #500 for 1.5GB")

        user = input("Enter your choice: ")

        if user == "1":
           
            print(f"You have successfully purchased 350MB for #300 for {self.user4}.")
        elif user == "2":
           
            print(f"You have successfully purchased 1GB for #200 for {self.user4}." )
        elif user == "3":
           
            print(f"You have successfully purchased 1.5GB for #500 for {self.user4}.")


                    # monthly

    def monthly4(self):
      
        print("1. #1,000 for 1.5GB 2. #1200 for 2GB 3. #1,500 for 3GB")

        user = input("Enter your choice: ")

        if user == "1":
          
            print(f"You have successfully purchased 1.5GB for #1,000 for {self.user4}.")
        elif user == "2":
           
            print(f"You have successfully purchased 2GB for #1200 for {self.user4}." )
        elif user == "3":
           
            print(f"You have successfully purchased 3GB for #1,500 for {self.user4}.")













    def exit(self):
        sys.exit()
               
        



ussd = Page()