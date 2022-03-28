N = int(input())
sum = 0
for i in range(1, N+1):
    lst = list(map(int,str(i)))
    if i < 100 :
        sum += 1
    elif lst[1] - lst[0] == lst[2] - lst[1]:
    	sum += 1
print(sum)