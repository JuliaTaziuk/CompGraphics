import matplotlib.pyplot as plt
import numpy as np

def affine_transform(point, rotation_center, angle_degrees):
    angle_radians = np.radians(angle_degrees)
    x, y = point
    cx, cy = rotation_center
    x_new = (x - cx) * np.cos(angle_radians) - (y - cy) * np.sin(angle_radians) + cx
    y_new = (x - cx) * np.sin(angle_radians) + (y - cy) * np.cos(angle_radians) + cy
    return x_new, y_new

dataset_path = r'C:\Users\User\Downloads\DS1.txt'
points = []

with open(dataset_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        parts = line.strip().split()
        if len(parts) == 2:
            x, y = map(float, parts)
            points.append((x, y))

if points:
    rotation_center = (480, 480)
    angle_degrees = 20

    transformed_points = [affine_transform(point, rotation_center, angle_degrees) for point in points]

    x_values, y_values = zip(*transformed_points)
    plt.scatter(x_values, y_values, marker='o', color='blue')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot of Transformed Points')
    plt.grid(True)
    plt.axis([0, 960, 0, 960])
    plt.gca().set_aspect('equal', adjustable='box')

    output_file_path = 'output_plot_transformed.png'
    plt.savefig(output_file_path)

    plt.show()

    print(f"The result was saved in {output_file_path}")
