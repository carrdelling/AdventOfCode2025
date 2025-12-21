from functools import cache


def solve(data):

    maze = {}
    for row in data:
        head, rest = row.split(':')
        outs = rest.strip().split()
        maze[head] = set(outs)

    # sorry, I am too lazy to avoid this
    @cache
    def count_paths(start, end):
        if start == end:
            return 0
        if end in maze.get(start, {}):
            return 1
        else:
            exits = maze.get(start, {})
            all_paths = 0
            for x in exits:
                all_paths += count_paths(x, end)
            return all_paths


    # dac first
    dac = count_paths('svr', 'dac')
    dac *= count_paths('dac', 'fft')
    dac *= count_paths('fft', 'out')

    # fft first
    fft = count_paths('svr', 'fft')
    fft *= count_paths('fft', 'dac')
    fft *= count_paths('dac', 'out')

    # combine
    solution = dac + fft

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
