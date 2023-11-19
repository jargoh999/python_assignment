num1 = float(input("enter number:"))

num2 = float(input("enter number:"))

num3 = float(input("enter number:"))


if num1 > num2 and num2 > num3 :

    print( num1 , num2 , num3)


elif num1 < num2 and num1 < num3 :

    print( num3, num2 , num1)

elif num2 > num1 and num1 > num3 :
 
    print( num2,num1,num3)

elif num2 < num1 and num1 < num3 :

    print(num3, num1, num2)
 
elif num3 > num2 and num2 > num1 :
    
    print( num3,num2,num1)

elif num3 < num2 and num2 < num1  :

      print( num1, num2, num3)