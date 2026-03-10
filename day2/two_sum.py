nums = [2,7,11,15,25,9,17]
target = 24

# Output: [0,1]

output = []
dict = {}

# i is 0 1 2 3
# j is 2 7 11 15
# in dict {2:0, 7:1, 11:2, 15:3}
for i, j in enumerate(nums):
    if j not in dict.keys():
        dict[j] = i

    if target - j in dict.keys() and j != dict[target - j]:
        output.append(dict[target - j])
        output.append(i)
        break

print(output)