# print("Welcome to python class")
# bottle = "water," "salt", 'stone'
# print(bottle)
# x, y, z, = 20, 30,90, 95.67
# print(x)
# print(y)
# print(z)
# __name_of_student = "Abimbola"
# address = "ogbomoso"
# state = "state"
# age = "14"


# print("my name is Abimbola "+  __name_of_student + ",I live in ogobomoso" + address +"16 yaaco" ) 
# # print(f"My name is , ")
# # global and locals variables
# global result
# val1 = 10
# val3 = 50
# def addition():
#     # This funtion performs an addition operation
#     global val2 
#     val2 = 20
#     result = val1 + val2 + val3
#     # print(f"Your answer is {result}") 
#     def substract():
#         # This funtion performs substraction operation 
#         val3 = 50
#         result2 = val3 - val2
#         print(f"Your answer is ") 

#         _my = ({"orage"," mango", "bananna"})
#         print(type(_my))
       
#     addition()
#     substract()
#         pyhon identation
#         identation refer to the space at the begining of a code
#         Type of datatype
#         1. text types: string (str)
#         2. Numeric types: integer(int), float, complex
#         3. sequence types: list, tuple, range 
#         4. mapping types: dictionary(dict)
#         5. set types: set, rozenset
#         6. boolean types: bool (true, false)
#         7. Binary types: bytes, bytearray, memoryview

#           #   #  Examples
#           string (str) example: "Johnson", "false", "56", 
#         x = "hello wolrd"     
#         x = 20

    # print("1. sign up 2. sign in")
    # print("My name is"+ frist_name +"Abimbola")

    # print(f"My name is {fristname} {lastname}, i am {age}years old")


# bytes() to convert to bytes

# print("Types before convertion", type(__name__))
# print("Types afer convertion")

# val1 = float (input("enter frist number"))
# val2 = input("enter frist number")
# result = val1 + float(val2)
# print(f"the total score is {result}")

# x = int(input("input your value"))
# # print(type(val1))
# if x :
#     print(" Yes ")
# else:
#     print(" No")    

# order = input("want do you want? ")
# if order.strip()==  "rice":
#      print("sucesss")
     
     
# else:
#      print("falied")


# name = "tim bank"
# print(name.center (100))

# name = "sunday"
# print(name.encode())

# print("she's the ower")



# ASSIGNMENT OF CBT TEST.

# student = input("Are you a student")
# if  student.strip() == "yes":
#    print("enter")

# else:
#   print("go to front desk to register")

# student = input("paid for tuition fees")
# if student.strip() == "Balance":
#   print("enter")
# elif student.strip() == "pay half":
#    print("go to front desk")
# else:
#    print("go home now")    

# x = 0
# for name in my_list:
#     print(name, x)
#     x += 1   
# DICTIONARY: IS A COLLECTION WHICH IS ORDERED CHANGEABLE BUT DOES NOT ALLOW DUPLICATION AND UNINDEXED
# it is written using {key:value} or dict(key=value)

# product = {'name':"damilare", 'coures':'robotics', 'vehicle':"toyota",
#  "passenger":60, "colour":"blue"}
# print(product['color])
# print(product.get('passengers'))
# print(product.key())
# print(product.values())
# product['passenger'] =10
# print(product)
# print(product.items)

# for y in product.key:()
#        print(y)
# print('name' in product)
# product.update({'size':13})
# print(product) 

# product.update(dict('age'==13))
# product.pop('color')
# product.popitems()
# del product
# product.clear()
# print(product)

# stundent = {}
# no =1 
# for x in range(3):
#  name = input(f"name{no}: ")
# mat_no = input(f"name{no}: ")
# course =input(f"name{no}: ")
# details =[name, mat_no, course]
#  print(details)
# studentData.update({f"student {no}": details})
# no +=1

# print(studetData)
#  for details in studentData.values():
#   print(details[0]) 

# furniture = ['1.) table -$100', '2.) chair - $50', '3.) rack -$80', '4.) half - $40']
# price = [100, 50, 80, 40]

# for item, amount in zip(furniture, price):
#     price(item)
#     user = int(input(f"pay ${amount}: "))
#     if user == amount:
#      print(f"take your item/n")
# else:
#    print("pay the require amount/n")   





#    x = 1
# while x <= 10:
#    print(f'you are welcome to class {x}')
#    x +=1
# x = 10
# while x > 0:
#  print ('i will not do it again')


# for x in(1,2,3,4,5,6,7,8,9,10,11,12): 
#    print (x, 'time table')
#    for i in (1, 2, 3, 4, 5, 6):
#       result = x * i
#       print(f"{x} x {i}=,{result}")
#  fuction declaration
# definition
# invocation


# def nameoffuction()  unparameter
# primt(f'my fuction name is {name}') parameter

# def addition(val1 , val2):
#     return val1+val2
# addition(25 ,10)

# def walk(name):
#     print(name,"is walking")
#     walk("presious")

# def divide(val1 , val2):
#     print(val1/val2)
#     divide(float(input("the numerator: ")), float(input("thr denominator: ")))

# def divide():
#     val1 = float(input("the Numerator"))
#     val2 = float(input("the denomerator"))
#     print(val1/val2)
# divide()    

# val1 = float(input("the nume"))

# def division():
#     global val2
#     val2 = float(input("the denomi: "))
#     addition()
#     # print(val1 ,val2)

