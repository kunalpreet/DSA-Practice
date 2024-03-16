def validPalindrome(s):
    if len(s) == 1:
        return True
    new = ''
    for a in s:
        if a.isalpha() or a.isdigit():
            new += a.lower()

    l, r = 0, len(new) - 1
    while l < r:
        if new[l] != new[r]:
            return False
        l += 1
        r -= 1
    return True

print(validPalindrome("A man, a plan, a canal: Panama"))
