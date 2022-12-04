from input import get_input

input = get_input(4)
subsets = 0
intersections = 0

for i in input:
    begin_1, end_1 = i.split(',')[0].split('-')
    begin_2, end_2 = i.split(',')[1].split('-')
    l1 = [a for a in range(int(begin_1), int(end_1)+1)]
    l2 = [a for a in range(int(begin_2), int(end_2)+1)]
    if set(l1).issubset(set(l2)) or set(l2).issubset(set(l1)):
        subsets += 1
    if len(set(l1).intersection(set(l2))) > 0:
        intersections += 1

print(subsets, intersections)