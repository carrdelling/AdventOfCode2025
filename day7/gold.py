from collections import defaultdict

def solve(data):

    area = set()
    rays = {}
    target = len(data)

    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == 'S':
                rays[j] = 1
            if c == '^':
                area.add((i, j))


    for i in range(1, target):

        current = dict(rays)
        rays = defaultdict(int)

        for j, c in current.items():
            if (i, j) in area:
                rays[j-1] += c
                rays[j+1] += c
            else:
                rays[j] += c

    output = sum(rays.values())

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
