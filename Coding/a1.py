# ---PYTHON PROGRAMMING---
# print("hello world")

#___CONDITIONAL STATEMENTS___
# a =  int(input("Enter firstr number: "))
# x = input("Enter operation: ")
# b = int(input("Enter second number: "))
# if (x == "+"):
#     print("a+b = ",a + b)
# elif(x == "-"):
#     print("a-b = ",a-b)
# elif(x == "*"):
#     print("a*b = ",a*b)
# elif(x == "/"):
#     print("a/b = ",a/b)
# elif(x == "//"):
#     print("a//b = ",a//b)
# elif(x == "**"):
#     print("a**b = ",a**b)
# else:
#     print("Operation does'n exist.")

# age = int(input("Enter your age: "))
# if(age < 18):
#     print("You are under 18,\nSo you can't drive.")
# else:
#     print("you can drive.")

#___TERNARY OPERATOR___     
#---SINGLE LINE---
# food = input("Food : ")
# eat = "yes" if food == "cake" or food == "jalebi" else "no"
# print(eat)

#---CLEVER IF ---
# age = int(input("Enter your age : "))
# vote = ("yes","no") [age<18]
# print(vote)

# __EXPRESSION EXECUTION___
# A,B="2",3
# text = "str"
# print(A,B)
# print(A*text*B)
# print((A+text)*B) 

# num = int(input("Enter your number: "))
# num *= 10
# print("num :",num)

# val1 = int(input("Enter val1:"))
# val2 = int(input("Enter val2:"))
# print("AND Operator:",(val1 >= val2) and (val1 == val2))
# print("OR Operator:",(val1 == val2) or (val1 < val2))
# print(type(val1))

# a = "34" 
# b = 4.51
# print(type(a))
# print(type(b))

# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))
# sum = num1 + num2
# print(sum)

# side = int(input("Enter side of square:"))
# area = side*side
# para = 4*side
# print("Area of square :",area)
# print("Parameter of square :",para)

# num1 = float(input("Enter first number :"))
# num2 = float(input("Enter second number :"))
# avg = (num1+num2)/2
# print("Avg :",avg)

# a = int(input("Enter first number :"))
# b = int(input("Enter second number :"))
# print(a >= b)

#___CONCATENATION,INDEXING,SLICING___
# a = "akshat" 
# b = "kumar"
# str = a + b
# print(str)
# print(len(str))
# print(str[7])
# print(str[2:9])
# print(str[-7:-3])        #negative index

#___STIRING FUNCTION___
# str = "my name is akshat kumar"
# print(str.endswith("ar"))            
# print(str.capitalize())
# print(str.replace("k","a.k"))
# print(str.find("is"))
# print(str.count("a"))

# name = input("Enter your name :")
# print("length :",len(name))
# print(name.count("a"))

# marks = int(input("Enter your marks :"))
# if(marks>=90):
#     grade = "A"
# elif(90>marks and marks>=80):
#     grade = "B"
# elif(80>marks and marks>=70):
#     grade = "C"
# else:
#     grade = "D"
# print("grade of student :",grade)

# #___NESTING___
# age = int(input("Enter your age :"))
# if(age>=18):
#     if(age>=80):
#         print("Cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")

# num = int(input("Enter your number :"))
# if(num%2==0):
#     print(num,"is even number")
# else:
#     print(num,"is odd number")

# num1 = int(input("Enter first number :"))
# num2 = int(input("Enter second number :"))
# num3 = int(input("Enter third number :"))
# if(num1>num2 and num1>num3):
#     print(num1,"is greatest number")
# elif(num2>num1 and num2>num3):
#     print(num2,"is greatest number")
# elif(num1 == num2 and num2 == num3):
#     print("all the number are equal")
# else:
#     print(num3,"is greatest number")

# num = int(input("Enter your number :"))
# if(num%7==0):
#     print(num,"is a multiple of 7")
# else:
#     print(num,"is not a multiple of 7")

# r = float(input("Enter the radius of circle :"))
# area = 3.14*r**2
# para = 2*3.14*r
# print("area of circle:",area)
# print("parameter of circle :",para)

# str = "hey buddy,How can i help you?"
# print(str.replace("d"," "))
# print(len(str))
# print(str.count("y"))
# print(str[:24])
# print(str.find("i"))

# x1 = float(input("Enter x1 coordinate :"))
# x2 = float(input("Enter x2 coordinate :"))
# y1 = float(input("Enter y1 coordinate :"))
# y2 = float(input("Enter y2 coordinate :"))
# dis = ((x2 - x1) + (y2 - y1))**0.5
# print(dis)

#___LISTS___                MUTABLE DATA TYPES
# marks = [54,98,35,65,23]
# student = ["akshat",53,98.5,"utu"]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[1:3])
# print(student[0])
# student[0] = "vanshu"            # MUTABLE
# print(student[0])

# student.append("kumar")          # METHODS
# print(student)    
# marks.sort()                
# print(marks)
# marks.sort(reverse=True)
# print(marks)
# fruits = ["mango","apple","banana"]
# print(type(fruits))
# fruits.sort()
# print(fruits)
# fruits.insert(0,"orange")
# print(fruits)
# fruits.append("papaya")
# print(fruits)
# fruits.remove("orange")
# print(fruits)
# fruits.pop(0)
# print(fruits)

#___TUPLES___              IMMUTABLE DATA TYPES
# tup = (3,5,7,33,64,33,556,645)
# print(type(tup))
# print(tup[3:])
# print(tup.index(556))
# print(tup.count(33))

# animals = [1,2,3]
# an1 = input("Enter first animal name :")
# animals[0] = an1
# an2 = input("Enter second animal name :")
# animals[1] = an2
# an3 = input("Enter third animal name :")
# animals[2] = an3
# print(animals)

# games = []
# game1 = input("enter 1st game :")
# game2 = input("enter 2nd game :")
# game3 = input("enter 3rd game :")
# games.append(game1)
# games.append(game2)
# games.append(game3)
# print(games)

# list = [1,3,5,3,1]
# list1 = list.copy()
# list1.reverse()
# if(list1 == list):
#     print("palindrome")
# else:
#     print("not palindrome")

# tup = ("C","D","A","A","B","B","A")
# tup = tup.count("A")
# print("number of students with the A grade is ",tup)

# list = ["D","A","C","B"]
# list.sort()
# print(list)

#___DICTIONARY___           #MUTABLE 
# dict = { 
#     "name" : "akshat kumar",
#     "cgpa" : 9.5,
#     "subjects" : ["python","DSA","OOPS"],
#     "marks" : "98,97,95",
# }
# dict["name"] = "AKSHAT KUMAR"
# print(dict)

# student = {
#     "name" : "Akshat kumar",
#     "branch" : "CSE",
#     "subjects" : {
#         "phy" : 98,
#         "chem" : 56,
#         "math" : 78, 
#     }
# }                                 #nested dictionary
# print(student["subjects"]["chem"])
# print(student.keys())
# print(list(student.keys()))

