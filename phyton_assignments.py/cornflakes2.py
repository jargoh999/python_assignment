counter_even = 0 

counter_odd = 0

for numbers in range (0,100):
  if numbers % 2 == 0:
     counter_even += 1

  elif numbers % 2 != 0:
      counter_odd += 1


print("number even numbers are: ",counter_even)

print("number odds numbers are: ",counter_odd)