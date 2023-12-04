with open('input.txt', 'r', encoding='utf-8') as f:
    data = [line.rstrip() for line in f]
    f.close()

sum_points = 0
for line in data:
    points = 0
    line = line.replace("  ", " ")
    line = line.replace("   ", " ")
    card, content = line.split(": ")

    card_id = card.split(" ")[1]

    expected, got = content.split(" | ")
    expected = expected.split(" ")
    got = got.split(" ")
    for number in got:
        if number in expected:
            if points == 0:
                points = 1
            else:
                points *= 2
    sum_points += points

print(sum_points)