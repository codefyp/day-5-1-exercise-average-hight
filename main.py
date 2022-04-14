# 🚨 Don't change the code below 👇
#splits the input student_heights into a list
student_heights = input("Input a list of student heights ").split()
#then create a loop where a range from 0 to the length of student_heights which converts the heights from input strings into integers 
for n in range(0,len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#srarting point of the sum
total_height =0
#creates a loop from student_heights and count the total_height
for heigth in student_heights:
  total_height = total_height + heigth
print(total_height)

#creates a loop from student_heights to count the number of students to divede from
number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(number_of_students)

#round the number which you devide
average_height = round(total_height / number_of_students)
print(average_height)
