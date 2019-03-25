# version 1
# def detectCapitalUse(word):
#     if word.upper() == word or word.lower() == word:
#         # if all letters are uppercase or all letters are lowercase, then the word is valid
#         return True
#     else:
#         for i in range(1, len(word)):
#             if word[i].upper() == word[i]:
#                 return False
#         return True


# version 2
def detectCapitalUse(word):
    return word.upper() == word or word[1:].lower() == word[1:]


print(detectCapitalUse('Word'))
print(detectCapitalUse('USA'))
print(detectCapitalUse('words'))
print(detectCapitalUse(''))
