print('WELCOME'.center(100))
noStudent = int(input('how many student are taking this Exam:  '))
print ('kindly provide the information of each student taking the exam...')
student_info = {}
student_info2 = {}
total_score = []
x =1 
for student in range(noStudent):
  info = []
  name = input(f"student{x} full Name: ")
  mat_no = input(f"stundent{x} mat_no: ")
  score = 0
  info =[name, mat_no, score] 
  student_info[f"student {x}: "] = info
  x +=1
  # print(info)

# print(score)
for inf, stu in student_info.items():
  print(stu[0], "Your exam start Now")
  question ={
  1:{'d':'''
  1. what are the capital of lagos State 
  (a)Berger (b) Ajah (c) Ogbomoso (d) Ikeja
  ''' },
  2:{'c':'''
  2. What is the capital of Oyo State
  (a) Abuja (b) Ibarapa (c) Ibadan (d)  Iseyin
  '''},
    3:{'a':'''
  3. What is the capital of Osun State
  (a) Yenagoa (b) osogbo (c) Sagbama (d)  Brass
  '''}
  } 

  for x in question.values():
    for y, z in x.items():
        print (z)
        user = input('your answer:')
        if user.strip().lower() == y:
          stu[2]+= 5
        
        
    print('''
    please Wait Result loading...
    '''.center(100))
    print ('your total score is', stu[2],'/15')

    total_score.append(stu[2])
    student_info2[stu[2]] = stu[0]

maximum = (max(total_score))
print (f"congratulation {student_info2 [maximum]} you score {maximum} which is the highiest score")

