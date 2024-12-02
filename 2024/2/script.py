data = open('in').read().split("\n")
lists = [[*map(int, i.split())] for i in data]


count1 = 0
count2 = 0


for list in lists:
    if (sorted(list) == list or sorted(list, reverse=True) == list) and len(set(list)) == len(list):
        ok = 1
        for i in range(len(list) - 1):
            if abs(list[i] - list[i+1]) not in [1, 2, 3]:
                ok = 0
                break
        if ok:
            count1 += 1
            continue
    
    for i in range(len(list)):
        aux = list.copy()
        aux = list[:i] + list[i+1:]
        if sorted(aux) == aux or sorted(aux, reverse=True) == aux:
            ok = 1
            for j in range(len(aux) - 1):
                if abs(aux[j] - aux[j+1]) not in [1, 2, 3]:
                    ok = 0
                    break
            if ok:
                count2 += 1
                break

print(count1)
count2 += count1
print(count2)


