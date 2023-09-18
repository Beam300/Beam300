import mysql.connector as sql 

mycon = sql.connect(host='127.0.0.1', user='root', password='', database = 'index_db')
mycursor = mycon.cursor()

import sys
import random
class Page:
    def __init__(self, name):
        self.name = name
        self.page1()

    def main(self):
        self.page1()

    def page1(self):

        
        print(f'Welcome to  Son Of Man mobile bank application'.center(100))
        



        print('''  1. Log in   2. Sign up   3. Exit   ''')

        user = input("User: ")
        if user == "1":
            self.log_in()
        elif user == "2":
            self.sign_up()
        elif user == "3":
            self.exit()

    def sign_up(self):
        query = "INSERT INTO customer_table(fullname, email, phone_number, bvn, username, password, account_no, account_bal) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
      
        print('Sign up page'.center(100))
        self.fullname = input(f"\nFullname: ")
        
        self.email_address = input("Email address: ")
       
        phone_number = input("Phone number: ")
       
        bvn = random.randint(22000000000, 22999999999)
        print(f"Your BVN number is {bvn}")
       
        self.username = input("Username: ")
       
        self.password = input(f"Password: ")
       
       
        account_no = random.randint(2100000000, 2199999999)
        print(f"Your account number is {account_no}")
       
        self.account_bal = 0.00
      
        val = (self.fullname, self.email_address, phone_number, bvn, self.username, self.password, account_no, self.account_bal)
        mycursor.execute(query, val)
        mycon.commit()
        print(mycursor.rowcount, 'row inserted successfully')
        print('Please wait...')
      
        print("Loading...")
       
        print("Successfully registered")
        self.log_in()
    
    def log_in(self):
        query = "SELECT username, password FROM customer_table WHERE username = %s AND password = %s"
      
        print('Log in page'.center(100))
        self.username = input("Username: ")
  
        self.password = input(f"Password: ")
      
        val = (self.username, self.password)
        mycursor.execute(query, val)
        output = mycursor.fetchall()
        if output:
            print('Please wait...')
         
            print("Loading...")
          
            self.home_page()
        else:
            print(f"Wrong password or username!")
            user = input("Press 'a' to reset password or 'b' to sign up: ")


                                # For password

            # 1
            

    def home_page(self):
   
        val = (self.username, self.password)
        print("""
                                                Home page
        """)
        print(f"""
                                        Welcome back {self.username}
        """)    
    
        print("""
                    1. Buy airtime                    5. Withdraw 
                    2. Transfer                       6. Transaction history                                      
                    3. Check balance                  7. Log out
                    4. Deposit                        8. Exit
                                                        
                    
        """
        )
        
        user = input("Enter your choice: ")
        if user == "1":
            self.buy_airtime()
        elif user == "2":
            self.transfer()
        elif user == "3":
            self.check_balance()
        elif user == "4":
            self.deposit()
        elif user == "5":
            self.withdraw()
        elif user == "6":
            self.transaction_history1()    
        elif user == "7":
            self.log_out()
        elif user == "8":
            self.exit()


    #             # Airtime

    def buy_airtime(self):
        
        print("Buy Airtime".center(100))
        
        query = "SELECT account_bal FROM customer_table WHERE username = %s and password = %s"
        val = (self.username, self.password)
        mycursor.execute(query, val)
        detail = mycursor.fetchall()
        self.balance = detail[0][0]
        print(f"Your account balance is #{detail[0][0]}")

        print("1. For self 2. For others")
        user = input("Enter your choice: ")

        if user == "1":
            self.for_self()
        elif user == "2":
            self.for_others()


        # Airtime for self

    def for_self(self):
        
        self.buy_airtime1 = float(input('Please enter an amount: '))
        

        if self.buy_airtime1:
            
            print(f"You have successfully recharge #{self.buy_airtime1} airtime.")

            self.balance -= self.buy_airtime1


            query = 'UPDATE customer_table SET account_bal = %s WHERE username = %s AND password = %s'
            val = (self.balance, self.username, self.password)
            mycursor.execute(query, val)        
            mycon.commit()
           
            print(f'Your new balance is #{self.balance}')
            
            print("Press 1 to go back or 2 to exit: ")
            user = input("Enter your choice: ")

            if user.lower() == "1":
                self.home_page()
            elif user.lower() == "2":
                sys.exit()
                


            # Airtime for others

    def for_others(self):
        
        print("Buy Airtime for others".center(100))
      
        query = "SELECT account_bal FROM customer_table WHERE username = %s and password = %s"
        val = (self.username, self.password)
        mycursor.execute(query, val)
        detail = mycursor.fetchall()
        self.balance = detail[0][0]
        print(f"Your account balance is #{detail[0][0]}")
        self.buy_airtime1 = float(input('Please enter an amount: '))
     
        number = print("\nPlease enter the recipients phone number")

        self.user2 = input("Recipients number: ")
        self.number()

    def number(self):
       
        print("Please choose a network  1. MTN 2. Airtel 3. GLO")
        

        user = input("Enter your choice: ")
        if user == "1":
          
            if self.buy_airtime1:
               
                print(f"You have successfully recharge #{self.buy_airtime1} airtime for {self.user2}.")

                self.balance -= self.buy_airtime1


                query = 'UPDATE customer_table SET account_bal = %s WHERE username = %s AND password = %s'
                val = (self.balance, self.username, self.password)
                mycursor.execute(query, val)        
                mycon.commit()
               
               
                print(f'Your new balance is #{self.balance}')
              
                print("Press A to go back or B to exit: ")
                user = input("Enter your choice: ")

                if user.lower() == "a":
                    self.home_page()
                elif user.lower() == "b":
                    sys.exit()
                
        elif user == "2":
            if self.buy_airtime1:
              
                print(f"You have successfully recharge #{self.buy_airtime1} airtime for {self.user2}.")

                self.balance -= self.buy_airtime1


                query = 'UPDATE customer_table SET account_bal = %s WHERE username = %s AND password = %s'
                val = (self.balance, self.username, self.password)
                mycursor.execute(query, val)        
                mycon.commit()
                
                print(f'Your new balance is #{self.balance}')
            
                print("Press A to go back or B to exit: ")
                user = input("Enter your choice: ")

                if user.lower() == "a":
                    self.home_page()
                elif user.lower() == "b":
                    sys.exit()
                  
        elif user == "3":
            if self.buy_airtime1:
               
                print(f"\nYou have successfully recharge #{self.buy_airtime1} airtime for {self.user2}.")

                self.balance -= self.buy_airtime1


                query = 'UPDATE customer_table SET account_bal = %s WHERE username = %s AND password = %s'
                val = (self.balance, self.username, self.password)
                mycursor.execute(query, val)        
                mycon.commit()
                
                print(f'Your new balance is #{self.balance}')
                
                print("Press A to go back or B to exit: ")
                user = input("Enter your choice: ")

                if user.lower() == "a":
                    self.home_page()
                elif user.lower() == "b":
                    sys.exit()
                    



                                # Transfer

    def transfer(self):
        
        print("Transfer".center(100))
        
        query = "SELECT account_bal FROM customer_table WHERE username = %s and password = %s"
        val = (self.username, self.password)
        mycursor.execute(query, val)
        detail = mycursor.fetchall()
        self.balance = detail[0][0]
        print(f"Your account balance is #{detail[0][0]}")
        self.transfer1 = float(input('Please enter the amount you want to transfer: '))
      

        if self.transfer1 >= self.balance:
          
            print("Insufficient fund.")
            
            print("1. Deposit 2. Back")

            customer = input("Please choose an option: ")

            if customer == "1":
                self.deposit()
            elif customer == "2":
                self.home_page()

        elif self.transfer1 <= self.balance:
            self.user = print("Please enter the beneficiary account number")

            self.account_no = input("Beneficiary account number: ")
           
            self.fullname1 = print({self.fullname})
            query1 = ("SELECT account_no, account_bal, fullname FROM customer_table WHERE account_no=%s")
            val1 = (self.account_no,)
            mycursor.execute(query1, val1)
            detail = mycursor.fetchall()
            # print(detail)
            self.balance_benef = detail[0][1]
            self.balance_benef += self.transfer1

            query = 'UPDATE customer_table SET account_bal = %s WHERE account_no=%s'
            val = (self.balance_benef, self.account_no,)
            mycursor.execute(query, val)
            mycon.commit()
          
            
            if detail:
                self.beneficiary_accountnumber()
            else:
                print("Invalid account number")
              
                print("Press A to go back to transfer page, B to go back to home page or C to exit: ")
                user = input("Enter your choice: ")

                if user.lower() == "a":
                    self.transfer()
                elif user.lower() == "b":
                    self.home_page()
                elif user.lower() == "c":
                    sys.exit()
                
        

    def beneficiary_accountnumber(self):
        
        if self.account_no:
            print(f"You have successfully transfer #{self.transfer1} to {self.account_no}.")
            



        self.balance -= self.transfer1

                     
                        
                        # User account update
        query = 'UPDATE customer_table SET account_bal = %s WHERE username = %s AND password = %s'
        val = (self.balance, self.username, self.password)
        mycursor.execute(query, val)        
        mycon.commit()
      
        print(f'\nYour new balance is #{self.balance}')
    
        print("Did you want to make another transaction?1. Continue 2. No")
        user = input("Enter your choice: ")
        if user == "1":
            self.transfer()
        elif user == "2":
         
            print("Press A to go back or B to exit: ")
            user = input("Enter your choice: ")

            if user.lower() == "a":
                self.home_page()
            elif user.lower() == "b":
                sys.exit()
            
                            # Check balance

    def check_balance(self):
     
        print("Check Balance".center(100))
       
        query = "SELECT account_bal FROM customer_table WHERE username = %s and password = %s"
        val = (self.username, self.password)
        mycursor.execute(query, val)
        detail = mycursor.fetchall()
        # print(detail)
        print(f"Your account balance is #{detail[0][0]}")
       
        print("Press A to deposit, B to go back to main or C to exit: ")
        user = input("Enter your choice: ")

        if user.lower() == "a":
            self.deposit()
        elif user.lower() == "b":
            self.home_page()
        elif user.lower() == "c": 
            sys.exit()
     


                                    # Deposit


    def deposit(self):
    
        print("Deposit".center(100))
      
        query = "SELECT account_bal FROM customer_table WHERE username = %s and password = %s"
        val = (self.username, self.password)
        mycursor.execute(query, val)
        detail = mycursor.fetchall()
        balance = detail[0][0]
        # print(detail)
        print(f"Your account balance is #{detail[0][0]}")
        deposit = float(input('Please enter the amount you want to deposit: '))
        balance += deposit

        
        query = 'UPDATE customer_table SET account_bal = %s WHERE username = %s AND password = %s'
        val = (balance, self.username, self.password)
        mycursor.execute(query, val)        
        mycon.commit()
        print("Loading...")
       
        print(f'Your new balance is #{balance}')
      
        print("Press A to go back or B to exit: ")
        user = input("Enter your choice: ")

        if user.lower() == "a":
            self.home_page()
        elif user.lower() == "b":
            sys.exit()
          



                                        # Withdraw

    def withdraw(self):
      
        print("Withdraw".center(100))
       
        query = "SELECT account_bal FROM customer_table WHERE username = %s and password = %s"
        val = (self.username, self.password)
        mycursor.execute(query, val)
        detail = mycursor.fetchall()
        balance = detail[0][0]
        print(f"Your account balance is #{detail[0][0]}")
        withdraw = float(input('Please enter the amount you want to withdraw: '))
        balance -= withdraw

        query = 'UPDATE customer_table SET account_bal = %s WHERE username = %s AND password = %s'
        val = (balance, self.username, self.password)
        mycursor.execute(query, val)        
        mycon.commit()
        print("Loading...")
    
        print(f"You have successfully withdraw #{withdraw}")
        
        print(f'Your new balance is #{balance}')
        
        print("Did you want to make another transaction?  1. Reply 2. No")
        user = input("Enter your choice: ")
        if user == "1":
            self.withdraw()
        elif user == "2":
         
            print("n Press A to go back or B to exit: ")
            user = input("Enter your choice: ")

            if user.lower() == "a":
                self.home_page()
            elif user.lower() == "b":
                sys.exit()
               



                            # Transaction History

    def transaction_history(self):
    
        print("Transaction History".center(100))
    
        query = "SELECT transaction_history FROM customer_table WHERE username = %s and password = %s"
        val = (self.username, self.password)
        mycursor.execute(query, val)
        detail = mycursor.fetchall()
        # print(detail)
        query = 'UPDATE customer_table SET transaction_history = %s WHERE username = %s AND password = %s'
        val = (self.transfer, self.deposit, self.withdraw, self.username, self.password)
                       
        mycon.commit()

        if self.transfer:
            print(f"You recently make a transfer")
        elif self.deposit:    
            print(f"You recently make a deposit")
        elif self.withdraw:
            print(f"You recently make a withdrawal")
        else:
            print("No transaction record")
      
        print("Press 1to go back or 2 to exit: ")
        user = input("Enter your choice: ")

        if user.lower() == "1":
            self.home_page()
        elif user.lower() == "2":
            sys.exit()
            
        












    def exit(self):
        sys.exit()
          
            



ussd = Page('name')