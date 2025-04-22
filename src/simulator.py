import numpy as np

def simulate_fire(grid_size=20, spread_prob=0.3, max_steps=30, terrain=None, resistance=None, ignition_points=None):
    """
    Simulates fire spreading in a square grid with optional terrain & resistance.

    Args:
        grid_size (int): Size of the square grid
        spread_prob (float): Base spread probability
        max_steps (int): Max simulation steps
        terrain (np.ndarray): 2D grid (same size) with terrain codes (0=water, 1=urban, 2=forest)
        resistance (np.ndarray): 2D array (0 to 1) representing fire resistance
        ignition_points (list): List of (r, c) tuples where fire starts

    Returns:
        history (list of np.ndarray): List of grid states at each step
    """
    # Fire states
    UNBURNED, BURNING, BURNED = 0, 1, 2

    # Initialize grid
    grid = np.full((grid_size, grid_size), UNBURNED)
    if ignition_points is None:
        ignition_points = [(grid_size // 2, grid_size // 2)]
    for r, c in ignition_points:
        grid[r, c] = BURNING

    # Terrain defaults to forest if not provided
    if terrain is None:
        terrain = np.full((grid_size, grid_size), 2)  # all forest
    if resistance is None:
        resistance = np.zeros((grid_size, grid_size))  # no resistance

    # Terrain multiplier
    terrain_multiplier = {0: 0.0, 1: 0.2, 2: 1.0}

    history = [grid.copy()]

    for _ in range(max_steps):
        new_grid = grid.copy()
        burning_cells = np.argwhere(grid == BURNING)

        for r, c in burning_cells:
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < grid_size and 0 <= nc < grid_size:
                    if grid[nr, nc] == UNBURNED:
                        t = terrain[nr, nc]
                        resist = resistance[nr, nc]
                        prob = spread_prob * terrain_multiplier.get(t, 1.0) * (1 - resist)
                        if np.random.rand() < prob:
                            new_grid[nr, nc] = BURNING
            new_grid[r, c] = BURNED

        if np.array_equal(grid, new_grid):
            break  # no more spread
        grid = new_grid
        history.append(grid.copy())

    return history
