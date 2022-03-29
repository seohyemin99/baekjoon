A, B = input().split()
A = list(str(A))
B = list(str(B))
a, b = "", ""
for i in range(0, len(A)) :
    a += A[len(A)-i-1]
for j in range(len(B)) :
    b += B[len(B)-j-1]
    
if int(a) > int(b) :
    print(a)
elif int(b) > int(a): 
    print(b)


    
    