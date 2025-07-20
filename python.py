print('Hello NauRaa From Python Language')
#Tasks About Basics 
#1 
def classify_temperature(degree):
    if degree <float(10):
        print('Very Cold')
    elif degree == float(10) and degree < float(25):
        print('Nice Weather!')    
    else:
        print('Very Hot!')

print(classify_temperature(9)) # very cold

#--------------------------------------------------
#2

sensor_value=int()

if sensor_value <0 or sensor_value > 100:
    print('Wrong Reading!')
else:
    print('Right'+ str((sensor_value)))

print(sensor_value) 

#----------------------------------------------
#4

def predict_age_group(age):
    if age<18:
        print('a child!')
    elif age == 18 and age <=60:
        print('An adult!')
    else:
        print('Old Age!')

print(predict_age_group(int(20)))

#----------------------------------------------
#4

def analyze_student(math , programming , english):
    if int( math + programming + english) / 3 >= 85:
        print('Exellent')
    elif int( math + programming + english) / 3 ==70 and int( math + programming + english) / 3<=85:
        print('Good')
    elif int( math + programming + english) / 3 <70:
        print('You need Improving!')
    return int( math + programming + english) / 3
print(analyze_student(100,60,80)) 
#معرفتهاش 
#-----------------------------------------------
#5
def simple_ai_bot(name, mood):
    if mood== 'Happy':
        print('Im Happy For You '+str(name))
    elif mood=='Sad':
        print('Im Here For You ..'+ str(name))
    else:
        print('I hope a Nice Day For You ' +str(name))

print(simple_ai_bot('NauRaa', 'super'))


#-----------------------------------------
#Tasks From Elzero web school
#1
name1= """
"Name: Osama"
"Age: 38"
"Country: Egypt"

"""
#-----------------------------------------------
print(name1)
name2={
'Name':'Osama' ,
'Age':'38',
'Country':'Egypt'
}
print('Your Name is:'+ name2['Name']+'\n Your Age is:'+name2['Age'])

#-----------------------------------------
#2
welC= 'Hello, '
idenT= 'My Name Is Osama And Iam 38 Years Old and I Live in Egypt'
print(welC + idenT)
#"Hello, My Name Is Osama And Iam 38 Years Old and I Live in Egypt."

#-----------------------------------------
print((type(name1)));print((type(idenT)));print((type(welC)))
#-----------------------------------------
name11='NauRaa'
age11='30'
country11='Tanta'
print('Hello '+name11+'," How You Doing \ """ Your Age Is "'+age11+' + And Your Country Is: '+country11)

#"Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt
#-----------------------------------------
print('Hello '+name11+'," How You Doing \ \n""" Your Age Is "'+age11+' + \n And Your Country Is: '+country11)
#-----------------------------------------

namee= 'Elzero'
print('Seconed letter is: '+ (namee[1]) +'\n'+'Third Letter is: '+ namee[2])

#-----------------------------------------
print(10);print(11.20);print(round(5.27));print(pow(2,3))
print(float(10));print(int(1.85))
#-----------------------------------------
num=10
print(f"{num:.10f}")
#-----------------------------------------
num1 = 159.650
print(int(num1))
print(type(int(num1)))
#-----------------------------------------
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(f'"{friends[0]}"=> Method One')
print(f'"{friends[0][0:5]}"=> Method Two')
print(f'"{friends[4]}"=> Method Three')
print(f'"{friends[4][0:7]}"=> Method Three')

# Needed Output
# "Osama" => Method One
# "Osama" => Method Two
# "Mahmoud" => Method One
# "Mahmoud" => Method Two
#---------------------------------------

friends1 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

friends1 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

result = friends1[:3]
result.append("Elzero")
result.append("Elzero")
print(result)

# Needed Output
# ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]
#------------------------------------
#1
result= (5 + 3) * 2 ** 3 / 4
print(float(result))
# (5 + 3) * 2 ** 3 ÷ 4
# الناتج النهائي لازم يطلع float

#---------------------------
#2
a = 15
b = 4
print(f'Remainder ={a%b}')
print(f'Floor Division ={a//b}')
print(f'Division ={a/b}')
#Remainder = ?
#Floor Division = ?
#Division = ? 

#------------------------
#3
friendsz = ["Ahmed", "Sayed", "Ali"]
friendsz.insert(0,'Osama')
print(friendsz) #1

friendsz.append('Mahmoud')
print(friendsz) #2

friendsz.remove('Ali')
print(friendsz) #3

#-------------------------------
#4
list1 = ["AI", "Python", "ML"]
list2 = ["Data", "Math"]

list1.extend(list2)
print(list1) #1

list1.sort(reverse=True)
print(list1)#2

#-------------------------------
#5

nums = (1, 3, 5, 3, 1, 3)

print(nums.count(3)) #1
print(nums.index(1)) #2
#------------------------------
#6
a = {"Python", "AI", "ML"}
b = {"Data", "AI", "Deep Learning"}
#هل فى ميثود بتعمل سيرش جوا ال set!!
#مش عافة اطبع العناصر المشتركة بينهم 'AI'
print(a.intersection(b))#1
print(a.difference(b)) #2
a.update(b)
print(a)#3

#-------------------------------
#7
emptySet= set()
emptySet.add("Python")
emptySet.add("Python")
emptySet.add('AI')
emptySet.add("AI")
emptySet.add("Math")
print(emptySet)
"Python", "Python", "AI", "AI", "Math"

#---------------------------
#1
x=7
y=3

print(f'Sum={x+y}')
print(f'Sub={x-y}')
print(f'Mul={x*y}')
print(f'Power={x**y}')
print(f'Remainder ={x%y}')
print(f'Floor Division ={x//y}')

#Sum = ?
#Sub = ?
#Mul = ?
#Power = ?
#Remainder = ?
#Floor Division = ?
#---------------------------
#2
langs = ["Python", "C++", "Java", "Ruby"]
langs.remove('C++')
langs.append('GO')
langs.append('JavaScript')
print(langs)

