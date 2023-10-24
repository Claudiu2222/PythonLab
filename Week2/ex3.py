def operations_for_list(list_one, list_two):
    # set_one = set(list_one)
    # set_two = set(list_two)

    # intersection = set_one.intersection(set_two)
    # reunion = set_one.union(set_two)
    # difference_first_second = set_one.difference(set_two)
    # difference_second_first = set_two.difference(set_one)

    intersection = [i for i in list_one if i in list_two]
    difference_first_second = [i for i in list_one if i not in list_two]
    differnece_second_first = [i for i in list_two if i not in list_one]
    reunion = intersection + difference_first_second + differnece_second_first

    return (intersection, difference_first_second, differnece_second_first,reunion)


list_one = [1, 2, 3, 4,4, 5, 6, 7, 8, 9, 10]
list_two = [5, 6, 7, 8, 9,4, 10, 11, 12, 13, 14, 15, 16, 17, 200]

print(operations_for_list(list_one, list_two))
