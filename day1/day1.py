

def get_depths():
    depths = []
    with open("input.txt") as f:
        for line in f.readlines():
            depths.append(int(line.replace("\n", "")))
    return depths

depths = get_depths()
changes = []
for index, depth in enumerate(depths):
    if not index:
        continue
    if depth > depths[index - 1]:
        changes.append(depth)
print(len(changes))
