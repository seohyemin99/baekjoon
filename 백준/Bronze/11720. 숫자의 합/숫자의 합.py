N = int(input())
num = input()

lst = list(map(int,str(num)))

sum = 0
for i in lst :
	sum += i	

print(sum)