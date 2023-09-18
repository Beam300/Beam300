student = input("Are you a student")
if  student.strip() == "yes":
   print("enter")

else:
  print("go to front desk to register")

student = input("paid for tuition fees")
if student.strip() == "Balance":
  print("enter")
elif student.strip() == "pay half":
   print("go to front desk")
else:
   print("go home now")  



print( "welcome".center(100)) 
print('''who are you
          1. student
          2. staff
          3. not a student ''')
res = input('your option:')
if res == '1':
  print(''' payment status
  1. fully paid
  2.yet to balance
  ''')
  res: input('your option')
  if res == (1):
    print("enter")
elif res == (2):
    print("Enter you are Welcome.") 
elif res == '2':  
     print("Go to the font dessk")
else:
   print('Invaild Option')