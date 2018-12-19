print('-'*60)
print('Narrative Bot: ')
name = input('Student Name: ')
grade = input('Grade: ')
grade = int(grade)
if grade < 65:
	print('Narrative: ' + name +', your final grade in AP Computer Science is ' + str(grade) + '%. This is largely a result of missing projects and homework assignments. Unfortunately, because this grade is less than a 65, you will have to complete an MBA assignment next semester. ')
print('-'*60)
if grade > 65:
	print('Narrative: ' + name + ', your final grade in AP Computer Science is ' + str(grade) + '%. You have excelled in all components of the class! I wish you continued sucess in the next semester of AP Computer Science!')
print('-'*60)