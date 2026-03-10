even = [x for x in range(10) if x % 2 == 0]
print(even)
upper = [x.upper() for x in ["qa","sdet","python"]]
print(upper)
longer_than_4 = [x for x in ["abc", "abcd", "ed", "efdad", "a", "adfawq"] if len(x) > 4]
print(longer_than_4)
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened_list = [x for sublist in nested_list for x in sublist]
print(flattened_list)