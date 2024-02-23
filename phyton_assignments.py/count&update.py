sentences = """the palace is a few miles away from the village but going to the palace to see startups is cool and 
fun"""
value = {}
lst = sentences.split()

for word in lst:
    value[word] = lst.count(word)

print(value)
