def generate_grid(N):
    if N <= 0:
        return "0"

    grid = [["#" for _ in range(N)] for _ in range(N)]

    for row in grid:
        print("".join(row))

N = 4
generate_grid(N)
