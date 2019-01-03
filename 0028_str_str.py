def strStr(haystack, needle):
    if len(needle) < 1:
        return 0
    for i in range(len(needle), len(haystack) + 1):
        if haystack[i - len(needle):i] == needle:
            return i - len(needle)
    return -1



print(strStr('hello', 'lo'))
print(strStr('aaaaa', 'bba'))