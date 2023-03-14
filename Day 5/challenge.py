# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆



# #Write your code below this row 👇
# count = 0
# for item in student_heights:
#   count += 1


# student_total=0

# for item_value in student_heights:
#   student_total += item_value 
  

# total_avg = round(student_total / count)

# print(total_avg)




# =============================================
##High Score

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

score = 0
for max_score in student_scores:
  if max_score > score:
    score = max_score

print(f"The highest score in the class is: {score}")
