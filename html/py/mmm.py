a = [5,3,8,6,7,20,30,56,76,5]
total = 0
for i in range(len(a)):
   if a[i] % 2 == 0:
       total += a[i]
print(total)