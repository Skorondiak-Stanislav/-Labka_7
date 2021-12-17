"""
Дано матрицю А .Перевірити, чи є дана матриця нижньою трикутною матрицею.

"""
a = [
    [5, 4, 7, -8],
    [0, 9, 4, 7],
    [0, 0, 8, 1],
    [0, 0, 0, 0]
]
def is_matrix_triangle(a):
    for i in range(len(a)):
        for j in range(i):
            if a[i][j] != 0:
                return False
    return True
b = is_matrix_triangle(a)
print(b)