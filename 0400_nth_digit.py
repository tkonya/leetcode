import math


def findNDigit(n):

    # first, find the block of n values that the param n falls within
    # a block corresponds to the number of digits each number within it uses
    n_start = 1  # lowest n value in the block, inclusive
    n_end = 9  # highest n value in the block, inclusive
    digits_per = 1  # number of digits per real number in the block
    start_real_number = 1  # the real number this block starts at

    # n_end goes up very fast, so this loop does not run many times
    while n > n_end:  # while n is still outside the range of our block
        n_start = n_end + 1  # will now start at the next value
        go_up_by = ((start_real_number * 10) - start_real_number) * 10
        start_real_number *= 10
        digits_per += 1  # every next block has one more digit per real number
        n_end = (go_up_by * digits_per) + n_start - 1

    # calculate what real number our n value will land on
    real_to_go_up = math.floor((n - n_start) / digits_per)
    n_to_go_up = real_to_go_up * digits_per
    real_target = start_real_number + real_to_go_up

    # calculate where to slice the real number
    index = n - (n_start + n_to_go_up)
    return int(str(real_target)[index:index+1])


# for testing only, really slow
def findNthDigitDumb(n):
    num_string = ''
    i = 0
    while len(num_string) < n:
        i += 1
        num_string += str(i)

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