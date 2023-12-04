import re

def replace_numbers_in_letters(text):
    pattern = r'(one|two|three|four|five|six|seven|eight|nine)'

    numbers = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    def replace(match):
        word = match.group(1)
        return numbers.get(word, '')

    result = re.sub(pattern, replace, text)
    return result

sums = []

with open('Day1/input.txt', 'r', encoding='utf-8') as f:
    lines = [line.rstrip() for line in f]
    f.close()

for line in lines:
    numbersLine = []

    for char in line:
        if char.isnumeric():
            numbersLine.append(int(char))
    if len(numbersLine) > 1:
        print(numbersLine, int(str(numbersLine[0]) + str(numbersLine[-1])))
        sums.append(int(str(numbersLine[0]) + str(numbersLine[-1])))

print(sum(sums))