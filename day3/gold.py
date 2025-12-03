
def solve(data):

    output = 0

    for row in data:
        acum = ''
        start = 0

        for i in range(12):
            v = '0'

            end = len(row) - 12 + i + 1
            for c in list(range(start, end)):
                if row[c] > v:
                    v = max(v, row[c])
                    start = c + 1
            acum += v

        output+= int(acum)

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
