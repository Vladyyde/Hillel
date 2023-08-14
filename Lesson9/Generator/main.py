def generate_grid(N):
    if N <= 0:
        yield "0"

    grid = [["#" for _ in range(N)] for _ in range(N)]

    for row in grid:
        yield "".join(row)

N = 4
grid_generator = generate_grid(N)

for row in grid_generator:
    print(row)
