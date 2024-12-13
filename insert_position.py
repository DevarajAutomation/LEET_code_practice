def insert_position(s,ch,pos):
    s=list(s)
    res=''
    for i in range(len(s)):
        if i == pos:
            s.insert(pos,ch)

    return res.join(s)

s="HelloWorld"
c = '!'
pos = 5

print(insert_position(s,c,pos))