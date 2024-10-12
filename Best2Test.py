#Write a Python program to find the best 2 test marks out of 3 tests and find the average of them
import math 
print("Enter 3 numbers = ")
lno = [int(i) for i in input().split()]
del lno[lno.index(min(lno))]
avg = sum(lno)/2
print(f"Average of the best 2 test marks: {avg:.2f}")