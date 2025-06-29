def isPalindrome(s):
    Str = ''
    for char in s:
        if char.isalnum():
            Str += char.lower()
    return Str == Str[::-1]
s = "I love Keio"
print(isPalindrome(s))