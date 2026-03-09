def string_reverse_loop(str):
    l, r = 0, len(str) - 1
    str_list = list(str)
    while l < r:
        str_list[l], str_list[r] = str_list[r], str_list[l]
        l += 1
        r -= 1

    return "".join(str_list)

def string_reverse_slicing(str):
    return str[::-1]

input = "deepank"
print(string_reverse_loop(input))
print(string_reverse_slicing(input))