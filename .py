'''=========================================================================================================== '''
#  --------------------------------------------AUTHOR: Deeksha R----------------------------------------------
'''=========================================================================================================== '''


#Complex Number: a=1j
'''print(type(a))
print(a) 
a= "Happy Father's Day"
b=a[1:6]
print(b)'''

#----------------------------------------------LIST[]-------------------------------------------------

'''a=[10, 2.3, False, "Hello", 1j, ['lmnop', 'b']]
print(a[3][-1])'''

#----------------------------------------------TUPLE()------------------------------------------------

#securable, unchangeable, ordered and indexed
'''a=(10, 2.3, False, "Hello", 1j, ('lmnop', 'b'))
print(a[-1])'''

#-----------------------------------------------SET{}-------------------------------------------------

'''is unordered and unindexed
a={10, 2.3, False, "Hello", 1j, 2.3, ('lmnop', 'b')}
print(a[-1])'''

#--------------------------------------------DICTIONARY{}---------------------------------------------

'''is unordered, changeable and indexed {key:value}
a={1: "Hello", 2: "World", 3: "Python"}
print(a[2])
b={'a':'hello','b':'world'}
print(b['b'])'''

#---------------------------------------------SLICING-------------------------------------------------

# is used to get a part of the string, etc. We use (:) operator. variable[start:stop:step]
#a='Hello'
#print(a[0:-1])
#print(a[0:4+1]) '''here 4+1 is used to include the last index'''
'''print(a[2:4-1])
a='Good Morning'
print(a[7:10+1])
print(a[-1:-12-1:-1]) #reversing
print(a[::-1]) #reversing
print(a[1:5+1:2])
print(a[5:11+1:3])
print(a[5:12:3])
print(a[5::3])
print(a[-7::3])'''


#----------------------------------------INPUT STATEMENTS-------------------------------------------

'''a=int(input("Enter a number: "))
b=a
print(a, "Multipled by 3 is", b*3)
a=eval(input("Enter: "))
print(a, type(a))'''


#--------------------------------------CONTROL STATEMENTS-------------------------------------------

'''a=int(input("Enter a number: "))
if a%2==0:
    print(a, "is an even number")
else:
    print(a, "is an odd number")'''
    
'''a=eval(input("Enter a list: "))
if len(a)==5:
    print("List has 5 elements")
else:
    print("List does not have 5 elements")'''

#print(ord('1')) ord() is used to get the ASCII value of a character
#print(ord('D')+32) #converting uppercase to lowercase

'''ch=input("Enter a character: ")
if "A"<=ch<="Z":
    print("Uppercase")
elif "a"<=ch<="z":
    print("Lowercase")
else:
    print("Not an alphabet")'''

#---------------------------------------LOGIN SYSTEM--------------------------------------------

'''un=input("Enter username: ")
if un=='lol':
    pw=input("Enter password: ")
    if pw=='lol4':
        print("Login Successful!")
    else:
        print("Password is incorrect")
else:
    print("Username is incorrect")'''

#--------------------------------------LOGIN SYSTEM TAKE 2--------------------------------------

'''username='lol'
password='lol4'
un=input("Enter username: ")
if un==username:
    pw=input("Enter password: ")
    if pw==password:
        print("Login Successful!")
    else:
        print("Password is incorrect")
else:
    print("Username is incorrect")'''

# -----------------------------------WHILE LOOP TO 100-------------------------------------------
'''i=1
while i<=100:
    if i%2==0:
        print(i)
    i+=1'''

#------------------------------------REVERSING A NUMBER------------------------------------------
'''n=int(input("Enter a number: "))
rev=0
while n>0:
    rev=(rev*10)+(n%10)
    n//=10
    ld=n%10
    n=n//10
    rev=(rev*10)+ld
print("Reversed number is", rev)'''

#------------FOR LOOP-------------
'''for i in range(0, 100, 5):
    print(i)
print("100")'''
'''l=[10,20,30]
for i in l:
    print(i)'''

#---------------------------------------FOR LOOP UPPER CASE---------------------------------------
'''s=input("Enter an alphabet: ")
for i in s:
    if "A"<=i<="Z":
        print(i, "is an uppercase letter")
    elif "a"<=i<="z":
        print(i, "is a lowercase letter")
    else:
        print(i, "is not an alphabet")'''

'''a='Happy Birthday'
print(a[-4:-7:-1])'''

#----------------------------------------------FUNCTIONS------------------------------------------

#They are reusable blocks of code that perform a specific task. They are defined using the 'def' keyword.
#Four types of functions:
#|1| No argument, no return value |2| Argument, no return value |3| No argument, return value |4| Argument, return value

#With Argument, with Return value:
'''def convert(s):
    output=''
    for i in s:
        if 'a'<=i<='z':
            output+=chr(ord(i)-32)
        else:
            output+=i
    return output
print(convert(input("Enter a string: ")))'''

#With Argument, Without Return value:
#Whenever there is a return statement, we have to call the function
'''def convert(s):
    output=''
    for i in s:
        if 'a'<=i<='z':
            output+=chr(ord(i)-32)
        else:
            output+=i
    print(output)
convert(input("Enter a string: "))'''

#Without Argument, without Return value:
'''def convert():
    s=input("Enter a string: ")
    output=''
    for i in s:
        if 'a'<=i<='z':
            output+=chr(ord(i)-32)
        else:
            output+=i
    print(output)
convert()'''

#Without Argument, with Return value:
'''def convert():
    s=input("Enter a string: ")
    output=''
    for i in s:
        if 'a'<=i<='z':
            output+=chr(ord(i)-32)
        else:
            output+=i
    return output
print(convert())'''



#-------------------------------OBJECT ORIENTED PROGRAMMING-------------------------------

#A class is a blueprint for creating objects. (Original)
#An object is an instance of a class. (Comes Next)
#Changes in object do not affect the class. (Independent)
#Changes in class affect the object. (Dependent)

#Class= Samsung Company, Object= Samsung Phone

'''class College:
    cname="Gopalan"
    cloc='Hoodi'
    
s1=College()
s1.sname='Girish'
s1.phno=9876543210

print(s1.cname, s1.cloc)
College.cloc='KR Puram'
print(College.cloc)
print(s1.cloc)
print("Changing Location wrt Object")
s1.cloc='Hoodi'
print(s1.cloc) #Hoodi
print(College.cloc) #KR Puram


s2=College()
s2.sname='Harish'
s2.phno=91234567890



print(s1.sname)
print(s2.sname)'''



#Constructors initialize repeated variable, methods, functions etc, using __init__

'''class college:
    cname='Gopalan'
    cloc='Hoodi'
    @classmethod
    def disp(cls):
        print(cls.cname, cls.cloc)
    def __init__(self,name,phno,usn): #Object method
        self.name=name
        self.phno=phno
        self.usn=usn
    def display(self):
        print(self.name, self.phno, self.usn)
    def change_name(self, new):
        self.name=new

s1=college('Harish', 9876543210, '1GD25ST001')
s2=college('Girish', 9012345678, '1GD25ST002')
s1.display()
s2.display()
s1.change_name("Hareesh")
s1.display()
s1.disp()
s2.disp()
college.disp()'''

