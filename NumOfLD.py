#Two people made a list of movies they like or dislike 
#Find the number of movies they both like or dislike
#Input is two strings containing 1's and 0's, 1 stands for like, 0 stands for dislike
print("Strings: ")
lld= input().split()
lt = min(len(lld[0]),len(lld[1]))
count = 0
for i in range(0,lt):
    if(lld[0][i]==lld[1][i]):
        count+=1
print(f"No of movies they both like or dislike: {count}")

