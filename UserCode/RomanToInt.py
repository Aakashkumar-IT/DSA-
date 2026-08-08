def romanToInt(s):

    # Dictionary to store Roman numeral values
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0

    # Traverse each character in the string
    for i in range(len(s)):

        # Check if the current symbol is smaller than the next symbol
        if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]

    return total


# -------- Main Program --------

roman_number = input("Enter a Roman Numeral: ").upper()

result = romanToInt(roman_number)

print("Integer Value =", result)