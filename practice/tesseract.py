import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_tesseract():
    # Define vertices of a 4D tesseract
    points = np.array([[-1, -1, -1, -1], [1, -1, -1, -1], [1, 1, -1, -1], [-1, 1, -1, -1],
                       [-1, -1, 1, -1], [1, -1, 1, -1], [1, 1, 1, -1], [-1, 1, 1, -1],
                       [-1, -1, -1, 1], [1, -1, -1, 1], [1, 1, -1, 1], [-1, 1, -1, 1],
                       [-1, -1, 1, 1], [1, -1, 1, 1], [1, 1, 1, 1], [-1, 1, 1, 1]])
    return points

def rotate_4d(points, angle, axis1=0, axis2=1):
    rotation_matrix = np.eye(4)
    c, s = np.cos(angle), np.sin(angle)
    rotation_matrix[axis1, axis1] = c
    rotation_matrix[axis1, axis2] = -s
    rotation_matrix[axis2, axis1] = s
    rotation_matrix[axis2, axis2] = c
    return np.dot(points, rotation_matrix)

def project_to_3d(points):
    # Simple projection that ignores the 4th dimension
    return points[:, :3]

def plot_tesseract(points_3d):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4),
             (0, 4), (1, 5), (2, 6), (3, 7), (8, 9), (9, 10), (10, 11), (11, 8),
             (12, 13), (13, 14), (14, 15), (15, 12), (8, 12), (9, 13), (10, 14), (11, 15),
             (0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15)]
    for edge in edges:
        point1, point2 = points_3d[edge[0]], points_3d[edge[1]]
        ax.plot3D(*zip(point1, point2), color="b")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    return fig

st.title("4D Tesseract Visualizer")

angle1 = st.slider("Rotation Angle XY (in radians)", -np.pi, np.pi, 0.0, 0.01)
angle2 = st.slider("Rotation Angle XZ (in radians)", -np.pi, np.pi, 0.0, 0.01)
angle3 = st.slider("Rotation Angle XW (in radians)", -np.pi, np.pi, 0.0, 0.01)

tesseract_points = generate_tesseract()
tesseract_points = rotate_4d(tesseract_points, angle1, 0, 1)
tesseract_points = rotate_4d(tesseract_points, angle2, 0, 2)
tesseract_points = rotate_4d(tesseract_points, angle3, 0, 3)
points_3d = project_to_3d(tesseract_points)

fig = plot_tesseract(points_3d)
st.pyplot(fig)
