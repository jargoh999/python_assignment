list_for_task = list(range(1, 16))
list_of_copy = list()

for index in list_for_task:
    list_of_copy.append(index)
    list_of_copy.append(index)

set_of_list = set(list_of_copy)
list_of_test = list(set_of_list)


def SumZ(elements):
    sums = 0
    for index2 in range(len(elements)):
        sums += elements[index2]
    return sums


def add_all_third_element(elements):
    list_to_return = []
    for index1 in range(1, len(elements), 3):
        list_to_return.append(index1)

    return SumZ(list_to_return)


def add_all_element_in_order(elements):
    if len(elements) % 2 != 0:
        print(elements)
        list_to_return = [elements[len(elements) - 1], elements[0], elements[len(elements) // 2]]
        print(elements)
        return SumZ(list_to_return)

    print(elements)
    value = (elements[(len(elements) // 2)] + elements[(len(elements) // 2) - 1]) // 2
    print(elements)
    list_to_return = [elements[len(elements) - 1], elements[0], value]
    print(elements)
    return SumZ(list_to_return)


a = list(range(1, 7))
print(add_all_element_in_order(a))
