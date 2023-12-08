with open('input.txt', 'r', encoding='utf-8') as f:
    data = [line.rstrip() for line in f]
    f.close()

testT = data[0]
testD = data[1]
testT_splitted = testT.split(' ')
testD_splitted = testD.split(' ')
time = [int(testT_splitted[i]) for i in range(len(testT_splitted)) if testT_splitted[i].isnumeric()]
records = [int(testD_splitted[i]) for i in range(len(testD_splitted)) if testD_splitted[i].isnumeric()]


race_id = 1
res = 1
for i in range(len(time)):
    possibilities = 0
    race = (time[i], records[i])
    for ms in range(race[0] + 1):
        speed = ms
        dis = speed*(race[0] - ms)
        if max(race[1], dis) == dis and race[1] != dis:
            possibilities += 1
    res *= possibilities
    race_id += 1

print(res)