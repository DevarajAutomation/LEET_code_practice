def convert_to_roman(s):
    total=0

    roman_values={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

    for i in range(len(s)-1):
        if roman_values[s[i]] < roman_values[s[i+1]]:
            total -= roman_values[s[i]]

        else:
            total += roman_values[s[i]]

    return total + roman_values[s[-1]]

s="MCMXCIV"
print(convert_to_roman(s))