#----------------------------
#3
nums = (5, 3, 8, 3, 9, 5, 3)
print(nums.count(3))#1
print(nums.count(5))#2
#numlist=f'{nums +[]}'
#print(numlist)
(_,_,A,b,c,d,e)=nums
print((A,b,c,d,e))#3
#----------------------
#4
a = {"AI", "ML", "Python"}
b = {"Math", "ML", "Python", "Deep Learning"}

print(a.difference(b))#1
print(a.intersection(b))#2
a.union(b)
print(f'Total elements = {len(a)}')

#------------------------
#5
topics1 = ["Data", "AI"]
topics2 = ["Python", "ML"]
topics3 = ["NLP", "Deep Learning"]

all_topics=[]
all_topics.extend(topics1)
all_topics.extend(topics2)
all_topics.extend(topics3)
print(all_topics)#1

print(all_topics.index('ML'))
all_topics.remove('ML')
all_topics.insert(3,'Math')
print(all_topics)#3
all_topics.sort(reverse=True)
print(all_topics)#4

#----------------------------
#6
names = ["Noura", "Ali", "Mona", "Mahmoud", "Nada"]
# مش عرفاها

#----------------------------
#7
skills = ["Python", "AI", "Python", "ML", "AI"]
#معرفش التحويلات
#--------------------------------
e = "noura@example.com"
print(e[:e.index("@")]) #noura
print(e[e.index("@")+1:e.index(".")])
#------------------------
d = {"a": 1, "b": 2}
d.popitem()  # يحذف b
print(d)
#-------------------------
d = {"x": 1}
print(d.setdefault("x", 0))  # 1
print(d.setdefault("y", 5))  # 5 → ويضيف "y"
print(d)
#------------------------------------
#Tasks Part 1
#1
a = 12
b = 5
print(f'Sum = {a+b}')
print(f'Sub = {a-b}')
print(f'Mul = {a*b}')
print(f'Remainder = {a%b}')
print(f'Floor Division = {a//b}')
print(f'Power = {a**b}')

#----------------------------------------
#2
user = {"name": "Noura", "age": 22}

#for one using deffirent ways
print(user["name"]) #1
print(user.get('name')) 
#print(user.pop('name')) 
print(user.setdefault('name',0))
print(user.get('age')) #2

#-------------------------------------
#3
skills = {"Python": "Advanced", "AI": "Beginner", "Math": "Intermediate"}
skills.pop('AI')
print(skills) #1
skills.popitem()
print(skills) #2

#-----------------------------------------
#4
profile = {"name": "Noura"}
profile.setdefault('Country','Egypt')
print(profile) #1
profile.update({'name':'Nourhan'})
print(profile)#2
#----------------------------------------
#5
student = {"name": "Ali", "grade": "A", "passed": True}

for key ,value in student.items() :
    print(f'{key} =>{value}')

#----------------------------------------
#6
a = ""
b = "Noura"
c = []
d = [1, 2]
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))

#---------------------------------------
#7 
x = 10
print('Negative') if x<0 else print('Positive')
#--------------------------------------
#8
data = {"username": "nour", "password": "12345"}

print('Access Denied') if data["password"] !='12345' else print('Access Granted')

#--------------------------------------
#9
info = {"lang": "Python", "level": "Advanced", "field": "AI"}

print(info.keys())
print(info.values())
#--------------------------------------
#10
#{'a': 0, 'b': 0, 'c': 0}

l_one=['a','b','c']
l_Two= dict.fromkeys(l_one,0)
print(l_Two)
l_Two.clear()
print(l_Two)
#------------------------------------
#keeping Tasks for part one
#1
user = {"name": "Noura", "age": 20, "country": "Egypt"}

# عدلي الاسم لـ "Nour" 
user.update({'name':'Nour'}) 
print(user)
# زودي مفتاح جديد job = "AI Engineer"  
user.update({'Job':'AI Engineer'})
print(user)
# احذفي مفتاح "country"
user.pop('country')
print(user)

#------------------------------------
#2
is_logged_in = False
# لو الشخص مسجل دخول اطبعي "Welcome", غير كده "Please Login First"
print('Please Login First')if not is_logged_in else print("Welcome")

#-----------------------------------
#3
student = {"name": "Ali", "grade": "B"}

# استخدمي setdefault لإضافة passed=True

student.setdefault('Passed',True)
print(student)
#--------------------------------------
#4
book = {"title": "AI Basics", "author": "Noura", "pages": 150}
# استخدمي loop لعرض كل key والقيمة

for key ,value in book.items():
    print(f'{key} => {value}')
#--------------------------------------
#5
settings = dict.fromkeys(["sound", "brightness", "volume"], "on")
# اطبعي الإعدادات
print(settings)
#-------------------------------------
#6
skills = {"Python": "Good", "AI": "Beginner"}
# لو "AI" موجودة، اطبعي "You're ready!", غير كده "You need to learn AI"
print("You're ready!") if 'AI' in skills else print("You need to learn AI")
#-------------------------------------
#7
x = 0
y = " "
z = [0]

# اطبعي النتيجة لكل وحدة
print(bool(x))
print(bool(y))
print(bool(z))

#----------------------------------------
#8
info = {"name": "Noura", "track": "AI", "level": "Beginner"}

# امسحي "track"
info.pop('track')
info.update({'level':'Advanced'})
print(info)
# حدّثي المستوى إلى "Advanced"
#----------------------------------------
#9
score = 88

# لو score أكبر من أو تساوي 90 → "Excellent"
# لو بين 70 و 89 → "Good"
# أقل من كده → "Try Again"
if score >=90 :
    print('Excellent')
elif score >= 70 and score <=89:
    print('Good')
else:
    print('Try Again')

#---------------------------------------
#10
profile = {"name": "Nour"}

