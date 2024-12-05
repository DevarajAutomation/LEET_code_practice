def needle_haystick(haystack, needle):
    m,n = len(haystack),len(needle)

    for i in range(m-n+1):
        if haystack[i:i+n] == needle:
            return i
        
    return -1




haystack = "leetcode"
needle = "leeto"
print(needle_haystick(haystack,needle))