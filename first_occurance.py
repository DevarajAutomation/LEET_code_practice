def needle_haystick(haystack, needle):
    m,n = len(haystack),len(needle)
    print(m)
    print(n)
    for i in range(m-n+1):
        if haystack[i:i+n] == needle:
            return i
            
        
    return -1


haystack = "sadbutsad"
needle = "sad"
print(needle_haystick(haystack,needle))