# استخدمي update علشان تضيفي:
# "email": "nour@example.com", "city": "Cairo"
profile.update({'email':'nour@example.com','City':'Cairo' })
print(profile)
#----------------------------------------
# Kepping Tasks for Part one
#1
user = {
  "name": "Noura",
  "details": {
    "age": 23,
    "country": "Egypt",
    "skills": {
      "Python": "Advanced",
      "AI": "Beginner"
    }
  }
}
#print(user.keys())
print(user["details"]['skills']['Python'])
#-----------------------------------------
#2
student = {
  "name": "Ali",
  "grades": {
    "math": 90,
    "ai": 50
  }
}
student["grades"].update({'ai':75})
student["grades"].pop('math')
print(student)
#--------------------------------------
#3
employee = {"name": "Mona", "job": "AI Intern"}
employee.update({'salary':0})
print(employee)
#-------------------------------------
#4
data = {
  "id": 101,
  "profile": {
    "username": "nour",
    "level": "Advanced"
  }
}
print(str(data['profile'].keys()))
#معرفتش اعرضها كل واحدة ع حدة بتطلع كدا 
#dict_keys(['username', 'level'])

for key ,value in data['profile'].items():
    print(key)

#Done <3
#---------------------------------------
#5
skills = {
  "Python": "Advanced",
  "AI": "Beginner",
  "ML": "Beginner",
  "Math": "Intermediate"
}

count = 0
for key, value in skills.items():
    if value == "Beginner":
        count += 1

print(count)


#----------------------------------------
#6
langs = {
  "Python": True,
  "C++": False,
  "JavaScript": True
}
#print('You Should Learn Java') if not langs else print("You're Ready")

if 'Java' not in langs:
    print("You should learn Java")

#-----------------------------------------
#7
project = {"name": "AI Tool", "budget": 5000}
if 'duration' not in project:
    print('Not Set')

#-----------------------------------------
#8
keys = ["Python", "AI", "Math"]
new_keys= dict.fromkeys(keys,'Beginner')
print(new_keys)
#----------------------------------------
#9
skills = {
  "Python": "Advanced",
  "AI": "Beginner",
  "ML": "Intermediate"
}
for key,value in skills.items():
    if value != 'Beginner':
        print(key)

#------------------------------------
#10
a = True
b = False
c = True
print(bool(a and b or c))
#--------------------------------
# Tasks For Part Two
#1
temperature = 25
# Output: Hot
if temperature <=10:
    print('Cold')
elif temperature ==20:
    print('Spring')
else:
    print('Hot')

#-----------------------------------
#2
name = "Noura"
age = 20
# Output: Welcome Noura
if name=='Noura':
    if age >=20:
        print(f'Welcome {name}')    
#----------------------------------
#3
number = 7
# Output: Odd
if number%2==0:
    print('Even Number')
else:
    print('Odd')
#another way
print('Odd') if not number%2==0 else print('Even Number')

#-------------------------------
#4
from datetime import date
birth_year = 2000
# Output: Your age is 25  (لو السنة الحالية 2025)
age=date.today().year - birth_year
print(age)
#-------------------------------
#5
skills = ["Python", "Math", "AI"]
# Output: Found
print('Found') if 'AI' in skills else print('Not Found')
#-------------------------------
#6
i=0
while i<3:
    print(i)
    i+=1
else:
    print('Done')
#-----------------------------------
#7
i=0
while i<3:
    print(i)
    i+=1
    if i==3:
        break
#-------------------------------
# 8
#i=0
for i in range(3):
    print(i)
    i+=1
else:
    print('Loop Finished')
#-------------------------------
#9
#i=0
#while i<=4:
#    if i==2:
 #     print(i)
 #     i+=1
#    continue
#if i==4:
   # break
   
for i in range(4):
    if i==2:continue
    if i==4:break
    print(i)
    i+=1

#-------------------------------
#10
number = 6
square= lambda number: number*number
print(square(number))
# Output: 36
#--------------------------------
#11
#def greet(name):
     #user=input('Enter Your name: ')
    # if user== True:
      #   print(f'Hello {name}')
     #else:
     #    print(f'Hello Guest')    
     
#print(greet('NauRaa'))
#مش بتطلع
def greet(name):
    if name!='':
        print(f'Hello {name}')
    else:
        print(f'Hello Guest')
#---------------------------
#12
def langs(*lang):
    print(lang)   
print(langs('Python', 'AI', 'Math'))      
    
#---------------------------
#13
def dicto(**kwargs):
    print(kwargs)

print(dicto(name='Noura', track= 'AI'))
#---------------------------
#14
squ=lambda x:x*x
print(squ(5))
#---------------------------
#15
def numb(n):
    if n<=1:
        return 1
    return n* numb(n-1)
print(numb(4))
#---------------------------
#Keeping Part Two
x = 10
y = 20
z = 30
if z<x:
    print(f'{x} is the largest')
elif z<y:
    print(f'{y} is the largest')
else:
    print(f'z is the largest')   
#------------------------------------
 #2
user = "Noura"
role = "admin"
logged_in = True

#if user!='Noura':
 #   print('Wrong pass name')
  #  if role !='admin':
   #     print('Wrong information role')
    #    if logged_in== False:
     #       print('Please Login')
#else:
  #  print('Full Access')    لما بلعب فالبيانات بيطلعلى بردو full access    
if user =='Noura':
    print(f' {name}')
    if logged_in==True:
        print('you are in')
    elif role=='admin':
        print('Hi Admin')    
else:
    print('Full Access')    
if user == 'Noura' and role=='admin' and logged_in==True:
    print('Full Access')
else:
    print('Check Ur data') 
#finally
if user=='Noura':
    if role=='admin':
        if logged_in==True:
            print('full Access')
        else:
            print('You r off')
    else:
        print('Wrong role')        
else:
    print('Check ur info')            
