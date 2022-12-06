from input import get_input

input = get_input(6)

def solve(input, marker_length: int):

    buffer = [a for i, a in enumerate(input[0]) if i < marker_length]

    for i, l in enumerate(input[0]):
        if i < marker_length:
            continue
        if len(set(buffer)) == len(buffer):
            return(i)
        else:
            buffer.pop(0)
            buffer.append(l)

print(solve(input, 4), solve(input, 14))