# age = int(input("enter your age :"))
# std = input("are you a student (yes/no) :")
# if(age<12):
#     if(std == "yes"):
#         print("ticket price is $5")
#     else:
#         print("ticket price is $8")
# elif(age>=65):
#     if(std == "yes"):
#         print("ticket price is $7")
#     else:
#         print("ticket price is $10")
# else:
#     if(std == "yes"):
#         print("ticket price is $12")
#     else:
#         print("ticket price is $15")


# cont = {
#     "alice" : "555-1234",
#     "bob" : "555-5678",
#     "enna" : "534-8765",
# }

# name = (input("search name :"))
# if(name == "alice"):
#     print("name : alice\ncontact :",cont["alice"])
# elif(name == "bob"):
#      print("name : bob\ncontact :",cont["bob"])
# elif(name == "enna"):
#     print("name : enna\ncontact :",cont["enna"])
# else:
#     print("Contact not found in the book.")

# tup = ("fireworks","weapons","expired_milk")
# cart = ["appples","milk","fireworks","bread"]
# if(cart[0]=="fireworks" or cart[0]=="weapons" or cart[0]=="expired_milk"):
#     print("Alert :",cart[0],"cannot be sold.")
# elif(cart[1]=="fireworks" or cart[1]=="weapons" or cart[1]=="expired_milk"):
#     print("Alert :",cart[1],"cannot be sold.")
# elif(cart[2]=="fireworks" or cart[2]=="weapons" or cart[2]=="expired_milk"):
#     print("Alert :",cart[2],"cannot be sold.")
# elif(cart[3]=="fireworks" or cart[3]=="weapons" or cart[3]=="expired_milk"):
#     print("Alert :",cart[3],"cannot be sold.")
# else:
#     print("All items in your cart are apporeved for purchase.")

# list = []
# list.append(int(input("enter 1st number:")))
# list.append(int(input("enter 2nd number:")))
# list.append(int(input("enter 3rd number:")))
# list.append(int(input("enter 4th number:")))
# list.append(int(input("enter 5th number:")))
# list.sort(reverse=True)
# print(list)

# temp = (int(input("enter temperature :")))
# rain = (input("is it raining (yes or no) :"))
# if(temp<15 and rain == "yes"):
#     print("Wear a heavy waterproof jacket and boots.")
# elif(temp<25 and rain == "no"):
#     print("Wear a heavy coat and scarf.")
# elif(temp>=15 and rain == "yes"):
#     print("Wear a light jacket and bring an umbrella.")
# else:
#     print("Wear a t-shirt and sunglasses.")

# allergens = ("peanuts","shellfish","dairy")
# recipe = ["flour","sugar","peanuts"]
# if(recipe[0] in allergens):
#     print("Alllergy Alert! This recipe contains a restricted allergen.")
# elif(recipe[1] in allergens):
#     print("Alllergy Alert! This recipe contains a restricted allergen.")
# elif(recipe[2] in allergens):
#     print("Alllergy Alert! This recipe contains a restricted allergen.")
# else:
#     print("Recipe is safe from listed allgerens.")

# sub = {
#     "basic" : 9,
#     "standard" : 15,
#     "premium" : 22,
# }
# plan = input("chosen_plan :")
# code = input("if you has promo_code (yes/no) :")
# if(plan in sub):
#     if(plan == "basic" and code == "yes"):
#         print("Promo code appplied! your new monthly total is $4.")
#     elif(plan == "standard" and code == "yes"):
#         print("Promo code appplied! your new monthly total is $10.")
#     elif(plan == "premium" and code == "yes"):
#         print("Promo code appplied! your new monthly total is $17.")
#     elif(plan == "basic" and code == "no"):
#         print("No promo code applied. your monthly total is $9.")
#     elif(plan == "standard" and code == "no"):
#         print("No promo code applied. your monthly total is $15.")
#     else:
#         print("No promo code applied. your monthly total is $22.")
# else:
#     print("There is no plan found.")

# details = {
#     "username" : "coder_pro",
#     "role" : "editor",
#     "is_active" : "True",
# }
# high = ("deleted_database","change_server_setting","ban_user")
# attempted_action = "ban_user"
# if(details["is_active"] == "True"):
#     if(details["role"] == "admin"):
#         print("Action authorized for administrator.")
#     else:
#         print("Access denied:Insufficient privileges for this action.")
# elif(details["is_active"]=="False"):
#     print("Access denied:Account is inactive.")
# else:
#     print("Action excuted successfully.")

# cart = ["wireless_mouse","keyboard","desk_mat"]
# store = ("SAVE20","FREESHIP","WELCOME10","CASH30")
# coupon = (input("entered_coupon :"))
# print("cart_total = $85")
# if(coupon in store):
#     if(coupon == "SAVE20"):
#         print("you got 20% discount on cart_total,\nThe final discounted price is $68.",)
#     elif(coupon == "FREESHIP"):
#         print("you got 30% discount on cart_total,\nThe final discounted price is $59.")
#     elif(coupon == "WELCOME10"):
#         print("you goy 40% discount on cart_total,\nThe final discounted price is $51.")
#     else:
#         print("Valid coupon applied,but no special discount rate matched.")
# else:
#     print("Invalid coupon code.\nOriginal total of $85 applies.")

# account = {
#     "user_name" : "akshat_kumar",
#     "account_type" : "premium",
#     "failed_attempts" : 4,
#     "is_locked" : "False",
# }
# account["failed_attempts"] = int(input("enter failed_attempts:"))
# account["is_locked"] = input("is_locked:")
# if(account["is_locked"] == "False"):
#     if(account["failed_attempts"] >= 5):
#         print("Warning:Account is flagged for high risk.")
#     elif(4>=account["failed_attempts"]>=3):
#         print("Security notice:Multiple failed login attempts detected.")
#     else:
#         print("Account is secure and operating normally.")
# else:
#     print("Account is locked due to security concerns.")

# wtg = {
#     "economy" : 20,
#     "business" : 30,
#     "first_class" : 50,
# }
# clss = input("enter passenger_class :")
# weg = int(input("enter baggage_weight :"))
# if(clss == "economy"):
#     if(wtg["economy"] >= weg):
#         print("Baggage approved. Have a safe flight!")
#     else:
#         print("Overweight bagged! you are",weg-20,"kg over the limit.\nA fee of $",(weg-20)*15,"applies.")
#         print("charge $15 per extra kg.")
# elif(clss == "business"):
#     if(wtg["business"]>=weg):
#         print("Baggage approved. Have a safe flight!")
#     else:
#         print("Overweight bagged! you are",weg-30,"kg over the limit.\nA fee of $",(weg-30)*15,"applies.")
#         print("charge $15 per extra kg.")
# elif(clss == "first_class"):
#     if(wtg["first_class"]>=weg):
#         print("Baggage approved. Have a safe flight!")
#     else:
#         print("Overweight bagged! you are",weg-50,"kg over the limit.\nA fee of $",(weg-50)*15,"applies.")
#         print("charge $15 per extra kg.")
# else:
#     print("NO CLASSES FOUND.")

