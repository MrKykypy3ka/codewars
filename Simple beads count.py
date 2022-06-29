def last_digit(n1, n2):
    if n2 == 0:
        return 1
    elif n2 == 1:
        return int(str(n1)[-1])
    elif n1 % 10 == 0 and n2 % 10 == 0:
        return 0
    elif str(n1)[-1] == '1':
        return 1
    elif str(n1)[-1] == '5':
        return 5
    elif str(n1)[-1] == '6':
        return 6
    else:
        return ((n1 % 10) ** ((n2 - 1) % 4 + 1)) % 10


print(last_digit(4, 1) == 4)
print(last_digit(4, 2) == 6)
print(last_digit(9, 7) == 9)
print(last_digit(10, 10 ** 10) == 0)
print(last_digit(2 ** 200, 2 ** 300) == 6)
print(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651) == 7)