N = int(input())
count = []

for i in range(N):
    a = input()
    for i in range(1,len(a)):
        if a[i-1] != a[i]:
            if a[i-1] in a[i:] :
                count.append(a)

count = list(set(count))
print(N - len(count))