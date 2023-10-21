def get_items_that_appear_x_times(*lists, x):
    appearence_dict = {}
    for list in lists:
        for item in list:
            if item in appearence_dict:
                appearence_dict[item] += 1
            else:
                appearence_dict[item] = 1
    return [item for item in appearence_dict if appearence_dict[item] == x]


print(
    get_items_that_appear_x_times([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=2)
)
