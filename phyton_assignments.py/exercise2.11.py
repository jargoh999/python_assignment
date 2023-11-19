UserNum = int(input("enter  number :"))

digit1 = UserNum %10
rem1 = UserNum // 10

digit2 = rem1 %10
rem2 = rem1 // 10

digit3 = rem2 %10
rem3 = rem2 // 10

digit4 = rem3 % 10
rem4 = rem3 // 10

digit5 = rem4 % 10

 
print( digit5,   digit4,   digit3,    digit2,   digit1    )

