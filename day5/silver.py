

def solve(ranges, values):

    fresh = set()

    for v in values:
        for a, b in ranges:
            if a <= v <= b:
                fresh.add(v)

    output = len(fresh)
    return output


def main():

    input_1 = []
    input_2 = []
    with open('input') as in_f:
        for row in in_f:
            if len(row) < 4:
                continue
            if '-' in row:
                a, b = row.strip().split('-')
                input_1.append((int(a), int(b)))
            else:
                v = row.strip()
                input_2.append(int(v))

    solution = solve(input_1, input_2)

    print(solution)


if __name__ == "__main__":

    main()