# name = {
#     "alice" : 97,
#     "bob" : 85,
#     "charlie" : 43,
# }
# target_student = input("enter target_student :")
# if(target_student in name):
#     if(name[target_student] >= 90):
#         print(target_student,"score",name[target_student],"Grade:A(Excellent)")
#     elif(name[target_student] >= 70):
#         print(target_student,"score",name[target_student],"Grade:B(Good)")
#     elif(name[target_student] >= 50):
#         print(target_student,"score",name[target_student],"Grade:C(Need Impovement)")
#     else:
#         print(target_student,"score",name[target_student],"Grade:F(Fail)")
# else:
#     print("Student record does not exist.")

# age = int(input("Enter your age :"))
# is_student = input("is student :")
# price = 43
# if(age<=12):
#     price = 12
# elif(age>=65):
#     price = 10
# else:
#     price = 15
# if(is_student == "yes"):
#     price = price-3
# print(f"the final ticket price is {price}")

# email = input("enter your email :")
# num = email.find("@")
# if("@" in email):
#     print("useranme :",email[:num])
# else:
#     print("Inavlid email address.")
# if(email.endswith(".org") or email.endswith(".com")):
#     print("organization type email.")
# else:
#     print("unable to found eamil type.")

# current_temp = int(input("Enter current temp :"))
# target_temp = int(input("Enter target temp :"))
# if((target_temp - current_temp)>=3):
#     print("Heating Mode : High")
# elif(3>(target_temp - current_temp)>1):
#     print("Heating Mode : Eco")
# elif(target_temp == current_temp):
#     print("Idle:Target reached.")
# else:
#     print("Cooling Mode : Active.")

# password = input("enter a strong password :")
# if(len(password) == 8):
#     if("#"or"@" in password):
#         if(" " not in password):
#             print("Strong Password.")
#         else:
#             print("Weak Password:Check requirements.")
#     else:
#         print("Weak Password:Check requirements.")
# elif(len(password) != 8):
#     print("Invalid length.")
# else:
#     print("Weak Password:Check requirements.")

# task = ["pay bills","email boss","buy groceries"]
# add = input("Add task :")
# task.append(add)
# if(len(task) > 3):
#     print("remove :",task[0])
#     task.pop(0)
#     print("Urgent task completed :",add)
#     print("final task :",task)
# else:
#     print("length of task is less than 3.")

# loc = []
# loc.append(int(input("Enter latitude:")))
# loc.append(int(input("Enter longitude")))
# # loc[0] = "north/south"
# # loc[1] = "east/west"
# if(loc[0] >=0 ):
#     print("Northen hemisphere")
# else:
#     print("Southern hemisphere")
# if(loc[1]>=0):
#     print("Eastern hemisphere")
# else:
#     print("Western hemisphere")

# code = (40,210,95)
# values = input("Enter values between 0 to 255 :")
# if(values<=85):
#     print("Colour : Red")
# elif(values <=170):
#     print("Colour : Green")
# elif(values <=255):
#     print("Colour : Blue")
# elif(values == code):
#     print("Colour : Grayscale shade")
# else:
#     print("Invalid value.")

# menu = {
#     "latte" : 4.50,
#     "espresso" : 3.00,
#     "muffin" : 3.25,
# }
# order_item = input("Enter order_item :")
# quantity = int(input("Enter quantity of oreder_item :"))
# if(order_item in menu):
#     cost = menu[order_item]*quantity
#     if(quantity >=3):
#         cost = (cost)*0.9
#         print("You got 10% discount.")
#     print("Final bill: ",cost)
# else:
#     print("order_item does'n exists.")

# loan = {
#     "title" : "clean code",
#     "days_overdue" : 6,
#     "fine" : 0.0,
# }
# loan["days_overdue"] = int(input("Enter days_overdue :"))
# if(loan["days_overdue"] > 0):
#     fine = 0.5*(loan["days_overdue"])
#     loan["fine"] = fine
# print(loan)

# flight = "BA-402"
# gates = {
#     "AI" : "Terminal 1",
#     "BA" : "Terminal 3",
#     "LH" : "Terminal 2",
# }
# if(flight[0:2] in gates):
#     print("airline code :",flight[0:2])
#     print("gates :",gates[flight[0:2]])
# else:
#     print("UNKNOWN airline code.")

# seats = ["aarav","meera","kabir",'diya']
# print(seats)
# if("meeraa" and "diya" in seats):
#     seats.pop(1)
#     seats.insert(1,"diya")
#     seats.pop(3)
#     seats.insert(3,"meera")
#     print(seats)

# staff = {
#     "E101" : {
#         "name" : "rohan",
#         "dept" : "IT",
#         "active" : True,
#     },
#     "E102" : {
#         "name" : "sara",
#         "dept" : "HR",
#         "active" : False,
#     }
# }
# emp_id = input("Enter emp_id :")
# if(emp_id in staff):
#     if(staff[emp_id]["active"] == True):
#         print("name",staff[emp_id])
#         print("Employee account is active")
#     else:
#         print("Empolyee account is deactive.")
# else:
#     print("emp_id is not exist.")

# order = {
#     "country" : "India",
#     "items" : ["Keyboard","Mouse"],
#     "subtotal" : 1800,
# }
# zones = ("India","Nepal","Bhutan")
# order["contry"] = input("Enter order_country name :")
# order["subtotal"] = int(input("Enter subtotal :"))
# if(order["country"] in zones ):
#     if(order["subtotal"]>=1500):
#         print("Shipping is $0.") 
#     else:
#         print("Shipping is $250.")
# else:
#     print("order_country cannot find.")

# rating = (4.5,3.8,4.2)
# avg = (rating[0]+rating[1]+rating[2])/3
# if(avg>=4.0):
#     print("Top Rated Movies.")
# else:
#     print("Standard Release.")

# 9 34 53%

# taken = ["admin","code123","python_fan"]
# new_user = "guest"
# if(new_user in taken):
#     print("Username taken.")
# else:
#     print("Username available.")

# device = {
#     "name" : "Living room AC",
#     "mode" : "cool",
#     "temp" : 21,
# }

# if(device["mode"] == "cool"):
#     if(device["temp"] < 21):
#         print("Energy saving mode.")
#     else:
#         print("Standard cool.")
# else:
#     print("System idle.")

