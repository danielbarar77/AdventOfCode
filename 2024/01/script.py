# my solution
lists = open("./in", "r")

list1 = []
list2 = []

for line in lists:
    line = line.split()
    list1.append(int(line[0]))
    list2.append(int(line[1]))

list1.sort()
list2.sort()

distance = 0
for i in range(len(list1)):
    distance += abs(list1[i] - list2[i])

print(distance)

similiarity = 0
list1 = set(list1)
for id in list1:
    count = 0
    for elem in list2:
        if elem == id:
            count += 1
    similiarity += id * count

print(similiarity)


# found solution
data = [*map(int, open('in').read().split())]
A, B = sorted(data[0::2]), sorted(data[1::2])
print(sum(map(lambda a, b: abs(a-b), A, B)),
      sum(a * B.count(a) for a in A))