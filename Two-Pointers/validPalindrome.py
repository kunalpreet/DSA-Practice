def validPalindrome(s):
    if len(s) == 1:
        return True

    s = [c.lower() for c in s if c.isalnum()]
    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return False
        l = l + 1
        r = r - 1
    return True


print(validPalindrome("A man, a plan, a canal: Panama"))
