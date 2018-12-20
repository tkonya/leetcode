import math

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    # special cases for short length inputs
    if len(s) < 1:
        return ""
    elif len(s) == 1:
        return s

    # look for longest first, that way we can stop once we find the first one
    for target_length in range(len(s), 0, -1):
        # print('target length: ' + str(target_length))
        for target_location in range(0, len(s) - target_length):
            # print(s[target_location:target_location + target_length + 1])
            if is_palindrome(s[target_location:target_location + target_length + 1]):
                return s[target_location:target_location + target_length + 1]

    return s[0:1]  # if no palindrome of at least len 2 is found, then just return the first character


def is_palindrome(s):
    a = s[:math.floor(len(s) / 2)]
    b = s[math.ceil(len(s) / 2):][::-1]
    return a == b


print(longestPalindrome("babad"))

# this is slow, it's essentially a brute force method
# a better way to do this problem would be to start from the bottom up:
# identify palindromes of 2 or 3, then expand them out,
# since you know that any palindrome of x length must be centered on a palindrome of x - 2 length
# it should be possible to keep eliminating candidates until you're left with only the longest

