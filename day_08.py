from input import get_input

input = get_input(8)
grid = {}

for i, h in enumerate(input):
    grid[i] = h


def is_visible(x,y, heigth):
    xb, xa, yb, ya = True, True, True, True

    for px in range(x+1, len(grid)): # rechts
        if grid[y][px] >= heigth:
            xa = False

    for py in range(y+1, len(grid)): # onder
        if grid[py][x] >= heigth:
            ya = False

    for px in range(0, x): # links
        if grid[y][px] >= heigth:
            xb = False

    for py in range(0, y): # boven
        if grid[py][x] >= heigth:
            yb = False

    return sum([xa, xb, yb, ya]) > 0


def scenic_score(x,y, heigth):
    xb, xa, yb, ya = [x], [len(grid) - 1 - x], [y], [len(grid) - 1 - y]

    for px in range(x+1, len(grid)):
        if grid[y][px] >= heigth:
            xa.append(abs(px - x))

    for py in range(y+1, len(grid)):
        if grid[py][x] >= heigth:
            ya.append(abs(py - y))

    for px in range(0, x):
        if grid[y][px] >= heigth:
            xb.append(abs(px - x))

    for py in range(0, y):
        if grid[py][x] >= heigth:
            yb.append(abs(py - y))

    return min(xb) * min(yb) * min(xa) * min(ya)


scores = []
visible_true = 0

for y, x_total in grid.items():
    for x in range(len(x_total)):
        height = x_total[x]
        if x == 0 or y == 0 or x == len(grid) - 1 or y == len(grid) - 1:
            visible_true += 1
            continue
        elif is_visible(x, y, height):
            visible_true += 1
            scores.append(scenic_score(x, y, height))

print(visible_true, sorted(scores, reverse=True)[0])