
def solve(data):

    area = {}
    for i, row in enumerate(data[:4]):
        numbers = list(map(int, row.split()))
        for j, n in enumerate(numbers):
            area[(i, j)] = n

    output = 0

    symbols = [x for x in data[4].split()]
    for x, op in enumerate(symbols):

        if op == '+':
            acum = 0
            for i in range(4):
                acum += area[(i, x)]
            output += acum
        if op == '*':
            acum = 1
            for i in range(4):
                acum *= area[(i, x)]

            output += acum

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
