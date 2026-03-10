inp = [1,2,2,3,4,4,5]

def remove_duplicate(inp):
    return set(inp)

def remove_duplicate_without_set(inp):
    dict = {}
    for i in inp:
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1
    return [x for x in dict.keys()]

print(remove_duplicate(inp))
print(remove_duplicate_without_set(inp))