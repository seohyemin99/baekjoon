lst_1 = []
for n in range(1,10001):
    n = str(n)
    lst = list(map(int,n))
    d = sum(lst) + int(n)
    lst_1.append(d)
lst_2 = list(range(1,10001))
lst_3 = list(set(lst_2)-set(lst_1))
lst_3 = sorted(lst_3)
for i in lst_3:
    print(i)