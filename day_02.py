from input import get_input

input = get_input(2)
ts = 0
d = {'X': 1, 'Y':2, 'Z':3}
six = {'X': 'C', 'Y': 'A', 'Z': 'B'}
three = {'X': 'A', 'Y': 'B', 'Z': 'C'}

part2 = {'X': 0, 'Y': 3, 'Z': 6}
X = {'A': 3, 'B': 1, 'C': 2}
Y = {'A': 1, 'B': 2, 'C': 3}
Z = {'A': 2, 'B': 3, 'C': 1}


for g in input:
    ts += d[g[2]]
    if six[g[2]] == g[0]:
        ts += 6
    if three[g[2]] == g[0]:
        ts += 3
    else:
        ts += 0
print(ts)

ts2 = 0
for g in input:
    ts2 += part2[g[2]]
    if g[2] == 'X':
        ts2 += X[g[0]]
    if g[2] == 'Y':
        ts2 += Y[g[0]]
    if g[2] == 'Z':
        ts2 += Z[g[0]]

print (ts2)
