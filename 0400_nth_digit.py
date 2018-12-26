import math


def findNDigit(n):

    # first, find the block of n values that the param n falls within
    # a block corresponds to the number of digits each number within it uses
    n_start = 1  # lowest n value in the block, inclusive
    n_end = 9  # highest n value in the block, inclusive
    digits_per = 1  # number of digits per real number in the block
    start_real_number = 1  # the real number this block starts at
    digits_passed = 0  # the

    # print('n start = ' + str(n_start) + ', n end = ' + str(n_end) + ', start_real = ' + str(start_real_number) + ', digits per = ' + str(digits_per) + ', passed = ' + str(digits_passed))
    while n > n_end:
        n_start = n_end + 1
        go_up_by = ((start_real_number * 10) - start_real_number)
        # digits_passed += (digits_per * go_up_by)
        go_up_by *= 10
        start_real_number *= 10
        digits_per += 1
        n_end = (go_up_by * digits_per) + n_start - 1
        # print('n start = ' + str(n_start) + ', n end = ' + str(n_end) + ', start_real = ' + str(start_real_number) + ', digits per = ' + str(digits_per) + ', passed = ' + str(digits_passed))

    n_to_go_up = n - n_start
    real_to_go_up = math.floor(n_to_go_up / digits_per)
    n_to_go_up = real_to_go_up * digits_per
    # print('n up = ' + str(n_to_go_up) + ' real up ' + str(real_to_go_up))

    real_target = start_real_number + real_to_go_up
    # print('real target = ' + str(real_target))

    index = n - (n_start + n_to_go_up)
    # print('index = ' + str(index))
    return int(str(real_target)[index:index+1])


# for testing only, really slow
def findNthDigitDumb(n):
    """
    :type n: int
    :rtype: int
    """
    num_string = ''
    i = 0
    while len(num_string) < n:
        i += 1
        num_string += str(i)
    print('n = ' + str(n) + ', last number added: ' + str(i) + ', answer = ' + num_string[n-1:n])

    return int(num_string[n-1:n])


def test(n):
    x = findNDigit(n)
    y = findNthDigitDumb(n)
    if x == y:
        print('test passed: ' + str(x) + ' == ' + str(y))
    else:
        print('test failed: ' + str(x) + ' != ' + str(y))


test(1)
test(9)
test(19)
test(100)
test(3598468)