# Task 3 =================================================================================

# ТЗ: Определите, каких чисел в массиве больше:
# которые делятся (без остатка) на первый элемент массива или
# которые делятся (без остатка) на последний элемент массива.

# Developer notes: Испльзуйте for

# Входные данные:
# input_list = [3, 54, 23, 678, 15, 2322, 798, 34, 33, 1, 23, 54, 45, 2]
# ========================================================================================

input_list = [3, 54, 23, 678, 15, 2322, 798, 34, 33, 1, 23, 54, 45, 2]
count_first = 0
count_last = 0

for i in input_list:
    if i % input_list[0] == 0:
        count_first += 1
    else:
        continue
# ====================================================================
# in this case we don't need else statement. for will do it for us :)     
# ====================================================================

for j in input_list:
    if j % input_list[-1] == 0:
        count_last += 1

if count_first > count_last:
    print("This list contains more numbers that are divisible by the first element.")
elif count_first < count_last:
    print("This list contains more numbers that are divisible by the last element.")
else:
    print("This list has the same number of numbers that are divisible by both the first and the last element of the list.")
