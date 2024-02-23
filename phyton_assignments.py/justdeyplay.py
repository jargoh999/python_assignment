count = 1
total = 1
factorial = 1
exp = 1
 
mnp= int (input("enter an exponent "))


num = int (input("enter a number "))

while  count < num :
       new_count = 1
       while  new_count <= count: 
            factorial *= count
            new_count += 1
            
            while exp < mnp:
                 exp *= mnp   
                 mnp+=1

       count += 1  
       total += exp/factorial

print('total is ',total) 

 