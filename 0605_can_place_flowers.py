def canPlaceFlowers(flowerbed, n):

    for i in range(0, len(flowerbed)):
        # is the previous position empty
        if flowerbed[i] == 0 and (i < 1 or flowerbed[i - 1] == 0) and (i + 1 >= len(flowerbed) or flowerbed[i + 1] == 0):
            print('can place at location ' + str(i))
            flowerbed[i] = 1
            n -= 1

    return n <= 0


# print(canPlaceFlowers([1, 0, 0, 0, 1], 1))
# print(canPlaceFlowers([1, 0, 0, 0, 1], 2))
# print(canPlaceFlowers([0, 0, 1, 0, 0], 2))
print(canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
