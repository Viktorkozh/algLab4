import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

amount_of_dots = 1000  # Количество точек
aod = (amount_of_dots + 1) * 10
a = {}
worst_time_find_min = {}
worst_time_find_max = {}
graph_stuff = [i for i in range(10, aod, 10)]
stuff_for_lsm_worst_find_min = {}
stuff_for_lsm_worst_find_max = {}


def find_min():
    min = 99999999999
    for i in range(len(a)):
        if a[i] < min:
            min = a[i]
    return min


def find_max():
    max = -99999999999
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    return max


def fill_arr(num_of_elements):
    a.clear()
    for i in range(num_of_elements):
        a[i] = random.randint(0, 10000000000)


for i in range(10, aod, 10):
    fill_arr(i)
    worst_time_find_min[i] = (timeit.timeit(lambda: find_min(), number=10)) / 50

for i in range(10, aod, 10):
    fill_arr(i)
    worst_time_find_max[i] = (timeit.timeit(lambda: find_max(), number=10)) / 50

A = np.vstack([graph_stuff, np.ones(len(graph_stuff))]).T
y = np.array(list(worst_time_find_min.values()))[:, np.newaxis]
alpha = np.dot(
    (np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)),
    np.array(list(worst_time_find_min.values())),
)  # Взято из книги "Python Programming And Numerical Methods: A Guide For Engineers And Scientists": https://pythonnumericalmethods.berkeley.edu/notebooks/chapter16.04-Least-Squares-Regression-in-Python.html

plt.figure(1).set_figwidth(8)
plt.xlabel("Количество элементов в массиве")
plt.ylabel("Среднее время выполнения (секунды)")
plt.title("Зависимость времени поиска минимального элемента от размера массива")
plt.scatter(graph_stuff, worst_time_find_min.values(), s=5)
plt.grid(False)
plt.plot(graph_stuff, alpha[0] * np.array(list(graph_stuff)) + alpha[1], "r")

formatted_alpha = [format(a, ".10f") for a in alpha]
print(
    "Коэффциенты прямой поиска минимального объекта в массиве: a =",
    formatted_alpha[0],
    "b =",
    formatted_alpha[1],
)
print(
    "Time spent searching min value correlation",
    np.corrcoef(graph_stuff, list(worst_time_find_min.values()))[0, 1],
)

A = np.vstack([graph_stuff, np.ones(len(graph_stuff))]).T
y = np.array(list(worst_time_find_max.values()))[:, np.newaxis]
alpha = np.dot(
    (np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)),
    np.array(list(worst_time_find_max.values())),
)

plt.figure(2).set_figwidth(8)
plt.xlabel("Количество элементов в массиве")
plt.ylabel("Среднее время выполнения (секунды)")
plt.title("Зависимость времени поиска максимального элемента от размера массива")
plt.scatter(graph_stuff, worst_time_find_max.values(), s=5)
plt.grid(False)
plt.plot(graph_stuff, alpha[0] * np.array(list(graph_stuff)) + alpha[1], "r")

formatted_alpha = [format(a, ".10f") for a in alpha]
print(
    "Коэффициенты прямой максимального объекта в массиве: a =",
    formatted_alpha[0],
    "b =",
    formatted_alpha[1],
)
print(
    "Time spent searching max value correlation",
    np.corrcoef(graph_stuff, list(worst_time_find_max.values()))[0, 1],
)

plt.show()