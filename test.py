q = int(50)
w = int(10)
e = int(5)
r = int(1)
print("輸入值只能介於0~10之間")
x = int(input("50元個數:"))
if x >=0 and x <= 10 :
   print("")
else:
   print("ERROR輸入值只能介於0~10之間")
   import sys
   sys.exit()
y = int(input("10元個數:"))
if y >=0 and y <= 10 :
   print("")
else:
   print("ERROR輸入值只能介於0~10之間")   
   import sys
   sys.exit()
z = int(input("5元個數:"))
if z >=0 and z <= 10 :
   print("")
else:
   print("ERROR輸入值只能介於0~10之間")
   import sys
   sys.exit()
i = int(input("1元個數:"))
if i >=0 and i <= 10 :
   print("")
else:
   print("ERROR輸入值只能介於0~10之間")
   import sys
   sys.exit()
print(q*x+w*y+e*z+r*i)