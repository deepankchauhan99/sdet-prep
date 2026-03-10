# Word frequency
# inp = "python automation python testing automation"
# inp_list = inp.split()

# print(inp_list)

# dict = {}

# for i in inp_list:
#     if i not in dict.keys():
#         dict[i] = 1
#     else:
#         dict[i] += 1

# print(dict)

# Group words by length
# a = ["qa","sdet","automation","api", "am", "abc"]

# dict = {}

# for i in a:
#     if len(i) in dict.keys():
#         dict[len(i)].append(i)
#     else:
#         dict[len(i)] = []
#         dict[len(i)].append(i)

# print(dict)

# Sort Dictionary by value
dictinp = {"a":5,"b":2,"c":9}

# Using sorted function
# sorted_dict = dict(sorted(dictinp.items(), key=lambda x: x[1]))
# print(sorted_dict)

# Without sorted function
items = list(dictinp.items())

for i in range(len(items)):
    for j in range(0, len(items)-i-1):
        if items[j][1]>items[j+1][1]:
            items[j], items[j+1] = items[j+1], items[j]
sorted_dict = dict(items)
print(sorted_dict)