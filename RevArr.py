#Given an array A of N numbers(integers), you have to write a program which prints the sum of the elements of array A with the corresponding elements of the reverse of array A. If array A has elements [1,2,3], then reverse of the array A will be 3,2,1] and the resultant array should be [4,4,4]
ar1 = [int(i) for i in input().split()]
ar2 = ar1.reverse()
sums = []
for i in range(0,len(ar1)):
    sums[i] = sums.append(ar1[i] + ar2[i])
print(sums)