import os
if os.path.exists("C:\\PYWORK\\text.pdf"):
    with open("C:\\PYWORK\\text.pdf", mode="rt") as myfile:
        print(myfile.read())
else:
    print("file does not exist")   
    print('_'*100)
    with open("C:\\PYWORK\\text.pdf", mode="xt")as myfile:
     print("file created successfully")




os.mkdir("C:\Users\b\Desktop\newfloder")
os.rmdir("C:\Users\b\Desktop\newfloder")