#---------------------------
#3 مطلوب المسألة مش واضح
num =13
print('Multiple of 3') if not num %3==0 else print('"Not multiple"')
#---------------------------
#4
from datetime import date
birth_year = 2010
age=date.today().year -birth_year
if age<18:
    print('Underage')
#-------------------------
#5
topics = ["Python", "AI", "ML"]
removed = "Math"

if removed in topics:
    print('Math')
else:
    print('You should learn Math')    
#another way
print('You should learn Math') if not removed in topics else print('Math')   

#------------------------------
#6
counter = 0
while counter < 5:
    if counter==3:break
    print(counter)
    counter+=1
else:
    print('Loops Done') #مظهرتش وانت مش كاتبها فالاوتبوت   
#-----------------------------
#7
skills = ["Python", "AI", "Math", "Excel"]
for i in skills:
    if i == "Excel":continue
    print(i)
#-----------------------
# 8
for char in "Noura":
    print(char)
else:
    print("Done")
#----------------------
#9
def check_pass(mark):
    # لو الدرجة أكبر من أو تساوي 50 → "Passed"
    if mark >=50:
        return 'Passed'
    # غير كدا → "Failed"
    else:
        return 'Failed'
pass

print(check_pass(60))
#----------------------------------
#15
def fact(n):
    if n<=1:
       return 1
    return n * fact(n-1) 
print(fact(3))   

#---------------------------------
#Keeping Part Two 
x = 10
y = 15
z = 20

if z>x and z>y :
    print("Z is the biggest")
else:
    print('Z Not the biggest')

#--------------------------------
#2
user = "Noura"
track = "AI"
level = "Beginner"

if user =='Noura' and track=='AI' and level != 'Advanced':
    print('Welcome AI Learner')
else:
    print('Update your info')
   
#----------------------------------
#3
score = 70
if score>=60:
    result= 'Pass'
else:
    result='Fail'
print(result)    
#-------------------------
#4
from datetime import date
birth = 1998
age= date.today().year - birth

print(f'You are {age} years old')

#You are 27 years old
#-----------------------------
#5
start = 0
for start in range(5):
    if start==3:break
    print(start)
#-----------------------------
#6
langs = ["Python", "C++", "AI", "HTML"]

for l in langs:
    if l=='HTML':continue
    print(l)
#-----------------------------
# 7
i = 1
while i< 4:
    print(i)
    i+=1
else:
    print('Done')   
#-----------------------------
# 8
n = 6
square1= lambda n:n**2
print(square1(n))
#-----------------------------
#9
def total(*nums):
    return sum(nums)
print(total(10, 20, 5))
#-----------------------------
#10
def fact(n):
    if n<=1:
        return 1
    return n* fact(n-1)
print(fact(4))
#-----------------------------
#Keeping Part Two 
#1
grade = 75  
logged_in = True
if grade >=60 and logged_in== True:
    print('Well Done')
else:
    print('Check Requirements')    
#-------------------------------------
#2
user = {
    "username": "Noura",
    "track": "AI"
}
    
if 'username' and 'track' in user:
    print(f'Welcome {user["track"]} Student {user['username']}')
#----------------------------
#3
def power_sum(*args):
    return sum(x**2 for x in args)
print(power_sum(2, 3, 4))
#-----------------------------
#4
skills = ["Python", "Math", "AI"]

if 'AI' and 'Math' in skills:
    print("You’re Ready For AI Track")
else:
    print('More Skills Needed')

#---------------------------------
#5
langs = {
  "Python": "Advanced",
  "AI": "Intermediate",
  "ML": "Beginner",
  "Math": "Intermediate"
}

count=0

for key,value in langs.items():
    if value =='Advanced' or value =='Intermediate':
        count+=1
print(count)    
    #مش عرفاها
#---------------------------------
# Keeping Tasks For Part Two
#1
my_lista=[5, 12, 7, 20, 3, 9]

for lis in my_lista:
    if lis%2==0:
        print(lis)

#-------------------------------
# 2
dicot={"Ali": 80,
"Sara": 60, 
"Mona": 45,
"Ziad": 90}
    
for key , value in dicot.items():
    if value >=50:
        print(f'Succeced student: {key}')
#----------------------------------
#3
def calc_area(length, width):
    return length * width
print(f'Area:{calc_area(4,5)}')

#---------------------------------
#4
i=1
while i<=5:
    print(i)
    i+=1
#---------------------------------
#5
lista= ["AI", "Python", "Math", "ML", "Data"]

counter=0

#for x in lista:
#    if len(lista[x]) >= 3:
#        counter+=1
#print(counter) #لية مشتغلتش !
for eleme in lista:
        if len(eleme) >=3:
           counter+=1
print(counter)            
#--------------------------------
#6
#limbada= [1, 2, 3, 4]

#squ= lambda x: for x in limbada x**2
#================================
#7
def average(*args):
    return sum(x for x in args)/len(args) 
print(average(2,8,5))

#--------------------------------
user = {
    "name": "Noura",
    "info": {
        "age": 23,
        "track": "AI",
        "skills": ["Python", "Math"]
    }
}
#المطلوب: تطبعي "Noura is 23 years old and learning AI"

print(f'{user["name"]} is {user["info"]["age"]} years old and learning {user["info"]['track']}')
#-----------------------------
#9
myLista=['Python','AI','Math']
for x in myLista:
    print(x)
else:
    print('All Done')
#-----------------------------
#10
def prog(num):
    if num %2==0:
        return 'Positive'
    else:
        return 'Negative'  
print(prog(4))    #testing number      
#---------------------------------
#keepin tasks for Part two 
#1
nums = [12, 7, 9, 20, 5, 8]

#Sum of even numbers is 40

total=0
for num in nums:
    if num%2==0:
        total+=num
    else:continue
print(f'sum of even numbers is {total}')
#another way 

#from functools import reduce
#result= reduce(lambda acc,curr: if curr %2==0 :acc+curr,nums)
# print(result) معرفتش احط الشرط

#-----------------------------
#2
def numbers(*args):
   return max(args)
