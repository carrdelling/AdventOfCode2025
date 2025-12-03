

def solve(data):

    output = 0
    for a, b in data:

        for i in range(a, b+1):
            s = str(i)
            l = len(s)
            if l % 2 == 1:
                continue
            c = l//2
            x, y = s[:c], s[c:]

            if x == y:
                output += i

    return output


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            vs = row.strip().split(',')
            for v in vs:
                t = v.split('-')
                input_.append((int(t[0]), int(t[1])))

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
