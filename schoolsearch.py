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
def find_by_last_name(students, last_name):
    results = [student for student in students if student[0] == last_name]
    
    if results:
        for student in results:
            print("Student Last Name: {}, First Name: {}".format(student[0], student[1]))
            print("Grade: {}, Classroom: {}".format(student[2], student[3]))
            print("Teacher: {} {}\n".format(student[6], student[7]))
    else:
        print("No student found with the last name: {}".format(last_name))

# Main loop to handle user input
def main():
    filename = "students.txt"
    read_students(filename)

    while True:
        command = input("Enter a command: ")
        
        if command.startswith("S"):
            input_student_name = input("Enter the student's last name: ").strip()
            find_by_last_name(students, input_student_name)
        
        elif command == 'q':  # Add an option to quit the loop
            print("Exiting the program.")
            break
        
        else:
            print("Invalid command. Please use 'S' or 'Q'.")


if __name__ == "__main__":
    main()
