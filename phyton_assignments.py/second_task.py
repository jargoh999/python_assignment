count = 1
sets = set()


def remove_item(element1, collection):
    if element1 in collection:
        collection.remove(element1)
        return collection

    return "none"


collect = remove_item(0, sets)
print(collect)


def find_intersection(collection, collection1):
    return set(collection.intersection(collection1))


set1 = {1, 2, 3, 4, 5, 6, 4}
set3 = {1, 2, 3, 4, 6, 7}

print(find_intersection(set1, set3))
