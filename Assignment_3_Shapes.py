# 4. shapes with Loops

def shapeswithloops():
    print("Shape - a")
    for row in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == 1:
                s += "#"
            else:
                s += "."
        print(s)
    print()

    print("Shape - b")
    for row in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == row:
                s += "#"
            else:
                s += "."
        print(s)
    print()

    print("Shape - c")
    for row in range(1, 7):
        s = ""
        for x in range(1, 10):
            if 3 <= x <= 6:
                s += "#"
            else:
                s += "."
        print(s)
    print()

    print("Shape - d")
    for row in range(1, 7):
        s = ""
        for x in range(1, 9):
            if row == 3:
                s += "#"
            elif x == 3:
                s += "#"
            else:
                s += "."
        print(s)
    print()

    print("Shape - e")
    for row in range(1, 7):
        s = ""
        for x in range(1, 9):
            if row == 1 and x in (5, 6):
                s += "#"
            elif row == 2 and x == 5:
                s += "#"
            elif row == 3 and x in (4, 5):
                s += "#"
            elif row == 4 and x in (3, 5):
                s += "#"
            elif row == 5 and x in (2, 5):
                s += "#"
            elif row == 6 and x in (1, 5):
                s += "#"
            else:
                s += "."
        print(s)
    print()

    print("shape - f")
    for row in range(1, 7):
        s = ""
        for x in range(1, 9):
            if row == 1 and x in (1, 6):
                s += "#"
            elif row == 2 and x in (2, 5):
                s += "#"
            elif row in (3, 4) and x in (3, 4):
                s += "#"
            elif row == 5 and x in (2, 5):
                s += "#"
            elif row == 6 and x in (1, 6):
                s += "#"
            else:
                s += "."
        print(s)
    print()

    print("Shape - g")
    for row in range(1, 7):
        s = ""
        for x in range(1, 9):   # 8 rows
            if x % 2 == 1:      # odd columns "#"
                s += "#"
            else:
                s += "."        # even positions "."
        print(s)
        print()

    print("Shape - h")
    for row in range(1, 7):
        s = ""
        for x in range(1, 9):
            if row in (2, 5) and 2 <= x <= 7:
                s += "#"
            elif row in (3, 4) and x in (2, 7):
                s += "#"
            else:
                s += "."
        print(s)
    print()

    print("Shape - i")
    for row in range(1, 7):
        s = ""
        for x in range(1, 9):
            if (row + x) % 3 == 0:
                s += "O"
            elif (row + x) % 2 == 0:
                s += "#"
            else:
                s += "."
        print(s)
    print()

    print("Shape - j")
    for row in range(1, 7):
        s = ""
        for x in range(1, 9):
            if row in (1, 2) and x in (3, 6):
                s += "#"
            elif row == 3 and x in (3, 6):
                s += "#"
            elif row == 5 and x in (2, 4, 6):
                s += "#"
            elif row == 6 and x in (1, 3, 5, 7):
                s += "#"
            else:
                s += "."
        print(s)

shapeswithloops()
