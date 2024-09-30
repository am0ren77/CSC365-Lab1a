# Ashley Moreno
# Lab 1 Part a
# schoolsearch.py


# Function to read students.txt file and store data in list of dictionaries
def read_students(filename):
    students = []
    with open(filename, 'r') as file:
	for line in file:
	    format_parts = line.strip().split(', ')
	    if len(format_parts) != 8:
		print("Error: Incorrect file format. Exiting program.")
                return None

	    student = {
		'StLastName': parts[0],
                'StFirstName': parts[1],
                'Grade': int(parts[2]),
                'Classroom': int(parts[3]),
                'Bus': int(parts[4]),
                'GPA': float(parts[5]),
                'TLastName': parts[6],
                'TFirstName': parts[7]
	    }
	    students.append(student)

    return students


# R4. S[tudent]: <lastname>
# Function to search for a student by last name and print the required details
def find_by_last_name(students, last_name):
    result = [student for student in students if student['StLastName'] == last_name]

    if not result:
        return f"No students found with last name: {last_name}"
    else:
	return '\n'.join([
            f"{student['StLastName']}, {student['StFirstName']}, Grade: {student['Grade']}, Classroom: {student['Classroom']}, Teacher: {student['TLastName']} {student['TFirstName']}"
            for student in result
        ])



# Main loop to handle user input
def main():
    filename = "students.txt"
    students = read_students(filename)

    while True:
        command = input("Enter command: ").strip()

# R3: search commands

	if command.startswith('S '):
	   parts = command.split()
            if len(parts) == 2:
                last_name = parts[1]
                result = find_by_last_name(students, last_name)
            else:
                result = "Invalid S command."
            print(result)	   



	elif command.startswith('T '):

	elif command.startswith('B '):	

	elif command.startswith('G '):

	elif command.startswith('A '):

	elif command.startswith('I '):

	elif command.startswith('Q '):

	else:





if __name__ == "__main__":
    main()
