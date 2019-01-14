# --- Part Two ---

# Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!

# For example, in the claims above, only claim 3 is intact after all claims are made.

# What is the ID of the only claim that doesn't overlap?


arr = [[[]]*10 for _ in range(10)]
claims = {}

with open("day3.txt") as f:
    for line in f:
        str_arr = line.split(' ')
        coords = str_arr[2].split(',')
        size = str_arr[3].strip().split('x')
        name = str_arr[0]
        claims[name] = 0
        for x in range(int(coords[0]), int(coords[0]) + int(size[0])):
            for y in range(int(coords[1].replace(':', '')), int(coords[1].replace(':', '')) + int(size[1])):
                print(name, arr[x][y], x, y)
                if name not in arr[x][y]:
                    arr[x][y] = arr[x][y] + [name]
                    if len(arr[x][y]) >= 2:
                        for claim in arr[x][y]:
                            claims[claim] = 1
                   
print(claims)
