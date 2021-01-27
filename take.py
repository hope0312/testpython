a = float(0.05)
b = float(0.12)
print("請輸入你的年收入")
x = int(input("輸入的單位為萬元\n"))
if x <=54:
  print("你應繳的稅率為"+str(round((x*a),2))+"萬元")
else:
  print("你應繳的稅率為"+str(round((54*a)+(x-54)*b,2))+"萬元")