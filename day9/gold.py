from itertools import pairwise

def collision(aa, bb, cc, dd, lines):

    for (i, j), (k, l) in lines:
        if i < cc and j < dd and k > aa and l > bb:
            return True

    return False


def solve(data):

    solution = ...
    candidates = []
    for x, y in data:
        for i, j in data:
            if x == i and y == j:
                continue
            aa, cc = min(x, i), max(x, i)
            bb, dd = min(y, j), max(y, j)
            dist_x = cc - aa + 1
            dist_y = dd - bb + 1
            area = dist_x * dist_y
            candidates.append((area, aa, bb, cc, dd))

    candidates = sorted(candidates)[::-1]
    lines = list(pairwise(data + [data[0]]))

    for area, aa, bb, cc, dd in candidates:
        if collision(aa, bb, cc, dd, lines):
            continue
        else:
            solution = area
            # get outta here
            break

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
