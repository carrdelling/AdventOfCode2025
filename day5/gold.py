

def solve(ranges, values):

    ranges.sort(key=lambda x: x[0])
    combined = [ranges[0]]

    for a, b in ranges[1:]:
        if a <= combined[-1][-1]:
            last_id = max(b, combined[-1][-1])
            combined[-1] = (combined[-1][0], last_id)
        else:
            combined.append((a, b))

    output = sum(d - c + 1 for c, d in combined)

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
