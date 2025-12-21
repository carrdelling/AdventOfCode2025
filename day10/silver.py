from collections import deque

def minimum_presses(target, buttons):

    end = {x for x in range(len(target)) if target[x] == '1'}

    states = deque([(set(), 0)])

    while states:
        current = states.popleft()
        cstate, cost = current

        if ((cstate & end) == end) and ((cstate | end) == end):
            return cost

        for b in buttons:
            nstate = {x for x in cstate}
            for n in b:
                if n in nstate:
                    nstate.discard(n)
                else:
                    nstate.add(n)
            states.append((nstate, cost +1))


def solve(data):

    # parse
    solution = 0
    for row in data:
        parts = row.split(' ')
        target = parts[0][1:-1].replace('.', '0').replace('#', '1')
        joltages = eval(parts[-1].replace('{', '[').replace('}', ']'))
        buttons = [tuple(map(int,p[1:-1].split(','))) for p in parts[1:-1]]

        solution += minimum_presses(target, buttons)

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
