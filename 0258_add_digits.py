import math

# version 1: simple, but slowish and uses recursion
def addDigits(num):

    x = 0
    for k in range(0, len(str(num))):
        x += int(str(num)[k])

    if len(str(x)) == 1:
        return x
    else:
        return addDigits(x)


def addDigits2(num):
    if num == 0:
        return 0
    return num % 9 if num % 9 else 9



for i in range(0, 99):
    print(str(i) + ' : ' + str(addDigits(i)) + ' : ' + str(addDigits2(i)))
    # print('[' + str(i) + '] : (' + str(i % 9) + ', ' + str(i % 10) + ', ' + str(math.floor(i / 9)) + ', ' + str(math.ceil(i / 9)) + ') = ' + str(addDigits(i)) + ' || ' + str(addDigits2(i)))
    # print('[' + str(i) + '] : (' + str(i % 9) + ', ' + str(i % 10) + ', ' + str(math.floor(i / 9)) + ', ' + str(math.ceil(i / 9)) + ') = ' + str(addDigits(i)))
    # print(str(i) + ' : ' + str(addDigits(i)))

