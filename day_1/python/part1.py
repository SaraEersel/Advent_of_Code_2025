import sys

with open(sys.argv[1], 'r') as file:
    lines = [line.strip() for line in file.readlines()]

dail = 50
solution = 0

for line in lines:
    if line[0] == 'L':
        number = int(line[1:])
        dail -= number
    elif line[0] == 'R':
        number = int(line[1:])
        dail += number

    dail %= 100
    if dail == 0:
        solution += 1

print(solution)   

