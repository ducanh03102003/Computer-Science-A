def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion"]

    if n == 0:
        return "zero"

    def group_to_words(n):
        words = []
        if n >= 100:
            words.append(ones[n // 100])
            words.append("hundred")
            n %= 100
        if n >= 20:
            words.append(tens[n // 10])
            n %= 10
        if n >= 10:
            words.append(teens[n - 10])
        elif n > 0:
            words.append(ones[n])
        return " ".join(words)

    result = []
    group_idx = 0
    while n > 0:
        n, remainder = divmod(n, 1000)
        group_words = group_to_words(remainder)
        if group_words:
            result.append(group_words + " " + thousands[group_idx])
        group_idx += 1

    return " ".join(reversed(result)).strip()

# Ask user for input
while True:
    try:
        user_input = int(input("Enter a non-negative integer (0 to exit): "))
        if user_input == 0:
            print("Exiting program.")
            break
        if user_input > 0:
            print(number_to_words(user_input))
        else:
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
