def is_palindrome(s):
    left = 0
    right = len(s)
    while left < right:
        if s[left] != s[right-1]:
            return False;
        left= left+1
        right = right-1
    return True;


print(is_palindrome("anna"))
