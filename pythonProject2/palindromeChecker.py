def is_palindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s)-i-1]:
            return False;
    return True;


print(is_palindrome("hello"))