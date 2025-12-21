import itertools
from fractions import Fraction


def minimum_presses(buttons, joltages):

    num_rows = len(joltages)
    num_cols = len(buttons)

    # Initialise matrix with zeros
    matrix = [
        [Fraction(0, 1) for _ in range(num_cols + 1)]
        for _ in range(num_rows)
    ]

    # Fill the right-hand side with joltages
    for row, value in enumerate(joltages):
        matrix[row][-1] = Fraction(value, 1)

    # Fill coefficients for each button/tool
    for col, tool in enumerate(buttons):
        for row in tool:
            matrix[row][col] = Fraction(1, 1)

    """
        Part 1
    """

    row_idx = 0
    free_vars = []

    num_cols = len(buttons)
    zero = Fraction(0, 1)

    for col in range(num_cols):
        # Find a pivot row at/under row_idx with a non-zero entry in this column
        pivot_row = next(
            (r for r in range(row_idx, len(matrix)) if matrix[r][col] != zero),
            None,
        )

        if pivot_row is None:
            free_vars.append(col)
            continue

        # Move the pivot row into position
        matrix[row_idx], matrix[pivot_row] = matrix[pivot_row], matrix[row_idx]

        pivot_val = matrix[row_idx][col]

        # Eliminate this column from all other rows
        for r, current_row in enumerate(matrix):
            if r == row_idx:
                continue

            factor = current_row[col]
            if factor == zero:
                continue  # nothing to eliminate

            scale = factor / pivot_val
            for j in range(len(current_row)):
                current_row[j] -= matrix[row_idx][j] * scale

        row_idx += 1

    """
        Part 2
    """

    for row in matrix:
        for i, value in enumerate(row):
            if isinstance(value, Fraction) and value.denominator == 1:
                row[i] = value.numerator

    """
        Part 3
    """

    count = None

    free_var_ranges = [range(max(joltages) + 1) for _ in free_vars]

    for free_values in itertools.product(*free_var_ranges):
        total = sum(free_values)

        if count is not None and total > count:
            continue

        good = True

        for row in matrix:
            # Skip all-zero rows
            if min(row) == 0 and max(row) == 0:
                continue

            # Compute RHS after substituting the free variables
            remaining = row[-1]
            for idx, col in enumerate(free_vars):
                remaining -= row[col] * free_values[idx]

            # Find the first non-zero coefficient (pivot-like)
            pivot = next((x for x in row if x != 0), 0)
            if pivot == 0:
                continue  # should be unreachable if non-all-zero row, but safe

            # Solve remaining / pivot, ensuring it's a non-negative integer
            if isinstance(remaining, int) and isinstance(pivot, int):
                if remaining % pivot != 0:
                    good = False
                    break
                value = remaining // pivot
            else:
                value = remaining / pivot
                if value != int(value):
                    good = False
                    break
                value = int(value)

            if value < 0:
                good = False
                break

            total += value
            if count is not None and total > count:
                good = False
                break

        if good:
            count = total if count is None else min(count, total)

    return count


def solve(data):
    # parse
    solution = 0
    for row in data:
        parts = row.split(' ')
        target = parts[0][1:-1].replace('.', '0').replace('#', '1')
        joltages = eval(parts[-1].replace('{', '[').replace('}', ']'))
        buttons = [tuple(map(int, p[1:-1].split(','))) for p in parts[1:-1]]

        solution += minimum_presses(buttons, joltages)

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
