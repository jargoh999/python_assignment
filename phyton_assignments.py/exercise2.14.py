
age = int(input("enter your age:"))

max_heart_rate = 220 - age
 
min_target_heart_rate = (50/ 100) * max_heart_rate 

max_target_heart_rate = (85/ 100) * max_heart_rate


print( "your max heart rate is :", max_heart_rate)

print( "your target heart rate should be between :", min_target_heart_rate, "-" , max_target_heart_rate)