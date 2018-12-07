repeated_freq = 0
current = []
new = 0
run = True

with open("day1.txt") as f:
    while run:
        f.seek(0)
        for line in f:
            if(line[:1] == '+'): 
                new += int(line[1:])
            else:
                new -= int(line[1:])

            if(new in current):
                repeated_freq = new
                print('gonna break')
                run = False
                break
            else:
                current.append(new)

            
print(repeated_freq)