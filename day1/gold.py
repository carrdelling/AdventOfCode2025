
def solve(data):

    pos = 50
    clicks = 0

    for ds, c in data:

        while c > 100:
            clicks += 1
            c -= 100

        if ds == 'L':
            pos_next = pos - c

            if pos_next < 0:
                if pos != 0:
                    clicks += 1
                pos_next = 100 + pos_next

            if pos_next == 0:
                clicks += 1
        else:
            pos_next = pos + c

            if pos_next >= 100:
                clicks += 1
                pos_next -= 100

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
