T = int(input())
for i in range(T):
    R, S = input().split()
    P = ""
    R = int(R)
    S = list(S)
    for j in S:
        j = j * R
        P += j
    print(P)