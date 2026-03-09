input = "A man, a plan, a canal: Panama"

def palindrome_slicing(str):
    res = [char.lower() for char in str if char.isalnum()]
    res = "".join(res)
    return res[::-1] == res

def palindrome_loop(str):
    l, r = 0, len(str) - 1
    while l < r:
        if str[l].isalnum() and str[r].isalnum():
            if str[l].lower() == str[r].lower():
                l += 1
                r -= 1
            else:
                return False
        elif not str[l].isalnum():
            l +=1
        elif not str[r].isalnum():
            r -= 1
    return True


print(palindrome_slicing(input))
print(palindrome_loop(input))