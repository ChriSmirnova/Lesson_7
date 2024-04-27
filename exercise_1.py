first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_list = [x for x in set(first) if x in second]
the_end = new_list[::-1]
print(the_end)
