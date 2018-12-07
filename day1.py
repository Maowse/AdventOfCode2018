result = 0
with open("day1.txt") as f:
    for line in f:
        if(line[:1] == '+'): 
            result += int(line[1:])
        else:
            result -= int(line[1:])

print(result)
