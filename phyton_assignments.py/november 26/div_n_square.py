def div_n_square(A): 

  if A % 5 == 0 :
     return A ** 0.5 

  elif A % 5 != 0 :
     return A % 5  

print(div_n_square(100))
