student_marks = [
("alice",[85,90,52]),
("Bob",[45,78,95]),
("david",[45,63,80])
]

print(student_marks)

#display student name n their avg marks

for student,marks in student_marks:
	total=sum(marks)
	average=total/len(marks)
	print(f"{student}:average marks is {average}")