


def adder(value,product):
      value = 0
      product = 1
      for i in range(1,20,2):
        value += i
        product *= value

      return  value, "" ,product

a = adder(2,3)
print(a)


