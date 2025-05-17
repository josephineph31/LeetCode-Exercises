def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    else:
        for char in s:
            if s.count(char) != t.count(char):
                return False
        return True
s = 'codingisfun'
t = 'iscodingfun'
print(isAnagram(s,t))