import numpy as np
import matplotlib.pyplot as plt

def simulate_fire(grid_size=20, steps=10):
    grid = np.zeros((grid_size, grid_size))
    center = grid_size // 2
    grid[center, center] = 1  # Start fire in the center

    for step in range(steps):
        new_grid = grid.copy()
        for i in range(1, grid_size - 1):
            for j in range(1, grid_size - 1):
                if grid[i, j] == 1:
                    # Spread to neighbors
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if np.random.rand() < 0.3:
                                new_grid[i + dx, j + dy] = 1
        grid = new_grid

    plt.imshow(grid, cmap='hot', interpolation='nearest')
    plt.title("Fire Spread Simulation")
    plt.show()

if __name__ == "__main__":
    simulate_fire()
