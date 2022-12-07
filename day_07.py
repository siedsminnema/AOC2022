import collections
import json

from input import get_input
from collections import defaultdict

input = get_input(7)

def count_bytes(d):
    # function to count size of a folder recursively
    bytesize = 0
    for k, v in dirs[d].items():
        if v != 'dir':
            bytesize += int(v)
        if v == 'dir':
            inside_dir = d + '/' + k
            bytesize += count_bytes(inside_dir)
    return bytesize

dirs = defaultdict(lambda: defaultdict(dict))
dirs_size = defaultdict(int)

# Make the filesystem in dirs
current_path = '/'
for i in input:
    if i == '$ cd /':
        current_path = '/'
    elif i == '$ cd ..':
        current_path = current_path.rsplit('/',1)[0]
    elif 'cd ' in i:
        current_path += '/' + i.split()[2]
    if '$' not in i:
        dir_or_size, name = i.split()[0], i.split()[1]
        dirs[current_path][name] = dir_or_size

# Calculate the size of each folder
for f in dirs:
    bytesize = count_bytes(f)
    dirs_size[f] = bytesize

# Calculate the answers
answer1 = sum([dirs_size[k] for k in dirs_size if dirs_size[k] < 100000])
answer2 = min([dirs_size[k] for k in dirs_size if dirs_size[k] > dirs_size['/'] - 40000000])
print(answer1, answer2)
