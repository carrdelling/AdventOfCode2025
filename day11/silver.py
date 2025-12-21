

def solve(data):

    maze = {}
    for row in data:
        head, rest = row.split(':')
        outs = rest.strip().split()
        maze[head] = set(outs)

    state = ['you']

    solution = 0

    while state:
        current = state.pop()

        if current == 'out':
            solution += 1
            continue

        for o in maze.get(current, []):
            state.append(o)

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
