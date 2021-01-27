a = int(input())
b = int(input())
c = int(input())
if a <= b:
  if a <= c:
    print(a, "is the smallest")
  else:
    print(c, "is the smallest")
else:
  if b <= c:
    print(b, "is the smallest")
  else:
    print(c, "is the smallest")