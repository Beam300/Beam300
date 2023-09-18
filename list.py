my_file = open(r'C:\PYWORK\text.txt', 'rt')
# print(file.read())
student_pass = []
student_fail = []
for i in my_file:
    file = i.split(',')
    print(file[1])
    if int(file[1]) < 40:
        student_fail.append(file)


    else:
         student_pass.append(file)  


passs = open(r'C:\PYWORK\pass.txt', 'wt')
# print(student_pass)
for items in student_pass:
    # print(items)
    it = ",".join(items)
    print(it)
    passs.write(it)


fail = open (r'C:\PYWORK/fail.txt', 'wt') 
# print(student_fail)      
for item in student_fail:
    print(items)
    it = ",".join(items)
    print(it)
    fail.write(it)




