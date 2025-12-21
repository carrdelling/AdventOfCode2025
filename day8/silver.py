from collections import Counter

def distance(a, b):

    d  = (a[0] - b[0]) ** 2
    d += (a[1] - b[1]) ** 2
    d += (a[2] - b[2]) ** 2

    return d


def solve(data):

    pairs = []
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            d = distance(data[i], data[j])
            pairs.append((d, i, j))

    pairs.sort()

    clusters = {}
    for _, a, b in pairs[:1000]:

        if (a not in clusters) and (b not in clusters):
            nc = max(clusters.values()) + 1 if clusters else 0
            clusters[a] = nc
            clusters[b] = nc
            continue

        if a in clusters and (b not in clusters):
            clusters[b] = clusters[a]
            continue

        if b in clusters and (a not in clusters):
            clusters[a] = clusters[b]
            continue

        if clusters[a] == clusters[b]:
            continue

        # merge clusters
        good = min(clusters[a], clusters[b])
        bad = max(clusters[a], clusters[b])

        assert good < bad

        for k in clusters:
            if clusters[k] == bad:
                clusters[k] = good

    sizes = Counter(clusters.values())
    top_3 = sorted(sizes.items(), key=lambda x:-x[1])[:3]

    solution = top_3[0][1] * top_3[1][1] * top_3[2][1]

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
