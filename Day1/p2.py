import re
import sys

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}
digittext = "|".join(digits.keys())
dfirst = re.compile("^.*?(" + digittext + ")")
dlast = re.compile(".*(" + digittext + ").*?$")
sum = 0
lines = open("Day1/input.txt", "r", encoding="utf-8").readlines()


for origline in lines:
    line = origline
    final = ""
    add = 0
    m = dfirst.match(line)
    if m:
        add += 10 * int(digits[m.group(1)])
    m = dlast.match(line)
    if m:
        add += 1 * int(digits[m.group(1)])
    sum += add
print(sum)

sys.exit(0)