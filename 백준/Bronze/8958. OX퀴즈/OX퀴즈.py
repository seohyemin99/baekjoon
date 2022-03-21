N = int(input())
for i in range(N):
    b = input()
    lst = list(b)
    score = 0
    a = 1
    for j in lst:
        if j == 'O' :
            score += a
            a += 1
        else :
            a = 1
    print(score)