from input import get_input

input = get_input(5)

s = dict.fromkeys(range(1,10), '')
print(s)

# fill dict with strings
for r in reversed(input):
    if '[' in r:
        print(r)
        for row in range(1, 10):
            b = -4 + 4 * row
            e = -1 + 4 * row
            if '[' in r[b:e]:
                s[row] += r[b:e]

print(s)


for i, r in enumerate(input):
    if i < 10:
        continue
    else:
        amount = int((r.split(' from')[0].split('move ')[1]))
        dep = int((r.split('from ')[1].split(' to')[0]))
        arr = int((r.split(' to')[1]))

        depstr = s[dep]
        blocks = s[dep][-amount*3:]
        # s[dep] = s[dep][]
        s[arr] += blocks
        print(r, s[dep], s[arr])
        print(r, depstr, blocks)