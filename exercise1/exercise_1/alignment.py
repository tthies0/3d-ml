""" Procrustes Aligment for point clouds """
import numpy as np
from pathlib import Path


def procrustes_align(pc_x, pc_y):
    """
    calculate the rigid transform to go from point cloud pc_x to point cloud pc_y, assuming points are corresponding
    :param pc_x: Nx3 input point cloud
    :param pc_y: Nx3 target point cloud, corresponding to pc_x locations
    :return: rotation (3, 3) and translation (3,) needed to go from pc_x to pc_y
    """
    R = np.zeros((3, 3), dtype=np.float32)
    t = np.zeros((3,), dtype=np.float32)

    # TODO: Your implementation starts here ###############
    # 1. get centered pc_x and centered pc_y
    mean_x = np.array([0,0,0])
    mean_y = np.array([0,0,0])
    for vert in pc_x:
        mean_x = mean_x + vert
    mean_x = mean_x / len(pc_x)
    for vert in pc_y:
        mean_y = mean_y + vert
    mean_y = mean_y / len(pc_y)
    centered_x = []
    for vert in pc_x:
        centered_x.append(vert - mean_x)
    centered_y = []
    for vert in pc_y:
        centered_y.append(vert - mean_y)
    # 2. create X and Y both of shape 3XN by reshaping centered pc_x, centered pc_y
    X = np.array(centered_x).T
    Y = np.array(centered_y).T

    # 3. estimate rotation
    U, D, V_T = np.linalg.svd(X @ Y.T)

    if np.linalg.det(U) * np.linalg.det(V_T)>0:
        S = np.eye(3)
    else:
        S = np.diag([1,1,-1])
    R = U @ S @ V_T
    print(R@R.T)

    # 4. estimate translation
    t = mean_y- R @ mean_x
    # R and t should now contain the rotation (shape 3x3) and translation (shape 3,)
    # TODO: Your implementation ends here ###############

    t_broadcast = np.broadcast_to(t[:, np.newaxis], (3, pc_x.shape[0]))
    print('Procrustes Aligment Loss: ', np.abs((np.matmul(R, pc_x.T) + t_broadcast) - pc_y.T).mean())

    return R, t


def load_correspondences():
    """
    loads correspondences between meshes from disk
    """

    load_obj_as_np = lambda path: np.array(list(map(lambda x: list(map(float, x.split(' ')[1:4])), path.read_text().splitlines())))
    path_x = (Path(__file__).parent / "resources" / "points_input.obj").absolute()
    path_y = (Path(__file__).parent / "resources" / "points_target.obj").absolute()
    return load_obj_as_np(path_x), load_obj_as_np(path_y)
