def compute_tuples(*lists):
    max_length = max(len(x) for x in lists)
    tuples_list = []

    for i in range(0, max_length):
        tuple_elements = []
        for list in lists:
            if i < len(list):
                tuple_elements.append(list[i])
            else:
                tuple_elements.append(None)
        tuples_list.append(tuple(tuple_elements))

    return tuples_list


print(compute_tuples([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))
