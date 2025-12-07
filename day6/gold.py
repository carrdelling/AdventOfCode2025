from collections import defaultdict

def solve(data):

    TN = len(data)
    area = defaultdict(lambda: ' ')
    for i, row in enumerate(data[:TN-1]):
        for j, n in enumerate(row):
            if n != ' ':
                area[(i, j)] = n

    output = 0

    symbol = None
    start = -1
    for x, op in enumerate(data[TN-1]):

        if op in {'+', '*'}:

            if symbol is None:
                symbol = op
                start = x
                continue

            # change to the next
            idx = x-2
            acum = 0 if symbol == '+' else 1
            while idx >= start:
                numbers = [area[(r, idx)] for r in range(4)]
                number = int(''.join(numbers).strip())

                if symbol == '+':
                    acum += number
                else:
                    acum *= number

                idx -= 1
            output += acum
            # prep for next
            symbol = op
            start = x
    else:
        # last column
        # my editor is weird
        idx = max(idx for r, idx in area) -1
        acum = 0 if symbol == '+' else 1
        while idx >= start:
            numbers = [area[(r, idx)] for r in range(4)]
            number = int(''.join(numbers).strip())

            if symbol == '+':
                acum += number
            else:
                acum *= number

            idx -= 1

        output += acum

    return output


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            v = row
            input_.append(v)

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
