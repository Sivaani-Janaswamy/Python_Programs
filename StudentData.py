#Write a Python program to read the student details like Name, USN and Marks in three subjects. Display the student details, total marks and percentage with suitable messages.
name = input("Enter your name:- ")
usn = input("Enter your usn:- ")
mrks1 = int(input("Maths Marks:- "))
mrks2 = int(input("Science Marks:- "))
mrks3 = int(input("English Marks:- "))
tmrk = (mrks1+mrks2+mrks3)
per = (tmrk/300)*100
print("Student Data: \n ")
print(" Name: %s \n Total marks: %0.2f \n Percentage: %0.2f "%(name,tmrk,per))


