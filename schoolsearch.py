# Ashley Moreno
# Lab 1 Part a
# schoolsearch.py

students = list()

# Function to read students.txt file and store student data

def read_students(filename):
    global students
    with open(filename, 'r') as file:
        for line in file:
	    data = line.strip().split(',')

	    student_info = [
		data[0],		# StLastName
		data[1],		# StFirstName
		int(data[2]),		# Grade
		int(data[3]),		# Classroom
		int(data[4]),		# Bus
		float(data[5]),		# GPA
		data[6],		# TLastName
		data[7]			# TFirstName
	    ]
	    students.append(student_info)

# R4. S[tudent]: <lastname>
# Function to search for a student by last name and print the required details
def find_by_last_name(last_name):
    results = [student for student in students if student[0] == last_name]
    if results:
        for student in results:
	    print({
                    'last_name': student[0],
                    'first_name': student[1],
                    'grade': student[2],
                    'class_room': student[3],
                    'teacher': student[7] + " " + student[6]
                })
    else:
        print("No students found with last name: " + last_name)

# Main loop to handle user input
def main():
    filename = "students.txt"
    read_students(filename)


    while True:
	command = input("Enter command: ").strip()
	
	if command.startswith('Q'):
            print("Quitting program.")
            break

	parts = command.split()
	main_command = parts[0]

	if command.startswith('S'):
	  if len(parts) > 1:
              last_name = parts[1]
              find_by_last_name(last_name)  



if __name__ == "__main__":
    main()

