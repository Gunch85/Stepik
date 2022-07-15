# 12 5 7 2
a, b, c, d = map(int, input().split())
if b > d + 1 and a > c + 1 or b > c + 1 and a > d + 1:
    print("ДА")
else:
    print("НЕТ")