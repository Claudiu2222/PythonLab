### Ex1


def operations_for_list(list_one, list_two):
    set_one = set(list_one)
    set_two = set(list_two)

    intersection = set_one.intersection(set_two)
    reunion = set_one.union(set_two)
    difference_first_second = set_one.difference(set_two)
    difference_second_first = set_two.difference(set_one)

    return [intersection, reunion, difference_first_second, difference_second_first]


list_one = [i for i in range(1, 10)]
list_two = [i for i in range(5, 20)]

print(operations_for_list(list_one, list_two))

### Ex2


def number_of_occurences(string_to_check: str):
    count_dict = dict()
    for char in string_to_check:
        if char not in count_dict:
            count_dict[char] = 0
        count_dict[char] += 1
    return count_dict


print(number_of_occurences("Ana has apples."))

### Ex3


def are_dictionaries_equal(dict_one, dict_two):
    if (
        type(dict_one) != dict
        or type(dict_two) != dict
        or len(dict_one) != len(dict_two)
    ):
        return False
    for key in dict_one:
        if key not in dict_two:
            return False
        if type(dict_one[key]) != type(dict_two[key]):
            return False
        if compare_values(dict_one[key], dict_two[key]) == False:
            return False
    return True


def are_lists_equal(list_one, list_two):
    if (
        type(list_one) != list
        or type(list_two) != list
        or len(list_one) != len(list_two)
    ):
        return False
    for index in range(len(list_one)):
        if type(list_one[index]) != type(list_two[index]):
            return False
        if compare_values(list_one[index], list_two[index]) == False:
            return False
    return True


def compare_values(value_one, value_two):
    if type(value_one) == dict:
        return are_dictionaries_equal(value_one, value_two)
    elif type(value_one) == list:
        return are_lists_equal(value_one, value_two)
    else:
        return value_one == value_two


dict1 = {
    "a": [{"b": [1, 2, {"x": 3, "y": [{1: 2}, 2, 3]}]}],
    "c": (3, 2),
    "d": {i for i in range(1, 10)},
}
dict2 = {
    "a": [{"b": [1, 2, {"x": 3, "y": [{1: 2}, 2, 3]}]}],
    "c": (3, 2),
    "d": {i for i in range(1, 10)},
}

print(are_dictionaries_equal(dict1, dict2))

### Ex4


def build_xml_element(tag, content, **kwargs):
    xml_element = f"<{tag}"
    for key in kwargs:
        xml_element += f' {key}="{kwargs[key]}"'
    xml_element += f">{content}</{tag}>"
    return xml_element


print(
    build_xml_element(
        "a",
        "Hello there",
        href="http://python.org",
        _class="my-link",
        id="someid",
    )
)

### Ex5


def validate_dict(set_of_tuples, dict_to_check):
    if len(set_of_tuples) != len(dict_to_check):
        return False
    for current_tuple in set_of_tuples:
        if current_tuple[0] not in dict_to_check:
            return False
        if not dict_to_check[current_tuple[0]].startswith(current_tuple[1]):
            return False
        if not dict_to_check[current_tuple[0]].endswith(current_tuple[3]):
            return False
        if current_tuple[2] == "":
            continue
        if (
            current_tuple[2] not in dict_to_check[current_tuple[0]]
            or dict_to_check[current_tuple[0]].startswith(current_tuple[2])
            or dict_to_check[current_tuple[0]].endswith(current_tuple[2])
        ):
            return False
    return True


print(
    validate_dict(
        {
            ("key1", "", "inside", ""),
            ("key2", "start", "middle", "winter"),
            ("key3", "test", "", "test"),
        },
        {
            "key1": "come inside, it's too cold out",
            "key2": "start in the middle of the winter",
            "key3": "test",
        },
    )
)


### Ex6


def get_unique_and_duplicate_elements_count(input):
    unique_elements = set(input)
    return (len(unique_elements), len(input) - len(unique_elements))


print(get_unique_and_duplicate_elements_count([i for i in range(1, 10)] * 3))


### Ex7


def operations_for_given_sets(*sets_to_check):
    operations_dict = dict()
    if len(sets_to_check) < 2:
        return operations_dict
    for index_one in range(len(sets_to_check) - 1):
        for index_two in range(index_one + 1, len(sets_to_check)):
            operations_dict[
                f"{sets_to_check[index_one]} | {sets_to_check[index_two]}"
            ] = (sets_to_check[index_one] | sets_to_check[index_two])
            operations_dict[
                f"{sets_to_check[index_one]} & {sets_to_check[index_two]}"
            ] = (sets_to_check[index_one] & sets_to_check[index_two])
            operations_dict[
                f"{sets_to_check[index_one]} - {sets_to_check[index_two]}"
            ] = (sets_to_check[index_one] - sets_to_check[index_two])
            operations_dict[
                f"{sets_to_check[index_two]} - {sets_to_check[index_one]}"
            ] = (sets_to_check[index_two] - sets_to_check[index_one])
    return operations_dict


print(operations_for_given_sets({1, 2, 3}, {2, 3, 4}, {3, 4, 5}))


### Ex8
def get_loop_list(mapping):
    visited_elements = set()
    loop_list = []
    current_element = mapping["start"]
    while current_element not in visited_elements:
        visited_elements.add(current_element)
        loop_list.append(current_element)
        current_element = mapping[current_element]
    return loop_list


print(
    get_loop_list(
        {
            "start": "a",
            "b": "a",
            "a": "6",
            "6": "z",
            "x": "2",
            "z": "2",
            "2": "2",
            "y": "start",
        }
    )
)


### Ex9


def number_of_found_elements(*args, **kwargs):
    return len([argument for argument in args if argument in kwargs.values()])


print(number_of_found_elements(1, 2, 3, 4, x=1, y=2, z=3, w=5))
