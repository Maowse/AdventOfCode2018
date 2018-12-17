# --- Part Two ---

# Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

# The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:

# abcde
# fghij
# klmno
# pqrst
# fguij
# axcye
# wvxyz

# The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

# What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)

# ids = ["abcde",
# "fghij",
# "klmno",
# "pqrst",
# "fguij",
# "axcye",
# "wvxyz"]
ids = []
with open("day2.txt") as f:
    for line in f:
        ids.append(line)

same = []
cont = True
for index in range(0, len(ids)):
    for index2 in range(index + 1, len(ids)):
        same = []
        for letterIndex in range(0, len(ids[index])):
            if ids[index][letterIndex] == ids[index2][letterIndex]:
                same.append(ids[index][letterIndex])

        if len(same) >= len(ids[index]) - 1:
            cont = False
            break
    if cont == False:
        break

print(''.join(same))