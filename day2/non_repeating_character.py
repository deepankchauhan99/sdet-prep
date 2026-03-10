inp = "aaabbcdd"
map = {}
for i in inp:
    if i not in map.keys():
        map[i] = 1
    else:
        map[i] += 1

for i in inp:
    if map[i] == 1:
        print(i)
