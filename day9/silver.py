

def solve(data):

    solution = 0
    for x, y in data:
        for i, j in data:
            dist_x = abs(x - i) + 1
            dist_y = abs(y - j) + 1
            area = dist_x * dist_y
            solution = max(solution, area)

    return solution


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            v = tuple(map(int, row.strip().split(',')))
            input_.append(v)

    solution = solve(input_)

    print(solution)
    

if __name__ == "__main__":

    main()

