for x in range(1,11):
  for y in range(1,x+1):
    print("*",end = "")
  print()
'''print("\n\n\n\n")'''
for x in range(1,11):
  for y in range(x-1,10):
    print("*",end = "")
  print()
  
''' (x-1,10)裡面也可以輸入10-i '''

for i in range(10):
  for j in range(i):
    print(" ",end = "")
  for j in range(10-i):
    print("*",end = "")
  print("")

'''print("\n\n\n\n") '''

for i in range(10):
  for j in range(10-i-1):
    print(" ",end = "")
  for j in range(i+1):
    print("*", end = "")
  print("") 
  
