import sys
class Code:
  def __init__(self):
    self.page1()
  def page1(self):
       
    user = input('USSD Code')
    if user == '*777#':
        self.page2()
    else:
      print('invalid ussd code')  
      self.page1()

  def page2(self):
    print('''
    1. Data plan
    2. Data Balance
    3. Exit
    ''')
    user = input('Option')
    if user == '1':
        self.data_plan()
    elif user == '2':
        self.data_Balance()
    elif user == '3':
        sys.exit () 

  def data_plan (self):
    print(f'''
       1.  daily plan
       2.  weekly plan 
       3.  montly plan
       4. exit
    ''' ) 
    user = input('Option')
    if user == '1':
        self.daily_plan()
    elif user == '2':
        self.weekly_plan()
    elif user == '3':
         self.exit()
    elif user == '4':
        sys.exit () 
  def daily_plan(self):
     print(f'''
       1.  50mb
       2.  100mb
       3.  3gb
        
        ''')
  def weeekly_plan(self):
     print(f"""
     1. 1gb 14days
     2. 500mb for 7 days
     3. 2gb for 7days 
     
     """)

  def montly_plan(self):
     print(f"""
     1. 5gb for 30days
     2. 10gb for 30days
     3. 1tb for 1year
     
     """)    
     user = (input('your option: '))
     if user == "daily_plan":
        print('you have recived you plan')

       

        



name = Code()