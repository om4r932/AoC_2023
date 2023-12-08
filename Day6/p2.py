with open('input.txt', 'r', encoding='utf-8') as f:
    data = [line.rstrip().replace(' ', '') for line in f]
    f.close()

t = int(data[0].split(':')[1])
d = int(data[1].split(':')[1])
race = (t, d)
possibilities = 0
for ms in range(race[0] + 1):
    speed = ms
    dis = speed*(race[0] - ms)
    if max(race[1], dis) == dis and race[1] != dis:
        possibilities += 1

print(possibilities)