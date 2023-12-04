copies = {}

with open('input.txt', 'r', encoding='utf-8') as f:
    data = [line.rstrip() for line in f]
    for line in data:
        line = line.replace("   ", " ")
        line = line.replace("  ", " ")
        card, content = line.split(": ")

        card_id = card.split(" ")[1]

        expected, got = content.split(" | ")
        expected = expected.split(" ")
        got = got.split(" ")
        copies[int(card_id)] = 1
    f.close()

card_ids = list(copies.keys())

for i in range(len(card_ids)):
    card_id = i+1
    matching = 0
    
    line = data[i]
    line = line.replace("  ", " ")
    line = line.replace("   ", " ")
    card, content = line.split(": ")

    expected, got = content.split(" | ")
    expected = expected.split(" ")
    got = got.split(" ")

    for number in got:
        if number in expected:
            matching += 1

    for i in range(card_id+1, card_id+1+matching):
        copies[i] += 1*copies[card_id]
print("Somme =", sum(copies.values()))