"""
Ущільнити задану матрицю, вилучаючи із неї рядки і стовпці, заповнені максимальним елементом.
"""
a = [
    [1, 4, 7, -8],
    [1, 2, 4, 7],
    [6, -24, 2, 1],
    [-4, 2, 5, 1]
]

max_num = a[0][0]
for i in range(len(a)):
    for j in range(len(a[i])):
        if max_num < a[i][j]:
            max_num = a[i][j]
            k=j
for el in a:
    el.pop(k)
print(a)