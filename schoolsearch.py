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

# Main loop to handle user input

def main():
    filename = "students.txt"
    students = read_students(filename)

    while True:
        command = input("Enter command: ").strip()

# R3: search commands

	if command.startswith('S '):

	elif command.startswith('T '):

	elif command.startswith('B '):	

	elif command.startswith('G '):

	elif command.startswith('A '):

	elif command.startswith('I '):

	elif command.startswith('Q '):

	else:





if __name__ == "__main__":
    main()
