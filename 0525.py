n = int(input("輸入一個>1正整數"))
prime = True
for i in range(2,n):
  if(n % i ==0):
    prime = False
    print(i)
    break
	

if (prime == True):
  print(n,"是質數")
else:
  print(n,"不是質數")