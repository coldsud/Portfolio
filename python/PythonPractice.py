import random

class Student:
    def __init__(self, name, number):
        self.name = name  # Instance Variable for student's name
        self.courses = [0] * number  # Initialize a list of grades with 0s

    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        # Format output to match the prompt's required format
        courses_str = " ".join(map(str, self.courses))
        return f"Name: {self.name}\nScores: {courses_str}"

def main():
    # Initialize the list with specific Student objects
    lyst = [
        Student("Berry", 10),
        Student("Dawn", 10),
        Student("Gale", 10),
        Student("Chan", 10),
        Student("April", 10)
    ]

    # Shuffle and print the unsorted list of students
    random.shuffle(lyst)
    print("Unsorted list of students:")
    for student in lyst:
        print(student)


    # Sort and print the sorted list of students
    lyst.sort()
    print("Sorted list of students:")
    for student in lyst:
        print(student)
       

if __name__ == "__main__":
    main()
