a = 'abc'
b = 'xyz'


def sort_it(a, b):
    c = a + " " + b
    holder = list()
    result = ''
    for characters in c:
        holder.append(characters)

    for letters in range(0, len(holder)):
        temp = ''
        temp1 = ''
        temp = holder[0];
        holder[0] = holder[-3]
        holder[-3] = temp

        temp1 = holder[1]
        holder[1] = holder[-2]
        holder[-2] = temp1

    for word in holder:
        result += word
    return result

print(sort_it("abc","xyz"))
