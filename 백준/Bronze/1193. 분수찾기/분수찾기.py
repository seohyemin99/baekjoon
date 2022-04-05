N = int(input())
num = N; line = 1; total = 1;
while N > total:
    num -= line
    line += 1
    total += line
if line % 2 == 1:
    print("%d/%d" %(line + 1 - num, num))
else:
    print("%d/%d" %(num, line + 1 - num))