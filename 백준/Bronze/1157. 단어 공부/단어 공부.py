S = list(input().upper())
lst = list(set(S))

maxs = []
for i in lst :
    maxs.append(S.count(i))

if maxs.count(max(maxs)) > 1:
    print("?")
else :
    print(lst[maxs.index(max(maxs))])

        