print(numbers(10, 45, 2, 99, 0))
#-----------------------------
#3
user = {"name": "Noura",
         "track": "AI",
           "logged_in": True}
if user["logged_in"]== True and user["track"]=='AI':
    print(f'Welcome {user["name"]} to the {user["track"]} track')
#------------------------------
#4
def check_student(name,*args):
    averagE= sum(x for x in args)/3
    if averagE >=70:
        return f'{name} has average {averagE} - Passed'
    else:
        return 'Not Successfull'
print(check_student("Ali", 80, 70, 90))

#---------------------------------
#6

skills = {
  "Python": "Advanced",
  "AI": "Intermediate",
  "Math": "Beginner",
  "ML": "Advanced"
}
for key , value in skills.items():
    if value == 'Advanced' or value == 'Intermediate':
         print(key)
#--------------------------------------
#7
nums = [1, 2, 3, 4]
nums.sort(reverse=True)
my_lmda= list(map(lambda x:x**2,nums))
print(my_lmda)
#------------------------------------
#8
data = ["Python", "Skip", "AI", "Math"]
for x in data:
    if x== 'Skip':continue
    print(x)
#-----------------------------------
# 9
skills = {
  "Python": "Advanced",
  "AI": "Beginner",
  "ML": "Beginner",
  "Math": "Intermediate"
}
countSkills=0
for key , value in skills.items():
    if value=='Beginner':
        countSkills+=1
print(countSkills)   
#----------------------------
#10
def sum_recursive(n):
    if n<=1:
       return 1
    return n + sum_recursive(n-1)

print(sum_recursive(5))    
#----------------------------------
#5
bookmarks = []
while True:
    inp = input('Enter number (or type "done" to finish): ')
    
    if inp.lower() == 'done':  # بيحول أي كتابة لـ lowercase علشان يقبل Done أو done أو DONE
        break
    
    if inp.isdigit():  # يتأكد إن الإدخال رقم
        bookmarks.append(int(inp))  # يضيف الرقم للقائمة بعد تحويله لـ int
    else:
        print("Please enter a valid number.")

# نحسب المتوسط بعد الخروج من اللوب
if bookmarks:  # نتأكد إن في أرقام
    average = sum(bookmarks) / len(bookmarks)
    print(f'Average is: {average}')
else:
    print("No numbers were entered.")
#-----------------------------------------
#Tasks for Part threee
#1
#pip install pyjokes مش شغالة 
#import pyjokes 
#print(pyjokes.get_joke()) معرفتش 
#--------------------------------------
#2
from datetime import datetime 
today= datetime.today()
print(today.strftime('%D/%M/%Y')) #07/12/25/22/2025 طبعلى كدا 
#------------------------------------
#3
print(today.strftime('%A'))
#------------------------------------
#4
nums=[10 , 20 ,30, 40, 50]
itera= iter(nums)
print(next(itera))
print(next(itera))
print(next(itera))
#------------------------------------
#5
itera_1=['one','two', 'three']
#itera_Total=iter(itera_1)
#print(itera_Total)
#while True:
#    print(next(itera_Total))
#else:
#    print('done')

#while itera_Total 

#while it < iter(itera_1):
#    print(it) معرفتهاش

#-------------------------------
#6
def geneR():
    yield 1
    yield 2
    yield 3
#geneR()
for i in geneR():
    print(i)
#-------------------------------
#7
#def squG((a,b,c,d)):
#    yield a**2
#    yield b**2
 #   yield c**2
#    yield d**2
#squG([1,2,3,4])

#for i in squG():
 #   print(i) #مطلعتش
def squG(lst):
    for i in lst:
        yield i**2

for x in squG([1,2,3,4]):
    print(x)

#----------------------------
#8
from datetime import datetime
hour= datetime.now().hour
minute= datetime.now().minute
print(f'Hour:{hour}')
print(f'Minute:{minute}')
#-------------------------------
#9
import math 
sq=64
print(math.sqrt(sq))
#-------------------------------
#10

from datetime import datetime
helpin= datetime.now().today
print(help(helpin))
#-------------------------------
#keeping Tasks Part three
#1
x = 15
y = 10
z = 7
if x>y or x > z :
    print('X is the biggest')
else:
    print('X is not the biggest')

#-----------------------------------
# 2
user = "Noura"
track = "AI"
level = "Beginner"

if user=='Noura':
    if track=='AI':
        if level=='Beginner':
            print(f'Welcome {track} {level}')
else:
    print('You should be learn basics')
#--------------------------------
#3
score = 75
if score>= 0:
    print('Passed')
else:
    print('Not Successfull')
#-------------------------------
#4
from datetime import date
birth = 1999
age= datetime.now().date().year - birth
print(age)
#------------------------------
#5
i = 0
#while i==0 and i<=2:
#    print(i)
#    if i==2:
#        print('Loop Done')
#فالحالتين مشتغلوش
#while i==0 and i <=2:
#       print(i)
#else:
#    print('Loop done)
#-----------------------------
#6
langs = ["Python", "C++", "AI", "HTML"]
for i in langs:
    if i== 'HTML': continue
    print(i)
# عملت range(langs) قالى غلط
#----------------------------
#7
n = 6
sq= lambda x:x**2
print(sq(n))
#---------------------------
#8
def total(*nums):
  #  return sum(x:for x in range(nums)) مش فاكرة اللوب جوا السم
    return sum(nums)
print(total(9,9,9,4,5,5,4))
#--------------------------
#9
user = {"name": "Ali", "logged_in": True}

if user["name"]== 'Ali':
    if user["logged_in"]== True:
        print(f'Welcome {user['name']}')
else:
    print('wrong data')
#------------------------------------
#10
def biggest(*num):
    return max(num)
print(biggest(5, 20, 100, 33))
#------------------------------------
#11
nums = [1, 2, 3, 4]
mapped= map(lambda x:x**2,nums)
result=[]
for i in mapped:
    result.append(i)

