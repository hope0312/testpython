
n = int(input("請輸入範圍數\n"))
m = int(input("請輸入公倍數\n"))
print("")
y = 0
for i in range(1,n+1):
  if i%m == 0 :
    y = i+y
    print(y,i)
    print("")
print("TOTAL"+" = "+str(y))

'''
for x in range(1, 10):
  for y in range(1, 10):
    print("  "+str(y) + " * " + str(x) + " = " +str(x * y).rjust(2) ,end = "")
  print("")

print("\n\n\n\n\n\n")

for i in range(1,10):
  for j in range(1,10):
    print("  %d * %d = %2d" % (j,i,i*j),end = "")
  print("")
'''