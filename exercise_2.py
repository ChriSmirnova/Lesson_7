first = [1, 2, 3, 5, 8, 13]
second = [1, 3, 4, 6, 7, 9, 10, 11, 12]
for new_list in set(first):
    if new_list not in second:
        print(new_list)