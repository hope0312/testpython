a = int(500)
b = int(100)
c = int(50)
d = int(10)
g = int(5)
f = int(1)

x = int(input("請輸入你的消費金額(值只能介於1~999之間):\n"))
if x >=1 and x <= 999:
  print("")
else:
  print("輸入值只能介於1~999之間，バカ")
  import sys
  sys.exit()
#防止豬頭亂輸入數字
  
y = int(999-x)

q = int(y//a) 
qq = int(y%a)
w = int(qq//b)
ww = int(qq%b)
e = int(ww//c)
ee = int(ww%c)
r = int(ee//d)
rr = int(ee%d)
t = int(rr//g)
tt = int(rr%g)
u = int(tt//f)
uu = int(tt%f)
#除法取餘數與商



z1 = str(",")
z2 = str("；")
x1 = str(",")
x2 = str("；")
c1 = str(",")
c2 = str("；")
v1 = str(",")
v2 = str("；")
b1 = str(",")
b2 = str("；")
n1 = str(",")
n2 = str("；")
#宣告標點浮號



if q ==0:
  a = ""
  q = ""
  z1 = ""
  z2 = ""
else:
  if w==0 and e==0 and r==0 and t==0 and u==0:
    z2=""

if w ==0:
  b = ""
  w = ""
  x1 = ""
  x2 = ""
else:
  if e==0 and r==0 and t==0 and u==0:
    x2=""

if e ==0:
  c = ""
  e = ""
  c1 = ""
  c2 = ""
else:
  if r==0 and t==0 and u==0:
    c2=""

if r ==0:
  d = ""
  r = ""
  v1 = ""
  v2 = ""
else:
  if t==0 and u==0:
    v2=""

if t ==0:
  g = ""
  t = ""
  b1 = ""
  b2 = ""
else:
  if u==0:
    b2=""

if u ==0:
  f = ""
  u = ""
  n1 = ""
  n2 = ""
else:
  if q!=0 or w!=0 or e!=0 or r!=0 or t!=0:
    n2=""

#如果上面數!=該==的數則隱藏。

print("則輸出應該是："+str(a)+z1+str(q)+z2+str(b)+x1+str(w)+x2+str(c)+c1+str(e)+c2+str(d)+v1+str(r)+v2+str(g)+b1+str(t)+b2+str(f)+n1+str(u)+n2)