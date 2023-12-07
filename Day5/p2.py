import sys

with open('input.txt', 'r', encoding='utf-8') as f:
    data = [line.rstrip() for line in f]
    data_test = data[5:]
    f.close()

seeds = []
seed_soil = []
soil_fert = []
fert_water = []
water_light = []
light_temp = []
temp_humid = []
humid_loc = []



i = 0
while i < len(data):
    try:
        line = data[i]
        if "seeds: " in line:
            seeds += line.split(": ")[1].split(" ")
        elif "seed-to-soil" in line:
            i += 1
            line = data[i]
            while line not in ["", "\n", "\n\n", " "]:
                line = data[i]
                if line.split(" ") != [""]:
                    seed_soil.append(line.split(" "))
                    i += 1
        elif "soil-to-fertilizer" in line:
            i += 1
            line = data[i]
            while line not in ["", "\n", "\n\n", " "]:
                line = data[i]
                if line.split(" ") != [""]:
                    soil_fert.append(line.split(" "))
                    i += 1
        elif "fertilizer-to-water" in line:
            i += 1
            line = data[i]
            while line not in ["", "\n", "\n\n", " "]:
                line = data[i]
                if line.split(" ") != [""]:
                    fert_water.append(line.split(" "))
                    i += 1
        elif "water-to-light" in line:
            i += 1
            line = data[i]
            while line not in ["", "\n", "\n\n", " "]:
                line = data[i]
                if line.split(" ") != [""]:
                    water_light.append(line.split(" "))
                    i += 1
        elif "light-to-temperature" in line:
            i += 1
            line = data[i]
            while line not in ["", "\n", "\n\n", " "]:
                line = data[i]
                if line.split(" ") != [""]:
                    light_temp.append(line.split(" "))
                    i += 1
        elif "temperature-to-humidity" in line:
            i += 1
            line = data[i]
            while line not in ["", "\n", "\n\n", " "]:
                line = data[i]
                if line.split(" ") != [""]:
                    temp_humid.append(line.split(" "))
                    i += 1
        elif "humidity-to-location" in line:
            i += 1
            line = data[i]
            while line not in ["", "\n", "\n\n", " "]:
                line = data[i]
                if line.split(" ") != [""]:
                    humid_loc.append(line.split(" "))
                    i += 1
        i += 1
    except:
        continue

glob = [seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc]
loc_values = []

# Seed l[1] -> Soil l[0]
for i in range(len(seeds)):
    if i % 2 == 0:
        proto = list(range(int(seeds[i]), (int(seeds[i]) + int(seeds[i + 1]) + 1)))
        print(len(proto))
        for seed in proto:
            sys.stdout.write(f"\r{round(proto.index(seed)+1/len(proto), 2)}%")
            mapping = [seed]    
            for m in glob:
                actual_length = len(mapping)
                for l in m:
                    if int(l[1]) <= mapping[actual_length - 1] <= int(l[1])+int(l[2]):
                        mapping.append(mapping[actual_length - 1] + (int(l[0]) - int(l[1])))
                        break
                if actual_length == len(mapping):
                    mapping.append(mapping[actual_length - 1])
            loc_values.append(mapping[-1])
            sys.stdout.flush()
print(min(loc_values))

# Still waiting (bro my house is at least 55°C, we're literally dying)
# Im gonna post it but i'll find a solution for that