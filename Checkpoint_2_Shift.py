def all_match_with_shift(needle, haystack, shift):
    for i in range(len(needle)):
        if needle[i] != haystack[i + shift]:
            return False
    return True

def is_sublist(needle, haystack):
    for i in range(len(haystack) - len(needle) + 1):
        if all_match_with_shift(needle, haystack, i) == True:
            return True
    return False
            
# Try it out...
h = [3, 2, 4, 3, 1, 2, 3]
n = [3, 1, 2]
print(is_sublist(n, h))
n = [2, 3]
print(is_sublist(n, h))
n = [1, 2, 3, 4]
print(is_sublist(n, h))