def canPlaceFlowers(flowerbed: list[int], n: int):
    global button
    if len(flowerbed) <= 3 and n == 1:
        return True

    button = (
        (flowerbed[0] == 1)
        or ((sum(flowerbed[:2]) == 0) and (flowerbed[2] == 1))
        or sum(flowerbed[:3]) == 0
    )
    plotable = 0

    def switch():
        global button
        if button:
            button = False
        else:
            button = True

    for bed in flowerbed:
        if button and bed == 1:
            continue
        elif button:
            plotable += 1
            switch()
            continue
        switch()

    return plotable >= n


print(canPlaceFlowers([1, 0, 0, 0, 1], 2))

# x = "1234"
# print(x[-2:])
