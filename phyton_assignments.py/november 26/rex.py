def my_discount(price,discount):
  rex = price - (price * discount / 100)
  return rex

c = 12
b = 230
a = my_discount(b,c)
print(a)