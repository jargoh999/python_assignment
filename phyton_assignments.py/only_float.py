def only_float (A,B):

 if A % 1 != 0 and B % 1 != 0 :

    return 2 

 elif A % 1 != 0 and B % 1 == 0 or A % 1 == 0 and B % 1 != 0:
  
    return 1 

 elif A % 1 == 0 and B % 1 == 0 :
    return 0







num1 = 12
num = 12
print(only_float(num,num1))