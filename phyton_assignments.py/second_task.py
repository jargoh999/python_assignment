count = 1
sets = set()



#def remove_item(element1, collection):
#    if element1 in collection:
 #       collection.remove(element1)
  #      return collection

   # return "none"


#collect = remove_item(0, sets)
#print(collect)


def inter_section(collection, collection1):
    new_set = set()
    element = 0
    new_set.add(collection.intersection(collection1))
    return new_set

set1 = {1,2,3,4,5}
set3 = {1,2,3,4}

print(inter_section(set1,set3))