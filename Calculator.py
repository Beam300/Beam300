def Calculator():
    op = input('''

''')


    x = float(input("enter your number"))
    y = float(input("enter your number"))

    if op =="+":
        print(x+y)
    elif op == "-":
        print(x-y)
    elif op == "*":
        print(x*y)
    elif op == "/":
        print(x/y)
    elif op == "**":
        print(x**y)    
    else:
        print("enter invaild number")  

Calculator()    
        
  
