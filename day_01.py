with open('input_1.txt') as f:
    data = f.read()
    input_list = [i for i in data.split("\n")]

amount = 0
totals = []

for c in input_list:
    try:
        amount += int(c)
    except:
        totals.append(amount)
        amount = 0

st = sorted(totals, reverse=True)
result1 = (st[0])
result2 = (st[0] + st[1] + st[2])

print(result1, result2)