# stock = {
#     "pens" : 12,
#     "notebooks" : 3,
#     "erasers" : 15,
# }
# check = input("Enter item to check :")
# if(check in stock):
#     if(stock[check] < 5):
#         print("you needed",10-(stock[check]),"to reach 10.")
#         print("Restock notice.")
#     else:
#         print("you don't needed more quantity.")
# else:
#     print(check,"is not in stock.")

# title = "introduction to python programming"
# if title.startswith("introduction"):
#     print(title.title()) 

# scores = [88,95,9,72]
# if(scores[0] < scores[1]):
#     scores[0],scores[1] = scores[1],scores[0]
# print(scores)

# phonebook = {
#     "alice" : "555-1111",
#     "bob" : "555-2222",
# }
# contact = "alice"
# if(contact in phonebook):
#     phonebook[contact] = "555-9999"
# print(phonebook)

# pwd = (input("Enter passsword :"))
# if(pwd[0].isupper()) and (pwd[-1].isdigit()):
#     print("success.")
# else:
#     print("Failure")

#___SET___                 MUTABLE
# set = {2,2,3,4,"Hello world"}
# set1 = {2,54,6,4}
# empty = set()
# print(set)
# print(type(set))
# print(len(set))
# set.add(6)             #METHOD
# set.remove(2)
# set.pop()
# set.clear()
# print(set.union(set1))
# print(set.intersection(set1))

# dict = {
#     "table" : ("a piece of furniture","list of facts & figures."),
#     "cat" : "a samll animal."
# }
# print(dict)

# subject = ["python","java","c++","javascript"]
# print("there are",len(subject),"classroom needed")

# marks = {}
# x = int(input("enter physics : "))
# y = int(input("enter chem : "))
# z = int(input("enter maths : "))
# marks.update({"physics" : x})
# marks.update({"chemistry" : y})
# marks.update({"mathematics" : z})
# print(marks)

# set = {
#     ("int", 9),
#     ("float" , 9.0),
# }
# print(set)

#___LOOPS___
# count = 1
# while count<=12:
#     print(count)
#     count += 1
# print(count)

# i = 1
# while i <=100:
#     print(i)
#     i += 1

# i = 10
# while i>=1:
#     print(i)
#     i -=1

# n = int(input("Enter number : "))
# i = 1
# while i <=10:
#     print(n*i)
#     i += 1

# i = 1
# nums = [1,4,9,16,25,36,49,64,81,100]
# while i < len(nums):
#     print(nums[i])
#     i += 1

# x = int(input("Enter nums : "))
# num = (1,4,9,16,25,36,49,64,81,100)
# i = 0
# while i < len(num):
#     if (num[i] == x):
#         print(i)
#     i += 1

# i = 1 
# while i <=10:
#     if(i == 5):
#         break
#     print(i)
#     i += 1

# i = 0 
# while i <= 7:
#     if(i == 4):
#         i +=1
#         continue  #skip
#     print(i)
#     i += 1

#___FOR LOOPS___
# num = [7,3,68,98]
# for val in num:
#     if( val == 68):
#         print(val)
#         break
#     print(val)

# nums = [1,4,9,16,25,36,49,64,81,100]
# for val in nums:
#     print(val)

# nums = [1,4,9,16,25,36,49,64,81,100]
# x = 16
# for val in nums:
#     if(val == x):
#         print(val)
#         break
#     print(val)

# seq = range(1,8)
# print(seq[0])
# for i in range(2,9):
#     print(i)
# for i in range(0,10,2):
#     print(i)
# for i in range(1,101):
#     print(i)
# for i in range(101,0,-1):
#     print(i)
# n = int(input("enter number : "))
# for i in range(1,11):
#     print(n*i)

# n = 10
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print("Total number of sum is : ",sum)
# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact)

# item = [("apple","fruit",120),("milk","dairy",60),("banana","fruits",50)]
# dict = {}
# for idx  in range(len(item)-1):
#     dict.update({idx})
#     idx += 1
# print(dict)

#___FUNCTIONS___
# function definition
# def cal_sum(a,b):
#     sum = a + b
#     print(sum)
#     return sum
# cal_sum(5,9)
# cal_sum(8,10) 
# def avg(a,b,c):
#     avg = (a+b+c)/3
#     print(avg)
#     return avg
# avg(8,98,98)

# val = [23,5,6,597,45]
# print(len(list))
# print(list)
# def print_len(list):
#     print(len(list))
# print(len(val))
# def converter(usd_val):
#     inr_val = usd_val*83
#     print(inr_val)
# converter(8)

# def num(a):
#     if(a%2==0):
#         print("EVEN")
#     else:
#         print("ODD")
# num(int(input("Enter a number :")))
# def show(n):
#     for i in range(n,0,-1):
        # i -= 1
        # print(i)
# show(5)

#___RECURSION___
# def show(n):
    #  if(n==0):         #base case
#           return
#      print(n)
#      show(n-1)
# show(5)

# list1 = [1,2,3,4,5]
# large = list1[0]
# for i in list1:
#     if(i>large):
#         small = large
#         large = i
# print(small)

# n = 3
# for i in range (n):
#     for j in range (n):
#         if i == 0 or i == n-1 or j == 0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end= " ")
#     print()

# scores = [78,92,85,92,67,89]
# large = scores[0]
# for i in scores:
#     if(i>large):
#         small = large
#         large = i
#         print(f"greates number in list is {i}")
#         print(f"second greates number in this list is :{small}")

# raw = "aaabbcdddda"
# for i in raw:
#     rep = raw.count(f"{i}") 
#     print(rep)
# raw = "aaabbcdddda"
# compressed = ""
# count = 1
# for i in range(1, len(raw)):
#     if raw[i] == raw[i - 1]:
#         count += 1
#     else:
#         compressed += raw[i - 1] + str(count)
#         count = 1
# compressed += raw[-1] + str(count)
# print("Compressed:", compressed)

# i = 1
# while i<=10:
#     print(i)
#     i += 1
# for i in range(-10,-0):
#     print(i)
# for i in range(0,4):
    # print(i)
    # print("Done")
# print("Done")
# n = 10
# sum = 0
# for i in range(n+1):
#     sum += i
# print(sum)
# n = int(input("enter number : "))
# mul = 0
# for i in range(1,11):
#     mul = i*n
#     print(mul)
# n = int(input("enter number : "))
# cube = 0
# for i in range(n+1):
#     cube = i**3
#     print(f"number is {i} and the cube is {cube}")
# num = [12, 75, 150, 180, 145, 525, 50]
# for i in num:
#     if(i>500):
#         break
#     if(i>150):
#         continue
#     if(i%5==0):
#         print(i)
# list1 = [10,20,10,30,10,40,50]
# target =int(input("Enter number to count : "))
# for i in list1:
#     if(i == target):
#         print(list1.count(target))
#         break
# list = [10,20,30,40,50,60,70,80,90,100]
# for i in range(len(list)+1):
#     if(i%2!=0):
#         print(list[i])
# list = [10,20,30,40,50]
# for i in range(len(list)-1,-1,-1):
#     print(list[i])
# original = "python"
# reverse = ""
# for i in original:
#     reverse = i + reverse
# print(reverse)
# name = input("enter your name : ")
# reverse = ""
# for i in name:
    # reverse = i + reverse
