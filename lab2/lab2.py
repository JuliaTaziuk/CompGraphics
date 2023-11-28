import matplotlib.pyplot as plt

dataset_path = r'C:\Users\User\Downloads\DS1.txt'
points = []
with open(dataset_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        parts = line.strip().split()
        if len(parts) == 2:
                x, y = map(float, parts)
                points.append((x, y))


if points:
    x_values, y_values = zip(*points)
    plt.scatter(x_values, y_values, marker='o', color='blue')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot of Points')
    plt.grid(True)

    output_file_path = 'output_plot.png'
    plt.savefig(output_file_path)

    plt.show()

    print(f"The result was saved in {output_file_path}")









