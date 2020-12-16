def flag(b):
    if b < 0:
        return "请传入大于0的数值！"
    if b == 0:
        return 0
    if b == 1:
        return 1
    if b == 2:
        return 1
    if b >=3:
        return flag(b-1) + flag(b-2)

print(flag(10))



