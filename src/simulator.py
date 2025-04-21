import numpy as np

def simulate_fire(grid_size=20, spread_prob=0.3, max_steps=30):
    """
    Simulates fire spreading in a square grid.
    Fire starts at the center and spreads to neighbors based on probability.

    Args:
        grid_size (int): Size of the square grid (NxN)
        spread_prob (float): Probability of fire spreading to a neighbor
        max_steps (int): Maximum number of simulation steps

    Returns:
        np.ndarray: Final grid showing fire spread
    """
    # Grid values: 0 = unburned, 1 = burning, 2 = burned
    grid = np.zeros((grid_size, grid_size), dtype=int)
    center = grid_size // 2
    grid[center, center] = 1  # start fire at center

    for _ in range(max_steps):
        new_grid = grid.copy()
        burning_cells = np.argwhere(grid == 1)

        for r, c in burning_cells:
            # Try to spread to 4 neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < grid_size and 0 <= nc < grid_size:
                    if grid[nr, nc] == 0 and np.random.rand() < spread_prob:
                        new_grid[nr, nc] = 1
            new_grid[r, c] = 2  # mark cell as burned

        if np.array_equal(grid, new_grid):
            break  # no new spread

        grid = new_grid

    return grid
