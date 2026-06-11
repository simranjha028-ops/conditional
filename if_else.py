###write a program to find the greatest of four numbers

a = int(input("Enter the 1st number:"))
b = int(input("Enter the 2nd number:"))
c = int(input("Enter the 3rd number:"))
d = int(input("Enter the 4th number:"))

if (a>b and a>c and a>d):
    print(a,"is the greatest number")
elif(b>a and b>c and b>d):
    print(b,"is the greatest number")
elif (c>a and c>b and c>d):
    print(c,"is the greatest number")
else: (d>a and d>b and d>c)
print(d,"is the greatest number")

#expected output
##Enter the 1st number:47
#Enter the 2nd number:5
#Enter the 3rd number:8
#Enter the 4th number:65
#65 is the greatest number



###write a program to find out whether a student has passed or failed if it requires total of 40% and atleast 33% in each sub to pass. take marks as input from user and assume sub.


m1 = int(input("Enter the 1st marks:"))
m2 = int(input("Enter the 2nd marks:"))
m3 = int(input("Enter the 3rd marks:"))

total_percent = (100*(m1+m2+m3))/300

if (total_percent>=40 and m1>=33 and m2>=33 and m3>=33):
    print("You have successfully passed the exam")

else:
    print("You failed the exam")

#expected output
#Enter the 1st marks:33
#Enter the 2nd marks:45
#Enter the 3rd marks:21
#You failed the exam

#also
#Enter the 1st marks:45
#Enter the 2nd marks:87
#Enter the 3rd marks:54
#You have successfully passed the exam


####Write a program to identify spam messages

s1 = "Make money"
s2 = "Buy now"
s3 = "Hurry and click the link"

mess = input("Enter your message:")

if ((s1 in mess) or (s2 in mess) or (s3 in mess)):
    print("This is a spam")

else:
    print("This is not a spam")

#output
#Enter your message:Make money now
#This is a spam

#Enter your message:Dont click
#This is not a spam



####Write a program to identify whether a username contains  less than 10 char or not

username = input("Enter the username:")

if(len(username)<10):
    print("Your username contains less than 10 chracters")
else:
    print("Your username is valid")

#output
#Enter the username:simisrunning
#Your username is valid
#Enter the username:sim
#Your username contains less than 10 chracters

#######write a program to find whther a name is present in a list or not.

l = ["Simran","Khushi","Riya"]

name = input("Enter the name:")

if(name in l):
    print("Your name is in the list")
else:
    print("Your name is not in the list")

#expected output
#Enter the name:sakshi
#Your name is not in the list

#Enter the name:Simran
#Your name is in the list

#####marking scheme

marks = int(input("Enter your marks:"))

if(marks<=100 and marks>=90):
    grade = "Excellent"
elif(marks<90 and marks>=80):
    grade = "A"
elif(marks<80 and marks>=70):
    grade = "B"
elif(marks<70 and marks>=60):
    grade = "C"
elif(marks<60 and marks>=50):
    grade = "D"
elif(marks<=50):
    grade = "F"

print("Your grade is:",grade)

##output
#Enter your marks:20
#Your grade is: F
#Enter your marks:89
#Your grade is: A