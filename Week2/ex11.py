def sort_list_of_tuples(tuples_list):
    sorted_list = sorted(tuples_list, key=lambda x: x[1][2] if len(x[1]) > 2 else "")
    return sorted_list


print(sort_list_of_tuples([("abc", "bcd"), ("abc", "zza")]))
