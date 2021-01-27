list =[]
list.append(["Bill",50,60])
list.append(["Judy",70,80])
list.append(["Bob",90,100])
list.append(["Mary",40,80])

name = input("姓名:")
mid = int(input("期中成績:"))
final = int(input("期末成績:"))
list.append([name , mid , final])

print("姓名", "期中", "期末")
for i in list:
  print(i[0] , i[1] , i[2])
  
id = int(input("修改第幾位的成績？"))
no = int(input("修改(1)期中考、(2)期末考？"))
newlist = int(input("正確成績是幾分？"))
list[id-1][no] = newlist
print(list)

print("=====================")

for i in list:
  finallist = (i[1]+i[2])/2
  if finallist >=60:
    print(i[0],finallist)
  else:
    print("*"+i[0],finallist)