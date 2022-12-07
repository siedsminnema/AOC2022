from input import get_input

input = get_input(3)
letters = []
letters2 = []

for s in input:
    half = len(s)/2
    s1 = [j for i, j in enumerate(s) if i < half]
    s2 = [j for i, j in enumerate(s) if i >= half]
    for i in s1:
        if i in s2:
            letters.append(i)
            break


for s in range(0, len(input), 3):
    s1, s2, s3 = input[s], input[s+1], input[s+2]
    s1 = [i for i in s1]
    s2 = [i for i in s2]
    s3 = [i for i in s3]
    for i in s1:
        if i in s2 and i in s3:
            letters2.append(i)
            break

def let_to_num(l):
    numbers = []
    for i in l:
        if i.islower():
            numbers.append(ord(i) - 96)
        if i.isupper():
            numbers.append(ord(i) - 64 + 26)
    return numbers

print(sum(let_to_num(letters)), sum(let_to_num(letters2)))