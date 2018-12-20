import re

def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """

    str2 = ''
    foundsign = False

    # loop through all input characters, add them to str2 if valid, break once invalid chars are found
    for i in range(0, len(str)):
        if re.match("[+-]", str[i: i + 1]):
            if len(str2) > 0:
                break
            elif foundsign:
                return 0
            else:
                foundsign = True
                str2 = str2 + str[i: i + 1]
        elif len(str2) > 0 and re.match("[a-zA-Z ]", str[i: i + 1]):
            break
        elif len(str2) == 0 and re.match("[a-zA-Z]", str[i: i + 1]):
            return 0
        elif re.match("[0-9\-+.]", str[i: i + 1]):
            str2 = str2 + str[i: i + 1]

    print('found number: ' + str2)

    try:
        num = float(re.sub('[a-zA-Z ]', '', str2))
    except ValueError:
        return 0

    if num < -2147483648:
        return -2147483648
    elif num > 2147483647:
        return 2147483647
    else:
        return int(num)


print(myAtoi("  -0012a42") == -12)
print(myAtoi("3.14159") == 3)
print(myAtoi("-5-") == -5)
print(myAtoi("-5-"))
