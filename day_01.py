from input import get_input

input = get_input(1)

def sorted_list(list):
    amount = 0
    totals = []
    for c in input:
        if c:
            amount += int(c)
        else:
            totals.append(amount)
            amount = 0
    return sorted(totals, reverse=True)

sl = sorted_list(input)
print(sl[0], sum(sl[0:3]))
