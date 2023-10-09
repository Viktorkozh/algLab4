import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

AmountOfDots = 1000 #Количество точек
AOD = (AmountOfDots + 1) * 10
a = {}
worstTimefindMin = {}
worstTimefindMax = {}
GraphStuff = [i for i in range(10, AOD, 10)]
StuffForLsmWorstfindMin = {}
StuffForLsmWorstfindMax = {}

def findMin():
    min = 99999999999
    for i in range(len(a)):
        if a[i] < min:
            min = a[i]
    return min

def findMax():
    max = -99999999999
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    return max

def fillArr(numOfEl):
    a.clear()
    for i in range(numOfEl):
        a[i] = random.randint(0, 10000000000)

for i in range(10, AOD, 10):
    fillArr(i)
    worstTimefindMin[i] = (timeit.timeit(lambda:findMin(), number = 10)) / 50

for i in range(10, AOD, 10):
    fillArr(i)
    worstTimefindMax[i] = (timeit.timeit(lambda:findMax(), number = 10)) / 50

A = np.vstack([GraphStuff, np.ones(len(GraphStuff))]).T
y = np.array(list(worstTimefindMin.values()))[:, np.newaxis]
alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),np.array(list(worstTimefindMin.values()))) # Взято из книги "Python Programming And Numerical Methods: A Guide For Engineers And Scientists": https://pythonnumericalmethods.berkeley.edu/notebooks/chapter16.04-Least-Squares-Regression-in-Python.html

plt.figure(1).set_figwidth(8)
plt.xlabel('Количество элементов в массиве')
plt.ylabel('Среднее время выполнения (секунды)')
plt.title('Зависимость времени поиска минимального элемента от размера массива')
plt.scatter(GraphStuff, worstTimefindMin.values(), s=5)
plt.grid(False)
plt.plot(GraphStuff, alpha[0]*np.array(list(GraphStuff)) + alpha[1], 'r')

formatted_alpha = [format(a, '.10f') for a in alpha]
print('Коэффциенты прямой худшего случая: a =', formatted_alpha[0], 'b =', formatted_alpha[1])
print('Worst time for finding min value correlation', np.corrcoef(GraphStuff, list(worstTimefindMin.values()))[0, 1])

A = np.vstack([GraphStuff, np.ones(len(GraphStuff))]).T
y = np.array(list(worstTimefindMax.values()))[:, np.newaxis]
alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),np.array(list(worstTimefindMax.values())))

plt.figure(2).set_figwidth(8)
plt.xlabel('Количество элементов в массиве')
plt.ylabel('Среднее время выполнения (секунды)')
plt.title('Зависимость времени поиска максимального элемента от размера массива')
plt.scatter(GraphStuff, worstTimefindMax.values(), s=5)
plt.grid(False)
plt.plot(GraphStuff, alpha[0]*np.array(list(GraphStuff)) + alpha[1], 'r')

formatted_alpha = [format(a, '.10f') for a in alpha]
print('Коэффициенты прямой среднего случая: a =', formatted_alpha[0], 'b =', formatted_alpha[1])
print('Median time for finding max value correlation', np.corrcoef(GraphStuff, list(worstTimefindMax.values()))[0, 1])

plt.show()