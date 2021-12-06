
def get_input():
    commands = []
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            parsed = line.replace("\n", "").split()
            commands.append((parsed[0], int(parsed[1])))
    return commands

commands = get_input()
horizontal_dir = 0
vertical_dir = 0
for (direction, amt) in commands:
    if direction == "forward":
        horizontal_dir += amt
    elif direction == "down":
        vertical_dir += amt
    elif direction == "up":
        vertical_dir -= amt
    else:
        print("Unexpected direction: " + direction)

print(horizontal_dir)
print(vertical_dir)
print(horizontal_dir * vertical_dir)
