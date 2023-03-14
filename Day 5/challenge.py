# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆



#Write your code below this row 👇
count = 0
for item in student_heights:
  count += 1


student_total=0

for item_value in student_heights:
  student_total += item_value 
  

total_avg = round(student_total / count)

print(total_avg)