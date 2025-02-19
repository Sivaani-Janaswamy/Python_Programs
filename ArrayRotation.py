T = int(input())
for i in range(0,T):
 NK = [int(i) for i in input().split()]
 A = [int(i) for i in input().split()]
 for i in range(0,NK[1]):
    A = [A[-1]] + A[0:-1]
 print(*A,sep = " ")


"""
T = int(input())
for i in range(0,T):
 NK = [int(i) for i in input().split()]
 A = [int(i) for i in input().split()]
 for i in range(0,NK[1]):
    A.insert(0,A[-1])
    A.pop()
 print(*A,sep = " ")
"""



"""
T = int(input())
for i in range(0,T):
 NK = [int(i) for i in input().split()]
 A = [int(i) for i in input().split()]
 for i in range(0,NK[1]):
    A.insert(0,A[-1])
    A.pop()
print(*A,sep = " ")
"""



""" def rotate(K,A):
    if(K!=0):
       A.insert(0,A[-1])
       A.pop()
       rotate(K-1,A)
    else:
       return A


T = int(input())
for i in range(0,T):
 NK = [int(i) for i in input().split()]
 A = [int(i) for i in input().split()]
 rotate(NK[1],A)
 print(*A,sep = " ")
"""







"""  l = len(A)
 for i in range(0,NK[1]):
    A.insert(0,A[l-1])
    A.pop()
"""
"""
T = 1 #testcases
NK = [5,2]
A = [1,2,3,4,5]
l = len(A)
for i in range(0,NK[1]):
    A.insert(0,A[l-1])
    A.pop()
print(*A,sep = " ")


for i in range(0,NK[1]):
    tA = []
    tA.append(A[l-1])
    for i in range(0,l-1):
        tA.append(A[i])
    A = tA.copy()
print(*tA,sep = " ") """

