a = int(500)
b = int(100)
c = int(50)
d = int(10)
g = int(5)
f = int(1)

x = int(input("請輸入你的消費金額\n"))
if x >=1 and x <= 1000:
  print("")
else:
  print("ERROR輸入值只能介於1~1,000之間")
  import sys
  sys.exit()
  
y = int(1000-x)

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

print("如果客人消費"+str(x)+"元，你應該找給他"+str(q)+"張500元、"+str(w)+"張100元、"+str(e)+"個50元、"+str(r)+"個10元、"+str(t)+"個5元、"+str(u)+"個1元。")
print("輸出："+str(q)+" "+str(w)+" "+str(e)+" "+str(r)+" "+str(t)+" "+str(u))