# print(reverse)
# sentence = input("Enter your sentence : ")
# vowel = ["a","e","i","o","u"]
# vow_count = 0
# cons = 0
# for i in sentence:
#     if i in vowel:
#         vow_count += 1
#     elif(i == " "):
#         cons += 0
#     else:
#         cons += 1
# print(f"total number of vowels in this sentence is : {vow_count}")
# print(f"total number of consonants in this sentence is : {cons}")
# num = int(input("Enter number : "))
# count = 0
# while num!=0:
#     num = num // 10
#     count = count + 1
# print(count)
# num = int(input("Enter the number : "))
# str_num = str(num)
# reversed_num = " "
# for char in str_num:
#     reversed_num = char + reversed_num
# print(reversed_num)
# num = 3
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end = " ")
#     print("")
# num = 3
# for i in range(num+1,-1,-1):
#     for j in range(i+1,0,-1):
#         print(j,end = " ")
#     print("")
# for i in range(1,21,2):
#     print(i)
# correct_pin = "7391"
# attempts = ["1111","2222","7391","9999"]
# tries = 3
# while tries<=3:
#     if(correct_pin in attempts):
#         print("Access Granted.")
#         break
# else:
#     print("Card Blocked.")
# items = [("Apple","Fruit",120),("Milk","Dairy",60),("Banana","Fruits",50),("Cheese","Dairy",180)]
# idx = 0
# for i in items:
#     print(i)
# num = [2,7,11,15,3,6]
# target = 9
# for i in num:
#     if(num[i]+num[i+1] == 9):
#         print(i)
# for i in range(1500,2701):
#     if(i%7 == 0 and i%5==0):
#         print(i)
# num = 2
# for i in range (0,11,2):
#     num1 = num**i
#     print(num1)
# n = int(input("Enter your number : "))
# sum = 0
# while n>0:
#     sum = sum + (n%10)
#     n //= 10
# print(sum)

#___RECURSION___
# def show(a):
#     if(a == 0):
#         return
#     print(a)
#     show(a-1)
# show(4)
# print("END!")
# def fact(a):
#     if(a == 0 or a == 1):
#         return 1
#     return a * fact(a-1)
# n = int(input("Enter your number : "))
# print(fact(n))
# def demo(name,age):
#     print(f"your name is {name}\nyour age is {age}")
# name = input("Enter your name : ")
# age = int(input("enter your age : "))
# demo(name,age)
# def fun(fun1,fun2):
#     print("Printing values.")
#     for i in range (len(fun1)-1):
#         print(fun1[i])
#     print("Printing value")
#     for j in range (len(fun2)-1):
#         print(fun2[j])
# fun1 = 34,43,75,479,23
# fun2 = 542,7,3,67
# fun(fun1,fun2)
# def calculation(num1,num2):
#     add  = num1 + num2
#     sub = num1 - num2
#     return add,sub
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# cal = calculation(num1,num2)
# print(cal)
# def show_empolyee(name,salary=9000):
#     print("Employee name is :",name,"\nSalary is :",salary)
# show_empolyee("ben",12000)
# def cal(a,b):
#     sum = a + b
#     sum += 5
#     return sum
# a = 10
# b = 10
# call = cal(a,b)
# print(call)
# def addition(num):
#     if num :
#         return num + addition(num-1)
#     else:
#         return 0
# add = addition(10)
# print(add)
# def display_student(name,age):
#     print(name,age)
# show_student = display_student
# show = show_student("Akshat",19)
# def list(a,b):
#     list1 = []
#     for i in range(a,b+1):
#         if(i%2==0):
#             list1.append(i)
#     print(list1)
# a = int(input("Enter the starting range : "))
# b = int(input("Enter the ending range : "))
# list(a,b)
# def list(x):
#     large = x[0]
#     for i in x:
#         if(i>large):
#             large = i
#     return large
# x = [4, 6, 8, 24, 12, 2]   
# print(list(x))
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
        
# print_info(name="Alice", age=30, city="New York")
# def dict(**adi):
#     for key,value in adi.items():
#         print(f"{key} : {value}")
# dict(name="Alice", age=30, city="New York") 
# def fact(num):
#     if(num == 0 or num == 1):
#         return 1
#     else:
#         return num*fact(num-1)
# num = int(input("Enter number for factorial : "))
# fact = fact(num)
# print(fact)
# addition = lambda a,b : a + b
# addition = addition(3,5)
# print(addition)
# num = int(input("enter the number : "))
# for i in range(1,num+1):
#     cube = i**3
#     print(f"The current number i :{i} and the cube is :{cube}.")
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in range(0,len(numbers)-1):
#     if (numbers[i]>500):
#         break
#     if(numbers[i] > 150):
#         continue
#     if(numbers[i]%5 == 0):
#         print(numbers[i])
# num = 12321
# temp = num
# reverse = 0
# while num>0:
#     digit = num % 10
#     reverse = (reverse*10) + digit
#     num = num//10
# if(reverse == temp):
#     print("The number is palindrome.")
# else:
#     print("The number is not palindrome.")
# num = 6
# print(num)
# while num != 1:
#     if(num%2 == 0):
#         num = num//2
#     else:
#         num = (num*3)+1
#     print(num)
# number = 153
# temp = number
# sum = 0
# while number>0:
#     digit = number % 10
#     cube = digit**3
#     sum += cube
#     number = number//10
# if(temp == sum):
#     print("Number is armstrong.")
# else:
#     print("Number is not armstrong.")
# for i in range(1,21,2):
#     print(i,end=" ")
# n = 5
# for i in range(n):
#     for j in range (n):
#         if(i == 0 or i == n-1 or j == 0 or j == n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end = " ")
#     print()
# list1 = [1,2,3,4]
# list2 = []
# sum = 0
# for i in list1:
#     sum += i
#     list2.append(sum)
# print(f"surrent list : {list2}")
# scores = {
#     "Alice": 85,
#     "Bob": 70, 
#     "Charlie": 95, 
#     "David": 60,
# }
# passing_student = {}
# threshold = 75
# for key,values in scores.items():
#     if(values>75):
#         passing_student[key] = values
# print(passing_student)
# list_a = [1, 2, 3, 4, 5]
# list_b = [4, 5, 6, 7, 8]
# list_c = []
# for i in list_a:
#     for j in list_b:
#         if(i == j):
#             list_c.append(i)
# print("common elements is : ",list_c)
# list = [4,3,2,1,6]
# even = []
# odd = []
# for i in list:
#     if(i%2 == 0):
#         even.append(i)
#         even.sort()
#     else:
#         odd.append(i)
#         odd.sort()
# final = even + odd
# print(final)
# list = [1,2,3,4,5]
# k = 2
# for i in range(len(list)-1,-1,-1):
#     for j in range(k):
#         list[j],list[i] = list[i],list[j]
# print(list)
# num = [2,7,11,15,3,6]
# target = 9
# for i in num:
#     for j in range(i):
#         if(i+j == target ):
#             sum = (i,j)
#             print(sum,end='')
# result = ("W","W","L","W","L","W","L","W")
# winning_streak = 0
# loss_streak = 0
# for i in result:
#     if(i=="W"):
#         winning_streak = winning_streak+1
#     else:
#         loss_streak = loss_streak + 1
# print(f"Winning streak is :{winning_streak}\nLoss streak is :{loss_streak}")
# f = open("D:\python\Coding\demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

