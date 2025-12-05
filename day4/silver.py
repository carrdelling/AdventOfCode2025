
def neighbours(x, y):

    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            if a == 0 and b == 0:
                continue
            yield x+ a, y + b

def solve(data):

    grid = set()

    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == '@':
                grid.add((i, j))

    output = 0
    for i, j in grid:
        count = 0
        for ii, jj in neighbours(i, j):
            if (ii, jj) in grid:
                count += 1

        if count < 4:
            output += 1


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