print(result)
#-------------------------------
#12
nums = [10, 13, 15, 20, 22]
def even_nums(n):
    if n%2==0:
        return n
    
filtered_nums=filter(even_nums,nums)
rezult=[]
for i in filtered_nums:
    rezult.append(i)
print(rezult)
#-------------------------------
#13
from functools import reduce
nums = [5, 10, 15]
def summ(num1,num2):
    return num1+num2

reduced_func= reduce(summ,nums)
print(reduced_func)
#--------------------------------
#14
my_list = [100, 200, 300, 400]
it=iter(my_list)
print(next(it))
print(next(it))
print(next(it))
#--------------------------------
#15
def my_gen():
    yield 1
    yield 2
    yield 3
for i in my_gen():
    print(i)
#---------------------------------
#Keeping Tasks for part three
#1
#result_average=''
#def check_grades(*nums):
  #  for x in nums: مش عافة احلها خالص
#        if x <=50:
 #         print('Check Student Performance')
 #       else:
 #           return result_average+=(sum(x) / 4) #len(list(nums)) عشان اجيب الطول متعملتش 
#check_grades(90, 60, 40, 80)
result='Average: '
def check_grades(*nums):
    for x in nums:
        if x<=50:
            print('Check Student Performance')
    print(f'{sum(nums)/4 }')  
check_grades(90, 60, 40, 80)

#---------------------------------
#2
#عملت نفس الفكرة قبل كدا ومش مدينى معطيات
#---------------------------------
#3
my_listr=[6,7,8, 10, 11]
mapped_list1= map(lambda x:x**2,my_listr)
filtere_mapped= filter(lambda x:x>50,mapped_list1)
result=[]
for x in filtere_mapped:
    result.append(x)
print(result)    
#----------------------------------
#4
#import os 
#print(os.getcwd())

#my_file= open("E:\PythonAI\NewTextDocument.txt",'r')
#print(my_file) مش عارفة اعملها
#---------------------------------
#Keeping Tasks for functions built in 
#1
nums = [5, 10, 15, 20]

if all(nums)>0:
    print('All Positive: True')
else:
    print('none positive')
#------------------------------------
#2
nums_a = [1, 3, 7, 8, 11]
if any(nums_a) // 2 == 0:
    print('Has Even: True') #مشتعلتش لما عملت %2
else:
    print('none even: False')

#---------------------------------
#3
nums = [10, 25, 30]
summ= sum(nums)
print(f'Total:{summ}')
max_x= max(nums)
print(f'Max: {max_x}')

#----------------------------------
#4
nums_4 = [2, 3, 4]
squar_4=map(lambda x:x**2,nums_4)
list_nums_4=[]
for x in squar_4:
    list_nums_4.append(x)

print(list_nums_4)
#---------------------------------
#5
nums_f = [1, 4, 5, 8, 11]
filtered_even_nums= filter(lambda x:x%2==0,nums_f)
list_f=[]
for x in filtered_even_nums:
    list_f.append(x)
print(list_f)

#-----------------------------------
#6
from functools import reduce
nums_R = [10, 20, 30]
def summ(num1,num2):
    return num1+num2

redu_nums= reduce(summ,nums_R)
print(redu_nums) #ازاى بتتعمل ب lambda 
#---------------------------------
#7
nums = [3, 1, 4, 2]
sor_nums=sorted(nums,reverse=True)
print(sor_nums)
#---------------------------------
#8
skills = ["Python", "AI", "Math"]
nums_en=enumerate(skills,start=0)
print(nums_en)
for x in nums_en:
    print(x)
#--------------------------------
#9
topics = ["Intro", "Flow", "Functions", "OOP"]
list_rev=[]
rev=reversed(topics)
for x in rev:
    list_rev.append(x)
print(list_rev)
#------------------------------
#10
names = ["Ali", "Noura"]
scores = [90, 95]
zipped= zip(names,scores)
for x in zipped:
    print(x)

#-------------------------------
#11
nums = [10, -5, 3, -2]
minned= min(nums)
print(f'Min Absolute Value: {abs(minned)}') #5
#------------------------------
#12
names = ["ali", "noura", "mona"]
def uppeR(name):
    return name.upper()
lis=[]
listed_map= map(uppeR,names)
for x in listed_map:
    lis.append(x)
print(lis)
#-------------------------------
#13
names = ["Ali", "Noura", "Ahmed", "Sara"]
#مش شغالة
#filte=filter(lambda :x for x in names: x.startswith('A'),names)
lis_fil=[]
#for x in filte:
#    list_f.append(x)
#print(lis_fil)
lisf=[]
def findin(name):
     return name.startswith('A')
filte=filter(findin,names)
for x in filte:
    lisf.append(x)
print(lisf)
#----------------------------------
#14
from functools import reduce
nums = [2, 3, 4]
def sreD(num1,num2):
    return num1+num2
redd=reduce(sreD,nums)
print(redd)
#---------------------------------
#15
names = ["Ali", "Noura"]
subjects = ["Math", "AI"]
grades = [90, 100]
zipped=zip(names,subjects,grades)
for x in zipped:
    print(x)

#------------------------------------
# 16
skills = ["AI", "Python", "ML", "Excel"]
en= enumerate(len(x)>3 for x in skills)
#print(en)
for x ,y in en:
    if y==True:
        print(x ,' -' ,y)
#print(enumerate(skills,start=0)) # مش عارفه اعمل الشرط 

#def s(n):
 #   if n in skills and len(n)>3:
 #       print(enumerate())
#for x in skills:
    #if len(x)>3:
       # print(enumerate(skills))
#for x in enumerate(skills,start=0):
#    if len(x)>3:
#        print(x) #مش عارفه خاااالص

#--------------------------------------
gen = (x * 2 for x in range(5))
print(gen)

