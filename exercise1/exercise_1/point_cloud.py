"""Triangle Meshes to Point Clouds"""
import numpy as np


def sample_point_cloud(vertices, faces, n_points):
    """
    Sample n_points uniformly from the mesh represented by vertices and faces
    :param vertices: Nx3 numpy array of mesh vertices
    :param faces: Mx3 numpy array of mesh faces
    :param n_points: number of points to be sampled
    :return: sampled points, a numpy array of shape (n_points, 3)
    """

    # ###############
    points = []
    surface_areas = []
    surface_total = 0
    for face in faces[0]:
        a = vertices[face[0]]
        b = vertices[face[1]]
        c = vertices[face[2]]
        area = tri_area(a, b, c)
        surface_areas.append(area)
        surface_total += area

    propabilities = np.divide(np.array(surface_areas), surface_total)

    for i in range(n_points):
        triangle_index = np.random.choice(range(len(faces[0])), p=propabilities)
        triangle = faces[0][triangle_index]
        a = vertices[triangle[0]]
        b = vertices[triangle[1]]
        c = vertices[triangle[2]]

        r_1 = np.random.random()
        r_2 = np.random.random()
        u = 1 - np.sqrt(r_1)
        v = np.sqrt(r_1)*(1-r_2)
        w = np.sqrt(r_1)*r_2
        points.append(a*u + b*v + c*w)

    return np.array(points)

def tri_area(a,b,c):
    ab=a-b
    ac=a-c
    cross_product = np.cross(ab,ac)
    return 0.5 * np.linalg.norm(cross_product)
    # ###############
