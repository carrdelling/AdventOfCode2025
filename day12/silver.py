

def solve(data):

    solution = 0
    for row in data:
        if 'x' not in row:
            continue

        pre, post = row.split(':')
        r, c = map(int, pre.split('x'))
        targets = list(map(int, post.strip().split()))

        capacity = (r // 3) * (c // 3)
        req = sum(targets)

        if req <= capacity:
            solution += 1

    return solution


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