numbers = [1, 2, 3, 4, 5]
squares = (x**2 for x in numbers)
print(next(squares))  # يطبع 1
print(next(squares))  # يطبع 4
#--------------------------------
#keeping tasks for functions built in 
#1
nums = [1, 3, 7, 8, 10, 13]
#find first evel number
def evel_e(num):
    return num % 2==0
d=[]
for x in filter(evel_e,nums):
    d.append(x)
it=iter(d)   
print(next(it)) 
#-------------------------------
#2
names = ["Sara", "Ali", "Mohammed", "Noor"]
s=sorted(names , key=lambda x: len(x))
print(s)
#-------------------------------
#3
nums = [1, 2, 3, 4, 5, 6]
def f(num):
    return num %2 ==0
d=[]
for x in filter(f,nums):
    d.append(x)
print(d)
from functools import reduce
redd=reduce(lambda x,y:x+y,d)
print(redd)
#-----------------------------------
#4
words = ["ai", "Math", "Data", "aiTool", "Excel", "ml"]
def f(word):
    if len(word) > 3 and str.istitle(word) == True:
        return word
d=[]
for x in filter(f,words):
    d.append(x)
print(d)
#--------------------------------
#5
students = ["Ali", "Noor", "Sara"]
grades = [90, 85, 99]
subjects = ["Math", "AI", "Physics"]
d=[]
for x in zip(students,grades,subjects):
    d.append(x)
print(d) # لو عاوزة الغى الليستا احول لتابل بس !!
#---------------------------------
#6
nums = [5, -3, 8, -1, 0, -6]
def f(num):
    return num <0
d=[]
for x in filter(f,nums):
    d.append(x)
print(len(d))
#-------------------------------
#7
skills = ["Python", "AI", "ML", "Excel", "Data"]
d=()
#d=[]
for index, value in enumerate(skills):
    if index != 0 and index % 2!=0:
        #d.append(index,value)
        #print(index,',' ,value)
        d+=(index,value),
print(d)

#-------------------------------------
#8
words = ["Intro", "AI", "OOP", "Functions", "Flow"]
s=sorted(words,key=lambda x:len(x),reverse=True)
print(s)

#------------------------------------
#9
nums = [2, 3, 4]
def m(num):
    return f'num: {num}'

#m= map(lambda x:'num: {x}',nums)
ml=[]
for x in map(m,nums):
    ml.append(x)
print(ml)
#--------------------------------------
#10
words = ["I", "love", "Python"]
redd= reduce(lambda x,y: x+' '+y,words)
print(redd)
#--------------------------------------
#Tasks for file handling
#1
import os 
print(os.getcwd())
my_file= open('E:\data.txt','w')
print(type(my_file))
print(my_file.name)
print(my_file.isatty())
# لو عاوزةاغير اسم الفايل اعمل اية !
#-----------------------------------
#2
my_file= open('E:\info.txt','w')
my_file.write('Line 1: Hello AI \n Line 2: Learning Python \n Line 3: File Handling is Easy')
my_file=open('E:\info.txt','r')
print(my_file.readlines(1))
print(my_file.read())
#----------------------------------
#3
my_file = open('E:\log.txt','w')
print(my_file.write('Python \nAI \nExcel'))
my_file=open('E:\log.txt','r')
print(my_file.read())
my_file=open('E:\log.txt','a')
my_file.write('\nML')
my_file= open('E:\log.txt','r')
print(my_file.read())
#-------------------------------------
#4
my_file=open('E:\details.txt','w')
my_file=open('E:\log.txt','r')
print(my_file.name)
#مش عارفه الترميز 
print(my_file.mode)
print(my_file.closed)
my_file.close()
print(my_file.closed)
#-------------------------------------
#5
my_file=open(r'E:\new.txt','w')
my_file.write('NauRaa \nPython \nAI Engineering \nEnglish')
open(r'E:\new.txt','r')
#معرفش عدد السطور
#---------------------------------------
#Tasks for Built-in Modules
#1
num =50
import math
s=math.sqrt(num)
print(f'Square Root:{s}')
import random
print(f' Random Number:{random.randint(10,50)}')
import os
print(f' Current Working Directory: {os.getcwd()}')
#-------------------------------
#2
#import mytools.py
#كتبت كدا فالتيرمنال pip install mytools.py عملى خطأ
#مش عارفاها خالص
 
#-------------------------------
#4
from datetime import datetime
now=datetime.now() 
print(f'Current Time:{now}')#2025-07-18 11:08:15.047232 طلعلى كدا
year=datetime.now().year
print(f'Current Year:{year}')
# بين تاريخين مين ومين 
#-------------------------------------
#5
now = datetime.now()
formatted = now.strftime("Today is %A, %d %B %Y - %I:%M %p")
print(formatted)
#-------------------------------------
#6
skills = ["AI", "Python", "ML"]
it=iter(skills)
print(next(it))
print(next(it))
for x in it:
    print(x)
#---------------------------------
#advanced Tasks for modules
#1
import math
num=int(input('square root is: '))
print((math.sqrt(num))) #مش عارفة 
import random
print(random.randint(100,200)) 
import os
print(os.getcwd())
#----------------------------------
#2
my_file=open('E:\PythonAI\myhelper.py','w')
my_file.write("""
def welcome(name):
    return f"Hello {name}, this is your assistant."

def add(x, y):
    return x + y
""")

my_file1=open('E:\PythonAI\main.py','w')
my_file1.write("""
import myhelper
print(welcome('Noura'))
print(add(5,10))
               """)
#--------------------------------------
#3
#import pyfiglet #مشتغلتش ومفعلة الباكدج
#4
from datetime import datetime
now=datetime.now()
print(now)
year= now.year
print(year)
print(now.month)
print(now.day)
birth_year=year-1994
print(birth_year)
#---------------------------------
#5
today= datetime.now().strftime(f'Today is {'%A'},{'%d %B %Y'}-{'%I:%m %p'}')
print(today)
#---------------------------------
#6
skills = ["AI", "Python", "ML", "Excel"]
it=iter(skills)
print(next(it))
print(next(it))
print(next(it))
for x in it:
    print(x)
