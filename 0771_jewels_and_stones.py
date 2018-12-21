def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    x = 0
    for j in J:
        x = x + S.count(j)
        S = S.replace(j, "")

    return x


print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))