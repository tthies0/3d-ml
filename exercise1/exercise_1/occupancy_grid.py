"""SDF to Occupancy Grid"""
import numpy as np


def occupancy_grid(sdf_function, resolution):
    """
    Create an occupancy grid at the specified resolution given the implicit representation.
    :param sdf_function: A function that takes in a point (x, y, z) and returns the sdf at the given point.
    Points may be provides as vectors, i.e. x, y, z can be scalars or 1D numpy arrays, such that (x[0], y[0], z[0])
    is the first point, (x[1], y[1], z[1]) is the second point, and so on
    :param resolution: Resolution of the occupancy grid
    :return: An occupancy grid of specified resolution (i.e. an array of dim (resolution, resolution, resolution) with value 0 outside the shape and 1 inside.
    """

    # ###############
    grid_size = .33
    cell_size = (grid_size * 2) / resolution
    i_to_point = np.mgrid[-grid_size:grid_size:cell_size]
    grid = np.zeros((resolution, resolution, resolution))
    for x in range(resolution):
        for y in range(resolution):
            x_values = np.full_like(i_to_point, i_to_point[x])
            y_values = np.full_like(i_to_point, i_to_point[y])

            vals = sdf_function(x_values, y_values, i_to_point)
            vals_occu = (vals < 0).astype(int)
            grid[x][y] = vals_occu
    return grid
    # ###############
