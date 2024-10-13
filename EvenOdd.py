"""
Write a Python Program to count no of even numbers and odd numbers from the given list
Give distict numbers as input values
Sample Input:
5
12345
Description:The first line of input consists of a single integer N denoting the total number of input
The second line of input consists of Nspace separated integers, denoting the individual elements in the input
Sample output:
23
Output description:Output a single line with ocunt of even numbers and odd numbers from N, separated by a single space. 
"""
n = int(input())
l = [int(i) for i in input().split]
e,o = 0,0
for i in l:
   if(i%2==0):
    e+=1
   else:
    o+=1
print(e," ",o)