#___PROBLEMS FOR LOGIC BUILDING___
#_CONDITIONAL THINKING__

# Take a number and print whether it's positive ,negative or zero
# num = int(input("Enter your number : "))
# if(num>0):
#     print(f"{num} is a positive number.")
# elif(num<0):
#     print(f"{num} is a negative number.")
# else:
#     print(f"The number is 0.")

# Check if a number is even or odd.
# num = int(input("Enter your number : "))
# if(num%2 == 0):
#     print(f"{num} is even number.")
# else:
#     print(num,"is odd number.")

# Check if a number is divisible by 5.
# num = int(input("Enter your number : "))
# if(num%5 == 0):
#     print(f"{num} is divisible by 5.")
# else:
#     print(num,"is not divisible by 5.")

# Check if anumber is divisible by 3 & 5.
# num = int(input("Enter your number : "))
# if(num%3 == 0 and num % 5 == 0):
#     print(num,"is divisible by 3 & 5.")
# else:
#     print(num,"is not divvisible by 3 & 5.")

# Check if a year is a leap year.
# year = int(input("Enter year : "))
# if(year%4 == 0):
#     print(year,"is a leap year.")
# else:
#     print(year,"is not a leap year.")

# Take two number and print the larger one.
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# if(num1>num2):
#     print(f"{num1} is larger than {num2}.")
# elif(num1 == num2):
#     print("Both numbers are equal.")
# else: 
#     print(f"{num2} is larger than {num1}.")

# Take three number and print largerest.
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# num3 = int(input("Enter thied number : "))
# if(num1>num2 and num1>num3):
#     print(num1,"is largest one.")
# elif(num2>num1 and num2 > num3):
#     print(num2,"is largest one.")
# elif(num1 == num2 and num2 == num3):
#     print("all three numbers are equal.")
# else:
#     print(num3,"is largest one.")

# Take a temperature value and print "Cold" ,"Warm" or"Hot" using range conditions.
# temp = int(input("Enter the tempeature : "))
# if(temp >= 35):
#     print("temperature is HOT.")
# elif(temp<= 20):
#     print("temperature is COLD.")
# else:
#     print("temperature is WARM.")

# Take a character and check if its's a vowel and consonent.
# char = input("Enter a character : ")
# vowel = ("a","e","i","o","u")
# if(char in vowel):
#     print(char,"is a vowel.")
# else:
#     print(char,"is a consonent.")

#  Take a character and check whether it’s uppercase, lowercase, a digit, or a special character.
# char = input("Enter a character : ")
# if(char == char.isupper()):
#     print("it's a uppercase.")        #pending
# elif(char == char.islower()):
#     print("it's a lowercase.")
# # elif(char == char.digit()):
# #     print("it's a digit.")
# else:
#     print("it's a special charcter.")

# Take three sides and check if they from a valid triangle.
# a = int(input("Enter first side : "))
# b = int(input("Enter second side : "))
# c = int(input("Enter third side : "))
# if((a+b)>c):
#     if((b+c)>a):
#         if((a+c)>b):
#             print("Valid triangle side.")
# else:
#     print("Unvalid traingel sides.")

# If the side from a valid triangle , determine whether it is equilateral,isosceles,or scalence.
# a = int(input("Enter first side : "))
# b = int(input("Enter second sie : "))
# c = int(input("Enter third side : "))
# if(a == b == c):
#     print("Equilateral triangle")
# elif(a == b or b == c or a == c):
#     print("Isosceles traingle")
# else:
#     print("Scalene traingle")

# Take marks(0-100) and print the corresponding grade(A/B/C/D/F)
# marks = int(input("Enter marks : "))
# if(marks>=90):
#     grade = "A"
# elif(marks>=80):
#     grade = "B"
# elif(marks>=70):
#     grade = "C"
# elif(marks>=50):
#     grade = "D"
# else:
#     grade = "F"
# print("Grade :",grade)

# Check if one of two numbers is a multiple of the other.
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter secind number : "))
# if(num1%num2 == 0):
#     print(f"{num1} is multiple of {num2}.")
# elif(num2%num1==0):
#     print(f"{num2} is multiple is {num1}.")
# else:
#     print("one of two given numbers is not a multiple of the other.")

# Take the hour of the day(0-23) and print.
# hour = int(input("Enter hour (0-23) : "))
# if(4<hour<11):
#     print("Good morning")
# elif(11<hour<17):
#     print("Good afternoon")
# elif(17<hour<20):
#     print("Good evening")
# else:
#     print("Good night")

# Check voting eligibility for a given age(18+)
# age = int(input("Enter your age : "))
# if(age >= 18):
#     print("You are eligible for voting.")
# else:
#     print("You are not eligible for voting.")

# Take two numbers and determine whether both are even, both are odd, or one is even and one is odd.
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# if(num1%2==0 and num2%2==0):
#     print("Both numbers are even.")
# elif(num1%2 == 0):
#     print(f"{num1} is even and {num2} is odd.")
# elif(num2%2==0):
#     print(f"{num2} is even and {num1} is odd.")
# else:
    # print("Both are odd.")
 
# Take an alphabet character and check if it lies between "a" and "m" or "n" and "z".
# char = input("Enter an alphabet : ")
# if("a"<char<"m"):
#     print("alphabet lies between a and m.")
# elif("n"<char<"z"):
#     print("alphabet lies between n and z.")
# else:
#     print("not a lowercase alphabet.")

# Take a day number (1-7) and print the corresponding day name.
# day = int(input("Enter day number : "))
# if(day == 1):
#     name = "sunday"
# elif(day == 2):
#     name = "Monday"
# elif(day == 3):
#     name = "Tuesday"
# elif(day == 4):
#     name = "Wednesday"
# elif(day == 5):
#     name = "Thrusday"
# elif(day == 6):
#     name = "Friday"
# elif(day == 7):
#     name = "Saturday"
# else:
#     name = "Invalid number."
# print("It's",name)

