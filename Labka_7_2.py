"""
Побудувати квадратну матрицю А, елементи якої задаються формулою:

a[i][j]= i! , if (i+j)%2==0 парне
                                                 (i,j)=1,n
         1**2+2**2+3**2+...+j**2 , (i+j)%2==1  непарне

"""
# позначення
"""
n - (nxn), розмірність квадратної матриці;

"""
# введення розмірності

n = int(input("n="))
i = j = n

def sum_j(j):
    return sum(map(lambda el: el ** 2, range(1, j + 1)))


# Введення матриці
def matrix_a(arr):
    for row in arr:
        for el in row:
            print(el, end=' ')
        print()


# Обчислення факторіалу
def factorial(m):
    if m == 0:
        return 1
    else:
        return factorial(m - 1) * m


# введення елементів матриці

def create_a(num):
    a = []
    internal_a = []
    for j in range(num):
        if (i + j) % 2 == 0:
            internal_a.append(factorial(i))
        else:
            internal_a.append(sum_j(j))
        a.append(internal_a)
        return a


# Створення матриці
a = [[factorial(i) if (i + j) % 2 == 0 else sum_j(j) for j in range(n)] for i in range(n)]


z = matrix_a(a)
print(z)

