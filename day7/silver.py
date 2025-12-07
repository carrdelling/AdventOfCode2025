
def solve(data):

    area = set()
    rays = set()

    target = len(data)
    output = 0

    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == 'S':
                rays.add((i, j))
            if c == '^':
                area.add((i, j))

    while len(rays) > 0:

        current = set(rays)
        rays = set()

        for i, j in current:
            if i >= target:
                continue
            elif (i + 1, j) in area:
                rays.add((i+1, j-1))
                rays.add((i+1, j+1))
                output += 1
            else:
                rays.add((i + 1, j))

    return output


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            v = row.strip()
            input_.append(v)

    solution = solve(input_)

    print(solution)
    

if __name__ == "__main__":

    main()
