# 811235 
num = list(map(int, input()))
if sum(num[:3]) == sum(num[3:]):
    print("ДА")
else:
    print("НЕТ")