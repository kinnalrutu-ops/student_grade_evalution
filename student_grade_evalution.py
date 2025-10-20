print("student_grade_evaluation")
print("enter your marks:")

print("enter maths marks:")
maths = int(input())
print("enter maths marks:")
physics = int(input())
print("enter maths marks:")
chemistry = int(input())
print("enter english marks:")
english = int(input())
print("enter computer science marks:")
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





