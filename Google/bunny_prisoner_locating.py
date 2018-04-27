def bunny_prisoner_locating(x,y):
    bunnyID = 1
    # to move one space to the right, we add (row+col) to the bunnyID

    # shift to correct row
    for r in range(1,y):
        bunnyID += r
    for c in range(1,x):
        bunnyID += y+c
    return bunnyID
i = bunny_prisoner_locating(3,2)
print(i)