# Take a month number (1-12) and print the number of days in that month(ignore leap year).
# month = int(input("Enter month number : "))
# if(month%2 == 0 and 0<month<=6):
#     days = 30
# elif(month == 9,11):
#     days = 30
# elif(month%2==0 and 6<month<=12):
#     days = 31
# else:
#     days = "invalid month number."
# print(days)

# Take a 3-digit number and check if all digit are distinct.
# num = int(input("Enter 3-digit number : "))
# str_num = str(num)
# if(str_num[0] == str_num[1] == str_num[2]):
#     digit = "Equal digits."
# elif(str_num[0] == str_num[1] or str_num[1] == str_num[2] or str_num[0] == str_num [2]):
#     digit = "Two distinct digits."
# else:
#     digit = "Distinct digits."
# print(digit)

# Take a 3-digit number and determine if the middle digit is the largest,smallest,or neither.
# num = int(input("Enter 3-digit number : "))
# first = num%10
# second = (num//10)%10
# third = (num//100)%10
# if(first<second and second>third):
#     print("Middle digit is largest.")
# elif(first>second and second<third):
#     print("Middle digit is smallest.")
# elif(first == second == third):
#     print("Digits are equals.")
# else:
#     print("Middle digit is not largest and smaller.")

# Take a 4-digit number and check if the first and last digit are equal.
# num = int(input("Enter 4-digit number : "))
# str_num = str(num)
# if(str_num[0] == str_num[3]):
#     print("first and last digit are equals.")
# else:
#     print("first and last digit are not equal")

# Check whether a given integer is single-digit,double-digit,or multi-digit
# num = int(input("Enter integer : "))
# str_num = str(num)
# if(len(str_num) == 1):
#     print("Single digit number.")
# elif(len(str_num) == 2):
#     print("Double digit number.")
# else:
#     print("Multi digit number.")

# Check if a numbe is a multiple of 7 or ends with 7.
# num = int(input("Entet your number : "))
# if(num%7==0 and num%10 == 7):
#     print(f"{num} is multiple of 7 and ends with 7.")
# elif(num%7==0 and num%10!=7):
#     print(f"{num} is multiple of 7 but not ends with 7.")
# elif(num%10==7 and num%7!=0):
#     print(f"{num} is ends with 7 but not multiple of 7.")
# else:
#     print(f"{num} is not a multiple of 7 and not ends with 7.")

# Take coordinates(x,y) and determine which quadrant yhe point lies in.
# x = int(input("Enter x coordinate : "))
# y = int(input("Enter y coordinate : "))
# if(0<x<=90):
#     quad = "1st Quadrant"
# elif(90<x<=180):
#     quad = "2nd Quadrant"
# elif(180<x<=270 or x<=-90):
#     quad = "3rd Quardrant"
# else:
#     quad = "4th Quadrant"
# if(0<y<=90):
#     quadrant = "1st Quadrant"
# elif(90<y<=180):
#     quadrant = "2nd Quadrant"
# elif(180<y<=270 or y<=-90):
#     quadrant = "3rd Qradrant"
# else:
#     quadrant = "4th Quadrant"
# print(f"Quadrant of x :{quad}\nQuadrant of y :{quadrant}")

# Check if an amount can be evenly divided into 2000,500, and 100 currency notes
# amount = int(input("Enter amount : "))
# if(amount%100 == 0):
#     notes = int(amount/100)
#     if(amount%500 == 0):
#         notes1 = int(amount/500)
#     else:
#         notes1 = "Cannot be divided"
#     if(amount%2000 == 0):
#         notes2 = int(amount/2000)
#     else:
#         notes2 = "Cannot be divided"
# else:
#     notes = notes1 = notes2 = "Cannot be divided"
# print(f"100 Currency notes {notes}\n500 Currency notes {notes1}\n2000 Currency notes {notes2}")

# Check if a number lies within the range[100,999]
# num = int(input("Enter your number : "))
# if(100<num<999):
#     print(num,"lies within the range [100,999].")
# else:
#     print(num,"isn't lies within the range [100,999].")

# Take two angles of a triangle and compute the third angle.
# angle1 = int(input("Enter first angle : "))
# angle2 = int(input("Enter second angle : "))
# angle3 = 180-(angle1+angle2)
# if(angle3>0):
#     print("Third angle :",angle3)
# else:
#     print("These angles can't make a triangle.")    

# Check whether a number is a perfect square(without using the square root function).
# squ = int(input("Enter the number : "))
# root = int(squ**.5)
# if(squ%root == 0):
#     print("It's a perfect square of",root)
# else:
#     print("It's not a perfect square.")

# Take a character and check if it is a letter,a digit,or neither.
# char = input("Enter character : ")
# if char.isalpha():
#     print("It is a letter.")
# elif char.isdigit():
#     print("It is a digit.")
# else:
#     print("It is a special character.")

# Take a number and print "Fizz" if divisible by 3,"Buzz" if divisible by 5 and "FizzBuzz" if divisible by both.
# num = int(input("Enter your number : "))
# if(num%3 == 0 and num%5 == 0):
#     print("FizzBuzz")
# elif(num%3==0):
#     print("Fizz")
# elif(num%5==0):
#     print("Buzz")
# else:
#     print("Nmber is not divisible by 3 & 5.")

# Take three number and print the median value (neither maximum nor minimum).
# num = int(input("Enter three digit number : "))
# ones = num%10
# tens = (num//10)%10
# hundred = (num//100)
# if(ones<tens<hundred or hundred<tens<ones):
#     median = tens
# elif(tens<ones<hundred or hundred<ones<tens):
#     median = ones
# elif(ones<hundred<tens or tens<hundred<ones):
#     median = hundred
# elif(ones == tens == hundred):
#     median = "All three digits are equal."
# print(f"Median : {median}")

# Take 24-hour time (hour and median) and print whether it is AM or PM.
# print("--24 HOUR TIME--")
# hour = int(input("Enter hours : "))
# min = int(input("Enter minutes : "))
# if(00 <=hour< 12):
#     print("Tt's AM.")
# elif(12<=hour<=23):
#     print("It's PM")
# else:
#     print("Invalid Time!")

# Take income and age,and check if eligible for tax(age>18 and income>5,00,000).
# age = int(input("Enter your age : "))
# income = int(input("Enter your income : "))
# if(age>18 and income>500000):
#     print("Eligible for tax.")
# else:
#     print("Not eligible for tax.")

# Take two number and check if both are positive and their sum is less than 100.
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# sum = num1 + num2
# if(0<num1 and 0<num2):
#     print("Both numbers are positive.")
# elif(0<num1):
#     print(f"Only {num1} is positive.")
# elif(0<num2):
#     print(f"Only {num2} is positive.")
# else:
#     print("Both are Negative.")
# if(sum < 100):
#     print("Sum of both numbers are less than 100.")
# else:
#     print("Sum of both numbers are equal and more than 100.")

