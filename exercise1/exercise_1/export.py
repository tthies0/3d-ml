"""Export to disk"""


def export_mesh_to_obj(path, vertices, faces):
    """
    exports mesh as OBJ
    :param path: output path for the OBJ file
    :param vertices: Nx3 vertices
    :param faces: Mx3 faces
    :return: None
    """

    # write vertices starting with "v "
    # write faces starting with "f "

    # ###############
    with open(path, 'w') as file:
        # Write each vertex as a line starting with "v"
        for vertex in vertices:
            line = f"v {vertex[0]} {vertex[1]} {vertex[2]}\n"
            file.write(line)

        # Write each face as a line starting with "f"
        for face in faces[0]:
            # OBJ format is 1-indexed, so we add 1 to each vertex index
            line = f"f {face[0] + 1} {face[1] + 1} {face[2] + 1}\n"
            file.write(line)
    # ###############


def export_pointcloud_to_obj(path, pointcloud):
    """
    export pointcloud as OBJ
    :param path: output path for the OBJ file
    :param pointcloud: Nx3 points
    :return: None
    """

    # ###############
    with open(path, 'w') as file:
        # Write each vertex as a line starting with "v"
        for vertex in pointcloud:
            line = f"v {vertex[0]} {vertex[1]} {vertex[2]}\n"
            file.write(line)
    # ###############
