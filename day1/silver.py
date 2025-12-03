

def solve(data):

    pos = 50
    clicks = 0

    for d, c in data:

        if d == 'L':
            pos_next = pos - c
            while pos_next < 0:
                pos_next += 100
        else:
            pos_next = (pos + c) % 100
            assert d == 'R', f"Bad parsing {d}"

        if pos_next == 0:
            clicks += 1

        pos = pos_next

    output = clicks

    return output


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            v = row.strip()
            input_.append((v[0], int(v[1:])))

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