# Take a single digit (0–9) and print its word form (“Zero” to “Nine”).
# num = int(input("Enter number from 0 to 9 : "))
# if(num == 0):
#     print("ZERO")
# elif(num == 1):
#     print("ONE")
# elif(num == 2):
#     print("TWO")
# elif(num == 3):
#     print("THREE")
# elif(num == 4):
#     print("FOUR")
# elif(num == 5):
#     print("FIVE")
# elif(num == 6):
#     print("SIX")
# elif(num ==7):
#     print("SEVEN")
# elif(num == 8):
#     print("EIGHT")
# elif(num == 9):
#     print("NINE")
# else:
#     print("Invalid Number.")

# Take a weekday number (1-7) and determine if it is a weekday or weekend.
# num = int(input("Enter weekday number : "))
# tup = (1,2,3,4,5)
# if(num in tup):
#     print("It is a weekday.")
# elif(num == 6 or num == 7):
#     print("It is a weekend.")
# else:
#     print("Invalid weekday number.")

# Take electricity units consumed and calculate the bill as per slabs (using if-else). 
# unit = int(input("Enter electricity unit : "))
# copy_unit = unit
# if(copy_unit<=100):
#     slabs = 3.00
#     copy_unit = copy_unit-100
# elif(0<copy_unit<=100):
#     slabs = 4.50
#     copy_unit = copy_unit-100
# elif(0<copy_unit<=100):
#     slabs = 6.00
#     copy_unit = copy_unit-100
# else:
#     slabs = 7.50
# bill = slabs*unit
# print("___ELECTRICITY BILL____\n")
# print(f"Toatal units consumed : {unit}\nTotal amount : {bill}")

# Take a password string and check basic rules(length>=8 and contains at least one digit).
# password = input("Enter your password : ").strip()
# if(len(password)>=8):
#     if any(char.isdigit() for char in password):
#         print("It is a valid password.")
#     else:
#          print("Password contains at least one digit.")
# elif(len(password)<8):
#     print("Password length should be 8 or more.")
# else:
#     print("Invalid password.")

# Take coordinates(x,y) and check if the point lies on the X-axis,Y-axis,or at the origin.
# x = int(input("Enter X-axis coordinate : "))
# y = int(input("Enter Y-axis coordinate : "))
# if(x == 0 and y == 0):
#     print("Coordinates at the origin.")
# elif(y == 0):
#     print("Coordinates lies on the X-axis.")
# elif(x == 0):
#     print("Coordinates lies on the Y-axis.")
# else:
#     print("Coordinates doesn't lies in X and Y axis.")

# Take day and month and check if it froms a valid calender date(ignore leap years).
# month = int(input("Enter month : "))
# date = int(input("Enter date : "))
# if(0<month<=7):
#     if(month%2 == 0 and 0<date<=30):
#         print("Valid calender date.")
#     elif(month%2!=0 and 0<date<=31):
#         print("Valid calender date.")
#     else:
#         print("Invalid calender date.")
# elif(7<month<=12):
#     if(month%2 == 0 and 0<date<=31):
#         print("Valid calender date.")
#     elif(month%2!=0 and 0<date<=30):
#         print("Valid calender date.")
#     else:
#         print("Invalid calender date.")
# else:
#     print("Invalid calender month.")

# Take two dates (day and month) and determine which one comes first in the calender.
# day1 = int(input("Enter first day : "))
# month1 = int(input("Enter first month : "))
# day2 = int(input("Enter second day : "))
# month2 = int(input("Enter second month : "))
# if(month1<month2):
#     earlier = day1,month1
# elif(month2<month1):
#     earlier = day2,month2
# elif(month1 == month2):
#     if(day1<day2):
#         earlier = day1
#     elif(day2<day1):
#         earlier = day2
#     else:
#         earlier = "same date."
# else:
#     earlier = "Invalid date."
# print("Earlier date is :",earlier)

# Count the number of digit in a given number.
# num = int(input("Enter the number : "))
# str_num = str(num)
# digit = 0
# for i in str_num:
#     digit += 1
# print(f"Number have {digit} digits.")

# Print the reverse of a given number and check if the number is palindrome.
# num = int(input("Enter your number : "))
# str_num = str(num)
# copy_num = ""
# for i in range(len(str_num)-1,-1,-1):
#     copy_num = copy_num + str_num[i]
# if(copy_num == str_num):
#     print("The number is palindrome.")
# else:
#     print(f"The number is not palindrome.\nReverse of {num} is {copy_num}.")

# Print the square of the numbers from 1 to n.
# num = int(input("Enter your number : "))
# for i in range(1,num+1):
#     cube = i**3
#     print(f"Cube of {i} is : {cube}")

# Print all number between a and b divisible by 7.
# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# for i in range(a,b+1):
#     if(i%7==0):
#         print(i,end=" ")

# Print all number whose sum of digit is even(1-100).
# for i in range(1,100):
#     first_digit = i%10
#     second_digit = i//10
#     sum = first_digit + second_digit
#     if(sum%2==0):
#         print(i,end=" ")

# Count how many number between 1-500 are divisible by 7 but not by 5.
# count = 0
# for i in range(1,501):
#     if(i%7==0 and i%5!=0):
#         count += 1
# print(f"There are {count}.")

# Print number between that are palindrome between 1-500.
# for i in range(1,501):
#     str_i = str(i)
#     reverse_i = str_i[::-1]
#     if(str_i == reverse_i):
#         print(str_i)

# Print factorial of each number from 1 to n.
# n = int(input("Enter the number : "))
# factorial = 1
# for i in range(1,n+1):
#     factorial *= i
#     print(f"Factorial of {i} is {factorial}")

# Print number from 1 to n using recursion.
# def number(n):
#     if n == 0:
#         return
#     number(n-1)
#     print(n,end=" ")
# n = int(input("Enter the number : "))
# number(n)

# Print numbers from n to down 1 using recursion.
# def number(n):
#     if n == 0:
#         return
#     print(n,end=" ")
#     number(n-1)
# n = int(input("Enter your number : "))
# number(10)

# Print only even numbers from 1 to n recursively.
# def even(n):
#     if n == 0:
#         return
#     even(n-1)
#     if(n%2==0):
#         print(n,end=" ")
# even(n = int(input("Enter the number : ")))

# Print only odd numbers from 1 to n recursively.
# def odd(n):
#     if n == 0:
#         return
#     odd(n-1)
#     if(n%2!=0):
#         print(n,end=" ")
# n = int(input("Enter the number : "))
# odd(n)

# Print sum of first n natural numbers recursively.
# def natural_sum(n):
#     if n == 0:
#         return 0
#     return n + natural_sum(n-1)    
# print(natural_sum(9))

# Print factorial of a number recursively.
# def factorial(n):
#     if n == 0:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

