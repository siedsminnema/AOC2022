from input import get_input

input = get_input(2)
score1, score2 = 0, 0

# result dicts
base_score = {'X': 1, 'Y':2, 'Z':3}
result_score = dict.fromkeys(['C X', 'A Y', 'B Z'], 6) | \
               dict.fromkeys(['A X', 'B Y', 'C Z'], 3) | \
               dict.fromkeys(['B X', 'C Y', 'A Z'], 0)
result_score2 = {'X': 0, 'Y':3, 'Z':6}
base_score2 = dict.fromkeys(['A X', 'C Y', 'B Z'], 3) | \
              dict.fromkeys(['C X', 'B Y', 'A Z'], 2) | \
              dict.fromkeys(['B X', 'A Y', 'C Z'], 1)

# calculate totals
for g in input:
    score1 += base_score[g[2]]
    score1 += result_score[g]
    score2 += base_score2[g]
    score2 += result_score2[g[2]]

print (score1, score2)
