# Task 1 =================================================================================

# ТЗ: Сформировать массив из элементов арифметической прогрессии
# с заданным первым элементом x и разностью d.

# Developer notes: Испльзуйте range() и for

# Входные данные:
# длинна массива = 47
# x = 4
# d = 2
# ========================================================================================
a = 47
x = 4
d = 2


list_arithmetic_progression = []

for i in range(x, a, d):
    list_arithmetic_progression.append(x)
    x += d

print(list_arithmetic_progression)