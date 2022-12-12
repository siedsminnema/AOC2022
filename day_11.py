import copy
import math
from collections import defaultdict

from input import get_input

input = get_input(11)
monkeys = defaultdict(lambda: defaultdict())

for i, j in enumerate(input):
    if 'Monkey' in j:
        monkeys[j]['items'] = list(map(int, input[i + 1].split(':')[1].split(',')))
        monkeys[j]['operation'] = input[i+2].split("= ")[-1]
        monkeys[j]['test'] = int(input[i+3].split("by ")[-1])
        monkeys[j]['iftrue'] = 'Monkey ' + input[i+4].split()[-1] + ':'
        monkeys[j]['iffalse'] = 'Monkey ' + input[i+5].split()[-1] + ':'


def throwing(md, rounds, bored = True):
    inspections = defaultdict(int)
    lcm = math.lcm(*[md[monkey]["test"] for monkey in md])
    for _ in range(rounds):
        for monkey in md:
            for old in md[monkey]['items']:
                new = eval(md[monkey]['operation'])
                if bored:
                    new = int(new / 3)
                new = new % lcm
                if new % md[monkey]['test'] == 0:
                    to_monkey = md[monkey]['iftrue']
                else:
                    to_monkey = md[monkey]['iffalse']
                md[to_monkey]['items'].append(new)
                inspections[monkey] += 1
            md[monkey]['items'] = []
    return inspections


monkeys2 = copy.deepcopy(monkeys)
i1 = throwing(monkeys, 20)
i2 = throwing(monkeys2, 10000, bored=False)

si1 = sorted(i1, key=i1.get, reverse=True)
si2 = sorted(i2, key=i2.get, reverse=True)

print(i1[si1[0]]*i1[si1[1]], i2[si2[0]]*i2[si2[1]])
