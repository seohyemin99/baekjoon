N = int(input())
new = N
cy = 0

while True :
    one = new % 10
    ten = new // 10
    a = (one + ten) % 10
    new = (one * 10) + a
    cy += 1
    if new == N :
        break
print(cy)

    