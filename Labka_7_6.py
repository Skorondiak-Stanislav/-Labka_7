"""
Дана цілочислова квадратна матриця. Визначити кількість рядків, у яких елементи упорядковані за зростанням
"""
a = [
    [1, 4, 7, -8],
    [1, 2, 4, 7],
    [6, -24, 2, 1],
    [-4, 2, 5, 1]
    #[True, True, False]
]

s = 0
for i in range(len(a)):
    ordered_iter_obj = map(lambda j: a[i][j - 1] <= a[i][j], range(1, len(a[i])))
    is_ordered = all(ordered_iter_obj)

    # for j in range(1, len(a[i])):
    #     if a[i][j-1] > a[i][j]:
    #         is_ordered = False
    #         break
    if is_ordered:
        s += 1
print(s)