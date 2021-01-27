x1 = int(input("請輸入第一個戶頭餘額:"))
x2 = int(input("請輸入第二個戶頭餘額:"))
y = int(input("請輸入第一個戶頭轉行金額:"))
if y>=0:
  a = x1-y
b = x2+y
if x1<y:
  a = 0
  b = x2+x1
print("第一個戶頭轉帳後餘額:"+str(a)+"\n"+"第二個戶頭轉帳後餘額:"+str(b))