#------------------------------------------
#Tasks for Iter, Generators,Decerators
#1
"""
iterable: can be string , lists , dict or Tuple
u can make loop on indexes in it
,
iterator: it's a mechanic can generate indexes in iterable
by using method next() but first u have to put iterable in iter()
so can generate it by generator function or loop or next() 

"""
lista= [1,2,3,4] #-> iterable
print(next(iter(lista))) #->generator for one by one index

lista=[10,11,12,13,14,15,16,20,30,40,50]
lit=iter(lista)
print(next(lit))
print(next(lit))
print(next(lit))
print(next(lit))
print(next(lit))
print('#'*10)
for x in lit:
    print(x)

#----------------------------------
#1
skills = ["AI", "ML", "Python", "Data"]
it=iter(skills)
print(next(it))
print(next(it))

for x in it:
    print(x)

#-----------------------------------
#2
def even_number(limit):
    yield limit

print(next(even_number(10)))
#-----------------------------------
def even_number(limit):
    for num in range(1, limit + 1):
        if num % 2 == 0:
            yield num

#------------------------------------
#5
def print_name(func):
    def nestedfunc():
        print('Hello')
        func()
        print('Bye')
    return nestedfunc

@print_name
def greet():
    print("Welcome Noura!")

greet()
print('#'*10)
#-------------------------------------
#6

def check_positive(func):
    def nested_check(x,y):
        if x <0 or y <0 :
          print('Be aware one of numbers less than zero')
        func(x,y)
        print('Bye Bye') 
    return nested_check



@check_positive
def add_numbers(x, y):
    print(x +y)

add_numbers(10, -5)

#--------------------------------------
#Keeping Tasks
#1
items = ["AI", "ML", "Data", "Python"]
it=iter(items)
print(next(it))
print(next(it))

for x in it :
    print(x)
#-------------------------------------
#2
def generate_odds(limit):
    for num in range(limit + 1):
        if num % 2 != 0:
            yield num

gen = generate_odds(7)
print(next(gen))
print(next(gen))
for num in gen:
    print(num)
#-------------------------------------
#3
def myDecorator(func):
    def nested_func():
        print('Hi')
        func()
        print('Bye')
    return nested_func
@myDecorator   
def say_hello():
    print("I'm learning decorators")

say_hello()

#-------------------------------------
#4

def check_numbers(func):
    def nested_Check(x,y):
        if x <0 or y< 0:
            print('Negative number detected')
        else:
            print('Hi')    
        func(x,y)
    return nested_Check    

@check_numbers
def multiply(a, b):
    print(a * b)

multiply(-2, 4)

#------------------------------------
#general Tasks about general basic python
#1
def check_grade(*grades):
    for x in grades:
        if x >=85 :
            print('Excellent')
        elif x <85 or x >=70:
            print('Good')
        else:
            print('Fail')

check_grade(0,100)
#it printed that ...
#Good
#Excellent
print('#' *10)

#------------------------------------
#2
#even_numbers= any(num %2 ==0 for num in range(1,20+1))
#print(even_numbers)
#if even_numbers == True:
#    for x in even_numbers:
#        print(x)

for x in range(1,20+1):
    if x %2 ==0 :
        print(f'{x} : even')
    else:
        print(f'{x} : odd')
print('#' *10)

#-----------------------------------
#3
from datetime import datetime

now = datetime.now()

print(now.strftime('%Y-%M-%D : Date | \n%I:%m :Hour '))
#مش عارفة اطلعها بالظبط 
#2025-44-07/20/25 : Date 
#03:07 :Hour
print('#' *10)

#-----------------------------------
#4
languages = ["Python", "Java", "C++", "Rust"]
it= iter(languages)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print('#' *10)
#-----------------------------------
#5
def even_numbers_up_to(limit):
    for x in range(0,limit+1):
        if x %2==0:
            print(x)

even_numbers_up_to(10)
print('#' *10)
#------------------------------------
#6
def log_info(func):
    def nested_log(x):
        print('Start')
        func(x)
        print('Done')
    return nested_log
@log_info
def say_hi(name):
    print(f'Hello {name}!')
say_hi('NauRaa')
print('#' *10)
#-------------------------------------
#1
numbers = [10, -5, 0, 23, -7, 8, -100, 44]
def positive_numbers(lst):
    for i in lst:
        if i > 0:
            yield i

gen = positive_numbers(numbers)
print(next(gen))
print(next(gen))
print(next(gen))

#--------------------------------
#2
sentences = [
    "AI is the future.",
    "     ",
    "Python is amazing!",
    "",
    "Machine Learning"
]

    
filtered = filter(lambda x: x.strip() != '', sentences)
for s in filtered:
    print(s)

print('#'*10)
#--------------------------------
#3
now= datetime.now()
print(now.strftime('Today is: %Y-%M-%d | Time: %I:%m %p'))
print('#'*10)

#--------------------------------
#4
from time import time

def starter(func):
    def nested_starter():
        start = time()
        func()
        end = time()
        print(f'Time Runing is = {end-start}')
    return nested_starter

@starter
def counting():
    for n in range(1,1000):
        print(n)

counting()
print('#'*10)

#---------------------------------
#6
languages = ["Python", "JavaScript", "C#", "Rust", "Swift"]
it= iter(languages)
print(next(it))
print(next(it))
print(next(it))

print('#'*10)
#---------------------------------
#7
text = "Artificial Intelligence is awesome"
#print(text.count('a'))
c=0
for x in text:
    if x=='a' or x=='A':
        c+=1
print(c)
print('#'*10)
#---------------------------------
#9
def kwa(*args):
    positives = [x for x in args if x >= 0]
    if not positives:
        return 0
    return sum(positives) / len(positives)

    
print(kwa(1,10,2,-1))
#--------------------------------





















































































































































