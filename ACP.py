import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

add = a + b
subtract = a - b
multiply = a * b
divide = a / b
power = a ** 2
modulo = a % b

mean = np.mean(a)
median = np.median(a)
std_dev = np.std(a)
variance = np.var(a)
sum_all = np.sum(a)
min_val = np.min(a)
max_val = np.max(a)

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

dot_product = np.dot(matrix1, matrix2)
elementwise_product = matrix1 * matrix2
transpose = matrix1.T
inverse = np.linalg.inv(matrix1)

x = np.linspace(0, 10, 5)
sine = np.sin(x)
cosine = np.cos(x)
exp = np.exp(x)
log = np.log(x + 1)

print(add)
print(subtract)
print(multiply)
print(divide)
print(power)
print(modulo)
print(mean)
print(median)
print(std_dev)
print(variance)
print(sum_all)
print(min_val)
print(max_val)
print(dot_product)
print(elementwise_product)
print(transpose)
print(inverse)
print(x)
print(sine)
print(cosine)
print(exp)
print(log)