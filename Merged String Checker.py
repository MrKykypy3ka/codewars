def is_merge(s, part1, part2):
    if part1 == '':
        return s == part2
    elif part2 == '':
        return s == part1
    elif s == '':
        return part1 + part2 == ''
    elif s[0] == part1[0] and is_merge(s[1:], part1[1:], part2) or \
            s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]):
        return True
    return False


print(is_merge('codewars', 'code', 'wars'))
print(is_merge('codewars', 'cdw', 'oears'))
print(not is_merge('codewars', 'cod', 'wars'))
print(is_merge('codewars', 'code', 'wasr'))
print(is_merge('codewars', 'cwdr', 'oeas'))