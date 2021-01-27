for x in range(1, 10):
  for y in range(1, 10):
    print("  "+str(y) + " * " + str(x) + " = " +str(x * y).rjust(2) ,end = "")
  print("")

print("\n\n\n\n\n\n")

for i in range(1,10):
  for j in range(1,10):
    print("  %d * %d = %2d" % (j,i,i*j),end = "")
  print("")