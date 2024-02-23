def list_one(lest):
   niche = []
   for i in lest:
       niche.append(i)
   niche[0] = 0
   niche[-1] = 0
   return niche 

num = [1,2,3,4,5,6,7,8,9,10]
print(list_one(num))

  
