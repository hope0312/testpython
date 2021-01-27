a = int(input("請輸入您的身高(公分)：\n"))
b = int(input("請輸入您的體重(公斤)：\n"))
c = a/100
d = c*c
BMI = round(b/d,1)
print("\n您的BMI值為："+str(BMI)+"\n")
if BMI < 18.5:
  print("\"提醒您，您的體重過輕\"")
elif BMI < 24 and BMI >= 18.5:
  print("\"提醒您，您的體重為正常範圍\"")
elif BMI >= 24 and BMI < 27:
  print("\"提醒您，您的體重過重\"")
elif BMI >= 27 and BMI < 30:
  print("\"提醒您，您的體重為輕度肥胖\"")
elif BMI >= 30 and BMI < 35:
  print("\"提醒您，您的體重為中度肥胖\"")
else:
  print("\"提醒您，您的體重為重度肥胖\"")