t = int(input())
for z in range(t):
    k = int(input())
    n = int(input())

    floor = []
    for i in range(k+1):
        floor.append([1])
    floor[0] = [i for i in range(1,n+1)]

    for j in range(1,k+1):
        for i in range(1,n):
            floor[j].append(floor[j-1][i] + floor[j][i-1])       

    print(floor[k][n-1])
