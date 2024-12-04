with open("./in", "r") as file:
    matrix = [list(line.strip("\n")) for line in file]

directions = [
    (-1, -1),  
    (-1,  0),  
    (-1,  1),  
    ( 0,  1),  
    ( 1,  1),  
    ( 1,  0),  
    ( 0, -1),  
    ( 1, -1),  
]

def is_in_bounds(x, y):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

def check_word(x, y, word):
    word_length = len(word)
    count = 0

    for dx, dy in directions:
        chars = []
        for step in range(word_length):
            nx, ny = x + dx * step, y + dy * step
            if not is_in_bounds(nx, ny):
                break
            chars.append(matrix[nx][ny])
        
        if "".join(chars) == word:
            count += 1
    
    return count

def check_pattern(x, y):
    w1 = ""
    w2 = ""

    # first diagonal
    nx, ny = x - 1, y - 1
    if not is_in_bounds(nx, ny):
        return 0
    w1 += matrix[nx][ny]

    nx, ny = x + 1, y + 1
    if not is_in_bounds(nx, ny):
        return 0
    w1 += matrix[nx][ny]


    # second diagonal
    nx, ny = x - 1, y + 1
    if not is_in_bounds(nx, ny):
        return 0
    w2 += matrix[nx][ny]

    nx, ny = x + 1, y - 1
    if not is_in_bounds(nx, ny):
        return 0
    w2 += matrix[nx][ny]

    if w1 in ["MS", "SM"] and w2 in ["MS", "SM"]:
        return 1
    
    return 0

count1 = 0
count2 = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 'X':
            count1 += check_word(i,j, "XMAS")
        if matrix[i][j] == 'A':
            count2 += check_pattern(i, j)

print(count1)
print(count2)