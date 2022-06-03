import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def simple_plot(x, y):
    plt.plot(x, y, label="y = f(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.title("График функции")
    plt.show()


def plot_with_trapecy(x, y, a, b):
    ab = np.linspace(a, b, 10000)
    ab_values = np.exp(ab)
    plt.plot(x, y, label="y = f(x)")
    plt.fill_between(ab, ab_values, np.zeros_like(y), color='red')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.title("Криволинейная трапеция, ограниченная функцией")
    plt.show()


def plot_with_extra_points(x, y, a, b, n, border):
    points = np.linspace(a, b, n + 1)
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y, label="y = f(x)")
    centres = []
    for i in range(n):
        if border == "left":
            x0 = points[i]
        elif border == "center":
            x0 = (points[i] + points[i + 1]) / 2
        elif border == "right":
            x0 = points[i + 1]
        else:
            raise "Uncorrect border Error"
        ax.plot([x0, x0], [0, np.exp(x0)], color="red")
        centres.append(x0)
    ax.scatter(centres, [np.exp(i) for i in centres], color="red")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.title("Значения точек в центрах отрезков")
    plt.show()


def plot_with_steps_figure(x, y, a, b, n, border):
    points = np.linspace(a, b, n + 1)
    values = np.exp(points)
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y, label="y = f(x)")
    ax.scatter(points, values)
    for i in range(n):
        x0, x1 = points[i], points[i + 1]
        if border == "left":
            h = values[i]
        elif border == "center":
            h = (values[i] + values[i + 1]) / 2
        elif border == "right":
            h = values[i + 1]
        ax.add_patch(patches.Polygon([(x0, 0), (x1, 0), (x1, h), (x0, h)], fill=False, color="red"))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.title("Ступенчатая фигура")
    plt.show()


def get_square(a, b, n, border):
    points = np.linspace(a, b, n + 1)
    values = np.exp(points)
    square = 0
    length = points[1] - points[0]
    for i in range(n):
        if border == "left":
            h = values[i]
        elif border == "center":
            h = (values[i] + values[i + 1]) / 2
        elif border == "right":
            h = values[i + 1]
        square += h * length
    return square


def squares_plot(a, b):
    n = range(1, 50)
    left = [get_square(a, b, i, "left") for i in n]
    center = [get_square(a, b, i, "center") for i in n]
    right = [get_square(a, b, i, "right") for i in n]
    plt.plot(n, left, label="Площадь фигур с левыми значениями")
    plt.plot(n, center, label="Площадь фигур с центральными значениями")
    plt.plot(n, right, label="Площадь фигур с правыми значениями")
    plt.legend()
    plt.xlabel("Количество отрезков")
    plt.ylabel("Площадь фигуры")
    plt.show()


def count_square(x, y):
    square = 0
    for i in range(len(x) - 1):
        h = (y[i] + y[i + 1]) / 2
        square += h * abs(x[i] - x[i + 1])
    return square