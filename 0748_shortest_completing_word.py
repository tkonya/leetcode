def shortestCompletingWord(licensePlate, words):
    licensePlate = ''.join(c for c in licensePlate.lower() if c.isalpha())
    print('new plate: ' + licensePlate)

    shortest = None

    for word in words:
        lpn_temp = licensePlate
        for c in word:
            if c in lpn_temp:
                lpn_temp = lpn_temp[:lpn_temp.find(c)] + lpn_temp[:lpn_temp.find(c) + 1]