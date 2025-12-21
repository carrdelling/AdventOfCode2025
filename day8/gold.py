

def distance(a, b):
    d = (a[0] - b[0]) ** 2
    d += (a[1] - b[1]) ** 2
    d += (a[2] - b[2]) ** 2

    return d


def solve(data):
    pairs = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            d = distance(data[i], data[j])
            pairs.append((d, i, j))

    pairs.sort()

    clusters = {}
    solution_parts = ... , ...
    for _, a, b in pairs:

        if (a not in clusters) and (b not in clusters):
            nc = max(clusters.values()) + 1 if clusters else 0
            clusters[a] = nc
            clusters[b] = nc
        elif a in clusters and (b not in clusters):
            clusters[b] = clusters[a]
        elif b in clusters and (a not in clusters):
            clusters[a] = clusters[b]
        elif clusters[a] == clusters[b]:
            ...
        else:

            # merge clusters
            good = min(clusters[a], clusters[b])
            bad = max(clusters[a], clusters[b])

            assert good < bad

            for k in clusters:
                if clusters[k] == bad:
                    clusters[k] = good

        # this check has to happen at the end of an iteration
        if len(clusters) == len(data):
            if len(set(clusters.values())) < 2:
                solution_parts = data[a][0], data[b][0]
                break

    solution = solution_parts[0] * solution_parts[1]

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
