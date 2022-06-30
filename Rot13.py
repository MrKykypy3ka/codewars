def rot13(message):
    if message == '':
        return message
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMN' \
          'abcdefghijklmnopqrstuvwxyzabcdefghijklmn'
    s = ''
    for let in message:
        if let.isalpha():
            s += ABC[ABC.index(let) + 13]
        else:
            s += let
    return s


print(rot13("test") == "grfg")
print(rot13("Test") == "Grfg")