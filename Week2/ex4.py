def compose(list_of_notes, list_of_order, start_position):
    final_notes_list = [list_of_notes[start_position]]
    current_index = start_position
    list_length = len(list_of_notes)
    for i in list_of_order:
        current_index = (current_index + i) % list_length
        final_notes_list.append(list_of_notes[current_index])
    return final_notes_list


print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
