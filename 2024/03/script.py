import re
from functools import reduce

data = open("./in").read()

mults = re.findall(r"(mul\(\d{1,3},\d{1,3}\))", data)

total = 0
for mul in mults:
    vals = [int(i) for i in re.findall(r"\d{1,3}", mul)]
    total += reduce(lambda x, y: x*y, vals)

print(total)

mults = re.findall(r"(?:mul\(\d{1,3},\d{1,3}\))|(?:don't\(\))|(?:do\(\))", data)
stats = [*map(lambda x: 1 if x=="don't()" else x, mults)]
stats = [*map(lambda x: 0 if x=="do()" else x, stats)]

total = 0
ok = 1
for i in range(len(mults)):
    if stats[i] == 1:
        ok = 0
        next
    elif stats[i] == 0:
        ok = 1
    if ok and stats[i] != 0 and stats[i] != 1:
        vals = [int(i) for i in re.findall(r"\d{1,3}", mults[i])]
        total += reduce(lambda x, y: x*y, vals)

print(total)