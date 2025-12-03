

def solve(data):

    output = 0
    for row in data:
        max_v = 0
        for x in range(len(row)):
            for y in range(x +1, len(row)):
                v = 10*int(row[x]) + int(row[y])
                max_v = max(v, max_v)
        output+= max_v

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


