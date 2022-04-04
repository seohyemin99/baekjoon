S = list(input().upper())

for i in range(len(S)):
    if S[i]=='A' or S[i]=='B' or S[i]=='C':
        S[i] = 3
    elif S[i]=='D' or S[i]=='E' or S[i]=='F':
        S[i] = 4
    elif S[i]=='G' or S[i]=='H' or S[i]=='I':
        S[i] = 5
    elif S[i]=='J' or S[i]=='K' or S[i]=='L':
        S[i] = 6
    elif S[i]=='M' or S[i]=='N' or S[i]=='O':
        S[i] = 7
    elif S[i]=='P' or S[i]=='Q' or S[i]=='R' or S[i]=='S':
        S[i] = 8
    elif S[i]=='T' or S[i]=='U' or S[i]=='V':
        S[i] = 9
    elif S[i]=='W' or S[i]=='X' or S[i]=='Y' or S[i]=='Z' :
        S[i] = 10
    else :
        S[i] = 11
        
print(sum(S))