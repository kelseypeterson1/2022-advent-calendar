with open("input_file.txt") as f:
    raw_text = f.readlines()
    input_data = [round.replace("\n","") for round in raw_text]

def calculate_winner_points(opp, me):
    if opp == "A" and me == "Y" or opp == "B" and me == "Z" or opp == "C" and me == "X":
        return 6
    elif opp == "A" and me == "X" or opp == "B" and me == "Y" or opp == "C" and me == "Z":
        return 3
    else:
        return 0

def calculate_choice_points(choice):
    match choice:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3
        
points = 0
for round in input_data:
    points += calculate_winner_points(round[0], round[2]) + calculate_choice_points(round[2])

print(points)