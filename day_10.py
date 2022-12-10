from collections import defaultdict

from input import get_input

input = get_input(10)


def check_strength(c, i, input):
    additions_done = [int(a.split()[1]) for a in input[0:i] if 'addx' in a]
    return (sum(additions_done) + 1) * c


def draw_pixel(CRT_pos, stride_pos):
    if stride_pos <= CRT_pos <= stride_pos + 2:
        pixel = '#'
    else:
        pixel = '.'
    return pixel


totals = []
CRT = ''
current, CRT_pos, stride_pos = 0, 0, 1

for i, c in enumerate(input):
    if c == 'noop':
        current += 1
        CRT_pos += 1
        CRT += draw_pixel(CRT_pos, stride_pos)
        if CRT_pos % 40 == 0:
            CRT += '\n'
            CRT_pos = 0
        if (current + 20) % 40 == 0 and current <= 220:
            totals.append(check_strength(current, i, input))
    if 'addx' in c:
        for _ in range(2):
            current += 1
            CRT_pos += 1
            CRT += draw_pixel(CRT_pos, stride_pos)
            if CRT_pos % 40 == 0:
                CRT += '\n'
                CRT_pos = 0
            if (current + 20) % 40 == 0 and current <= 220:
                totals.append(check_strength(current, i, input))
        stride_pos += int(c.split()[1])

print(sum(totals), '\n', CRT)
