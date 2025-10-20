print("student_grade_evaluation")
print("enter your marks:")

maths = int(input())
physics = int(input())
chemistry = int(input())
english = int(input())
CS= int(input())

marks = (maths + physics + chemistry + english + CS) / 5
print("average marks:", marks)

if marks >= 85:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 65:
    print("C")
elif marks >= 55:
    print("D")
else:
    print("FAIL")




