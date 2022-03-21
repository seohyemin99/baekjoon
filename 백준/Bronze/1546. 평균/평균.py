N = int(input())
lst = list(map(int,input().split()))

b = max(lst)
for j in range(len(lst)):
    lst[j] = lst[j]/b*100
    
print(sum(lst)/len(lst))