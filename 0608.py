gradeStr = input()
grades = gradeStr.split(',')

sum = 0


for i in grades:
  sum = sum + int(i)
print(sum)