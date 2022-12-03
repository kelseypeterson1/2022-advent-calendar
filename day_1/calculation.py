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

max_calories = max(list(map(lambda elf: sum(elf), elves)))

print(max_calories)
