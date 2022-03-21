C = int(input())
for i in range(C) :
    score = list(map(int,input().split()))
    N = score[0]
    avg = sum(score[1:])/N
    a = 0
    for j in score[1:] :
        if j > avg :
            a += 1
    rate = a/N*100
    print(f'{rate:.3f}%')
