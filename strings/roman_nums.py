def romanToInt(s):
    roman = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    total = 0
    n = len(s)

    for i in range(n):
        if i + 1 < n and roman[s[i]] < roman[s[i+1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]

    return total
def intToRoman(num):
    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    result = ""

    for val, symbol in values:
        while num >= val:
            result += symbol
            num -= val

    return result
