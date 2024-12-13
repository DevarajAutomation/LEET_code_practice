def length_two_string(s1,s2):
    if len(s1) != len(s2):
        return 'No'
    else:
        if s1==s2:
            
            return 'Yes'
        else:
            return 'No'
s1 = 'abc'
s2 = 'abc'

print(length_two_string(s1,s2))
