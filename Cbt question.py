print("fill this following Question". center)
score = 0
print(''' Ques1. how many  state in nigeria
A. 34
B. 36
C. 56
D. 34

    ''')
Ques1 = input("enter your answer")
if Ques1.upper() == "B":
    print("correct")
    score += 2
else:
    print("wrong") 

print(''' Ques2. How many local government in Oyo state
A. 22
B. 33
C. 43
D. 12
''')
Ques2 = input("enter your answer")
if Ques2 == "B":
    print("correct")
    score =+ 2
else:
    print("wrong")    
print(''' Ques3. How many local government in Oyo state
A. 22
B. 33
C. 43
D. 12
''')
Ques3 = input("enter your answer")
if Ques3 == "2":
    print("correct")
    score = score+2
else:
    print("wrong")    
print(''' Ques4. how many  state in nigeria
A. 34
B. 36
C. 56
D. 34
# ''')
Ques4 = input("enter your answer")
if Ques4 == "2":
    print("correct")
    score = score+2
else:
    print("wrong") 

print("your total score is "+str(score)+"out of 4")