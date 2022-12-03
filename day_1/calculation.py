from heapq import nlargest

with open('input_file.txt') as f:
    text = f.readlines()
    elves = []
    elf = []
    for piece in text:
        if piece != "\n":
            calories = piece.replace("\n","")
            elf.append(int(calories))
        else:
            elves.append(elf)
            elf = []

sum_calories = list(map(lambda elf: sum(elf), elves))
max_calories = max(sum_calories)
print(max_calories)

top_calories = nlargest(3, sum_calories)
print(sum(top_calories))