def combine(list_1, list_2):
    length_of_list_1 = len(list_1)
    length_of_list_2 = len(list_2)
    combined_list = []
    if length_of_list_1 == length_of_list_2:
        for index in range(length_of_list_1):
            combined_list.append(list_1[index])
            combined_list.append(list_2[index])
    elif length_of_list_1 > length_of_list_2:
        for index in range(length_of_list_2):
            combined_list.append(list_1[index])
            combined_list.append(list_2[index])
        for index in range(length_of_list_2, length_of_list_1):
            combined_list.append(list_1[index])
    else:
        for index in range(length_of_list_1):
            combined_list.append(list_1[index])
            combined_list.append(list_2[index])
        for index in range(length_of_list_1, length_of_list_2):
            combined_list.append(list_2[index])
    print(combined_list)

combine([11,22,33], [1,2,3])