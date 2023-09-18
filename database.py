import mysql.connector as sql 

mycon = sql.connect(host='127.0.0.1', user='root', password='', database = 'index_db')

# mycursor = mycon.cursor()

# mycursor.execute("CREATE DATABASE index_db")


# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

# mycursor.execute("CREATE TABLE customer_table(id INT(3) PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(50), account_no VARCHAR(10) UNIQUE, account_bal FLOAT(9))")

# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

# mycursor.execute("ALTER TABLE customer_table CHANGE id customer_id INT(3) AUTO_INCREMENT" )

# mycursor.execute("ALTER TABLE customer_table ADD username VARCHAR(50) UNIQUE")

# mycursor.execute("ALTER TABLE customer_table ADD password VARCHAR(50) UNIQUE")


# mycursor.execute("INSERT INTO customer_table(fullname, account_no, account_bal, username , password) VALUES('Arise Damilare', '2109345864', 2000, 'Damilare', '1234')")

# mycon.commit()

# query = "INSERT INTO customer_table(fullname, account_no, account_bal, username , password) VALUES(%s,%s,%s,%s,%s)"
# val = ('Arise Damilare','2123456789', 2000, 'Damilare3', '2234')
# mycursor.execute(query, val)
# mycon.commit()
# print(mycursor.rowcount, 'row inserted successfully')

# mycursor.execute('SELECT*')
# def sign_in()



# inp_username = input ("username: ")
# inp_password = input ("password: ")

# query = "SELECT fullname, account_bal, account_no FROM customer_table WHERE username = %s AND password = %s"
# val = (inp_username, inp_password )
# mycursor.execute(query,  val)
# detail = mycursor.fetchall()
# # print(detail[0][0])

# if detail:
#     print("access granest")
# else:
#     print("access Denied")


# query = 'UPDATE customer_table SET account_bal = %s WHERE username = %s AND password = %s'
# val = (50000,inp_username, inp_password )
# mycursor.execute(query,val)
# mycon.commit()

# # with open ("c://PYWORK")

# Create 'x' mode
# my_file = open("C:\\PYWORK\\text.txt", 'xt')
# print('file created successfully')
# my_file = open("C:\\PYWORK\\text.pdf", 'a')
# print('file created successfully')

# my_file = open("C:\\PYWORK\\text.pdf", 'a')
# my_file.write("i am not writing.......")
# # myfile = open("C:\\PYWORK\\text.pdf", 'rt')
# print(myfile.read())


# # my_file = open("C:\\PYWORK\\text.pdf", 'w')
# # my_file.write("i am  writing.......")
# myfile = open("C:\\PYWORK\\text.pdf", 'rt')
# print(myfile.read())
# myfile.close

# import os
# if os.path.exists("C:\\PYWORK\\text.pdf"):
#     with open("C:\\PYWORK\\text.pdf", mode="rt") as myfile:
#         print(myfile.read())
# else:
#     print("file does not exist")   
#     print('_'*100)
#     with open("C:\\PYWORK\\text.pdf", mode="xt")as myfile:
#      print("file created successfully")

# os.mkdir("C:\\Users\Desktop\newfloder")
# os.rmdir("C:\\PYWORK\\Desktop\\newfloder")


 
# import os
# if os.path.exists("C:\\PYWORK\\file.pdf"):
#     with open("C:\\PYWORK\\text.pdf", mode="rt") as myfile:
#         print(myfile.read())
# else:
#     print("file does not exist")   
#     print('_'*100)
#     with open("C:\\PYWORK\\text.pdf", mode="xt")as myfile:
#      print("file created successfully")




# import os.path
# homedir = os.pathpanduser("~")
# print(homedir)
# print(homedir+"\Document")


# import os 
# homedir = os.environ["PATH"]
# print(homedir)

# import os
# print (os.path.abspath("database.py"))

# print(os.path.dirname(os.path.abspath("database.py")))




         