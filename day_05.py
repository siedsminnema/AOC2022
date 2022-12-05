from input import get_input

input = get_input(5)


# fill dict with strings
def build_dict(input):
    s = dict.fromkeys(range(1, 10), '')
    for r in reversed(input):
        if '[' in r:
            for row in range(1, 10):
                b = -4 + 4 * row
                e = -1 + 4 * row
                if '[' in r[b:e]:
                    s[row] += r[b:e]
    return s


def move_blocks(s, input, CM9001=True):
    for i, r in enumerate(input):

        if i < 10:
            continue
        else:
            amount = int((r.split(' from')[0].split('move ')[1]))
            dep = int((r.split('from ')[1].split(' to')[0]))
            arr = int((r.split(' to')[1]))

            if CM9001:
                s[arr] += s[dep][-amount * 3:]
                s[dep] = s[dep][:-amount * 3]

            if not CM9001:
                for blocks in range(0, amount):
                    s[arr] += s[dep][-3:]
                    s[dep] = s[dep][:-3]
    return s

s1, s2 = build_dict(input), build_dict(input)
s1 = move_blocks(s1, input, CM9001=False)
s2 = move_blocks(s2, input, CM9001=True)

for item in s1:
    print(s1[item][-2])

for item in s2:
    print("".join([s2[item][-2]]))