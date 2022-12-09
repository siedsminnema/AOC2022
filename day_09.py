from collections import defaultdict

from input import get_input

input = get_input(9)

def follow(x, y, xt, yt):
    # non diagonal moves:
    if xt - x == 2 and yt - y == 0:
        xt -= 1
    if x - xt == 2 and yt - y == 0:
        xt += 1
    if yt - y == 2 and xt - x == 0:
        yt -= 1
    if y - yt == 2 and xt - x == 0:
        yt += 1

    # diagonal moves:
    if xt - x == 2 and yt - y == 1:
        xt -= 1
        yt -= 1
    if x - xt == 2 and yt - y == 1:
        xt += 1
        yt -= 1
    if yt - y == 2 and xt - x == 1:
        yt -= 1
        xt -= 1
    if y - yt == 2 and xt - x == 1:
        yt += 1
        xt -= 1
    if xt - x == -2 and yt - y == -1:
        xt += 1
        yt += 1
    if x - xt == -2 and yt - y == -1:
        xt -= 1
        yt += 1
    if yt - y == -2 and xt - x == -1:
        yt += 1
        xt += 1
    if y - yt == -2 and xt - x == -1:
        yt -= 1
        xt += 1
    if yt - y == 2 and xt - x == 2:
        yt -= 1
        xt -= 1
    if yt - y == 2 and xt - x == -2:
        yt -= 1
        xt += 1
    if yt - y == -2 and xt - x == 2:
        yt += 1
        xt -= 1
    if yt - y == -2 and xt - x == -2:
        yt += 1
        xt += 1

    return xt, yt


tracking = defaultdict(int)
tracking2 = defaultdict(int)
d = dict.fromkeys(range(0, 10), (0,0))
x, y = 0, 0
xt, yt = 0, 0

for i, m in enumerate(input):
    for t in range(int(m.split()[1])):

        if m[0] == 'D':
            y -= 1
        if m[0] == 'U':
            y += 1
        if m[0] == 'R':
            x += 1
        if m[0] == 'L':
            x -= 1

        d[0] = (x, y)
        for k, v in d.items():
            if k == 0:
                continue
            d[k] = follow(d[k-1][0], d[k-1][1], d[k][0], d[k][1])
        tracking[d[1]] = 1
        tracking2[d[9]] = 1

print(len(tracking), len(tracking2))