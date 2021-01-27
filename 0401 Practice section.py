a = int(input("請輸入您的身高(公分)：\n"))
b = int(input("請輸入您的體重(公斤)：\n"))
c = a/100
d = c*c
BMI = round(b/d,2)
print("您的BMI值為："+str(BMI))
print("\"提醒您，正常BMI範圍為18.5~24之間\"")