#     # division()
# def addition():
#     val3 = 20
#     res = val1 + val3 + val2
#     print(res)
#     # addition()
# division()
    

# def subtracte(a, b):
#     return a - b
# print(subtracte(20,10))

# class Human:
#     def __init__(self):
#         self.name = "abimbola"
#         self.complexion = "dark"
#         self.talk()

#         def talk(self):
#             print(f"my name is {self.name}")
#             abimbola= Human

# class Phone:
#     def __init__(self):
#       self.phone = 'tecno'
#       self.battery = "22000mh"
#       self.product()
#     #   self.message()

#     def product(self):
#        print(f"the name of the phone {self.phone}")
#        self.message() 
#     def message(self):
#        print(f"{self.message}tecno live it love it")
   
# tecno = Phone()


                                            #OOOPPY>PY

# ImportError
# class Calculator:
#     def __init__(self):
#         self.name = 'casnio'
#         self.math()

#     def math(self): 
#         print(f"{self.name} Calculator".center(100)) 

#         self.val1 = float(input("enter val1: "))
#         self.val2 = float(input("enter val2: "))

#         print(f""" 
    
#         select your option
#         1.  addition
#         2.  substration
    
#         """)
#         user = input("your option: ")  
#         if user =="1":
#             self.addition()
#         elif  user == "2":
#             self.substration()

#     def substration(self):
#         print(self.val1 - self.val2)

#     def addition(self):
#         print(self.val1 + self.val2)
#         print(f""" press 1 to go to main menu 
#                     2 to exit
    
#         """)
#         user = input('math')
#         if user == '1':
#             self.math()
#         elif user == '2': 
#          SystemExit()
#         else:
#             print('worng input')   

# casnio = Calculator()

        
# class Father:
#     def __init__(self,  frist_name, last_name, age):
#         self.first_name = frist_name
#         self.last_name = last_name
#         self.age = age
#     def details(self, occupation):
#         print(f"My name is {self.first_name} {self.last_name}, Iam{self.age}yrs old. I am an {occupation}")

#         self.occupation = occupation
#     def talk(self):
#         print(f"My name is {self.first_name} {self.last_name}, Iam{self.age}yrs old. I am an {self.occupation}")



# Daddy = Father("Justice", "Adebayo", 50)
# Daddy.details("Footballer")      
# Daddy.details("Footballer")   
# Daddy.talk() 

# import sys
# class Calculator:
#     def __init__(self, add):
# #         self.add = add
      
#     def math(self, val3 , val4): 
#         print (f"{self.add} Calculator")

#         self.val3 = val3   
#         self.val4 = val4   

#         print("""
#         choose  operation
#         1. addition
#         2. subtraction
#         3. exict
#         """)

#         user = input("option: ")
#         if user  == '1':
#             self.addition
#         elif user == '2':
#             self.subtraction 
#         elif user == '3':
#             sys.exit          

# add = Calculator
# import sys
# class Code:
#   def __init__(self):
#     self.page1()
#   def page1(self):
       
#     user = input('USSD Code')
#     if user == '*777#':
#         self.page2()
#     else:
#       print('invalid ussd code')  
#       self.page1()

#   def page2(self):
#     print('''
#     1. Data plan
#     2. Data Balance
#     3. Exit
#     ''')
#     user = input('Option')
#     if user == '1':
#         self.data_plan()
#     elif user == '2':
#         self.data_Balance()
#     elif user == '3':
#         sys.exit () 

#   def data_plan (self):
#     print(f'''
#        1.  daily plan
#        2.  weekly plan 
#        3.  montly plan
#        4. exit
#     ''' ) 
#     user = input('Option')
#     if user == '1':
#         self.daily_plan()
#     elif user == '2':
#         self.weekly_plan()
#     elif user == '3':
#          self.exit()
#     elif user == '4':
#         sys.exit () 
#   def daily_plan(self):
#      print(f'''
#        1.  50mb
#        2.  100mb 
#        3.  3gb
        
#         ''')
#   def weeekly_plan(self):
#      print(f"""
#      1. 1gb 14days
#      2. 500mb for 7 days
#      3. 2gb for 7days 
     
#      """)

#   def montly_plan(self):
#      print(f"""
#      1. 5gb for 30days
#      2. 10gb for 30days
#      3. 1tb for 1year
     
#      """)    
#      user = (input('your option: '))
#      if user == "daily_plan":
#         print('you have recived you plan')


# page = Code()


#                                  INHERITACE PYTHON

class Parent:
    def __init__(self):
        self.fristName = 'johndo'
        self.lastName = 'Alagba'
#         self.age = '40'
#     def print(self):
#           print(f"my name {self.fristName} {self.lastName}, i am  {self.age}years old"), 



# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self .fristName = "Olamide"
#         self.age = 22
#         self.print()
        self.running()

#     def running(self):
#          print(f"{self.fristName } is running")       
# child = Child()
# child.print

# class Grand_child(Child):
#     def __init__(self):
#           Child.__init__(self)
#           self.fristName = "Emma"
#           self.age = 13
          
#     def running(self):
#          print(f"{self.fristName} is Running")

 
# granchild = Grand_child()
# granchild.print()

# import time os, sys, datetime, random, re

# import
# shola = Parent()
# shola.print        



# print("HELLO")
# print(True)
# f_bool = False
# print(f_bool)
# print("Hello World")