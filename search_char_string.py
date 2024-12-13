def search_char_string(s,ch):

    for i in range(len(s)):
        if s[i]==ch:
            return i
    return -1

s = "geeksforgeeks" 
ch = 's'

print(search_char_string(s,ch))
