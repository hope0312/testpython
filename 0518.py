for x in range(1, 10):
  for y in range(1, 10):
    if(x*y > 9):
      print(str(y) + " * " + str(x) + " = " +str(x * y),end = " | ")
    else:
      print(str(y) + " * " + str(x) + " = 0" +str(x * y),end = " | ")
  print("")
  
print("\n\n\n")

for i in range(1,10):
  for j in range(1,10):
    print("  %d * %d = %2d" % (j,i,i*j),end = "")
  print("")