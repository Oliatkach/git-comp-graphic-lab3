import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import numpy as np

# Зчитуємо датасет з файлу
def read_dataset(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        points = [list(map(int, line.split())) for line in lines]
    return np.array(points)

# Знаходимо опуклу оболонку
def compute_convex_hull(points):
    hull = ConvexHull(points)
    return hull

# Відображаємо опуклу оболонку та точки
def plot_convex_hull(points, hull_points):
    plt.figure(figsize=(12, 6))
    
    # Відображаємо точки
    plt.scatter(points[:, 0], points[:, 1], c='black', label='Points')
    
    # Відображаємо опуклу оболонку
    for simplex in hull_points:
        plt.plot(points[simplex, 0], points[simplex, 1], 'b-')

    plt.title('Convex Hull')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()

# Зберігаємо результати у файл графічного формату
def save_plot(file_path, points, hull_points):
    plt.figure(figsize=(12, 6))
    
    # Відображаємо точки
    plt.scatter(points[:, 0], points[:, 1], c='black', label='Points')
    
    # Відображаємо опуклу оболонку
    for simplex in hull_points:
        plt.plot(points[simplex, 0], points[simplex, 1], 'b-')

    plt.title('Convex Hull')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    
    # Зберігаємо графіку у файл
    plt.savefig(file_path)
    plt.close()

# Головна частина програми
def main():
    # Зчитуємо датасет з файлу
    file_path = 'DS2.txt'  
    points = read_dataset(file_path)

    # Знаходимо опуклу оболонку
    hull = compute_convex_hull(points)

    # Відображаємо опуклу оболонку та точки
    plot_convex_hull(points, hull.simplices)

    # Зберігаємо результати у файл графічного формату
    save_plot('convex_hull_plot.png', points, hull.simplices)

if __name__ == "__main__":
    main()