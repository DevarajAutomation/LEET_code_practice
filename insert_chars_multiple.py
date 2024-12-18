def insert_chars_multiple(s,ch):
    s=list(s)
    res=''
    for i in ch:
        for char in range(len(s)):
            if char==i:
                s.insert(i,"*")
                char +=1

    return res.join(s)


str = 'spacing'
chars = [0, 1, 2, 3, 4, 5, 6]
print(insert_chars_multiple(str,chars))