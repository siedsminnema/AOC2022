from collections import defaultdict, deque

from input import get_input

input = get_input(12)

pixels = {} # key = coordinates in tuple, value = place in alphabet
for y, j in enumerate(input):
    for x, l in enumerate(j):
        value = ord(l) - 97
        if l == 'S':
            value = 0
            start = (x, y)
        if l == 'E':
            value = 25
            end = (x, y)
        pixels[(x, y)] = value


possibilities = defaultdict(list) # key = parent, value = possible childs
for c, h in pixels.items():
    if (c[0]+1, c[1]) in pixels and h - pixels[(c[0]+1, c[1])] >= -1 : # right
        possibilities[c].append((c[0]+1, c[1]))
    if (c[0], c[1]+1) in pixels and h - pixels[(c[0], c[1]+1)] >= -1: # down
        possibilities[c].append((c[0], c[1]+1))
    if (c[0]-1, c[1]) in pixels and h - pixels[(c[0]-1, c[1])] >= -1: # left
        possibilities[c].append((c[0]-1, c[1]))
    if (c[0], c[1]-1) in pixels and h - pixels[(c[0], c[1]-1)] >= -1: # up
        possibilities[c].append((c[0], c[1]-1))


def find_shortest_path(possibilities, starting_point, ending_point):

    parent = {starting_point: None}
    dist = {starting_point: 0}
    q = deque()
    q.append(starting_point)

    while q:
        u = q.popleft()
        for n in possibilities[u]:
            if n not in dist:
                parent[n] = u
                dist[n] = dist[u] + 1
                queue.append(n)

    return dist.get(ending_point)


startings_points = [pixel for pixel in pixels if pixels[pixel] == 0]
possible_routes = [find_shortest_path(possibilities, s, end) for s in startings_points]

print(find_shortest_path(possibilities, start, end), min([r for r in possible_routes if r]))


