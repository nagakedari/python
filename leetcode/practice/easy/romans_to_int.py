def roman_to_int(s):
    roman_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    int_val = 0
    for i in range(0, len(s)-1):
        if roman_map[s[i]] < roman_map[s[i+1]]:
            int_val -= roman_map[s[i]]
        else:
            int_val += roman_map[s[i]]

    return int_val+roman_map[s[-1]]


if __name__ == "__main__":
    print(roman_to_int("III"))
    print(roman_to_int("LVIII"))
    print(roman_to_int("MCMXCIV"))