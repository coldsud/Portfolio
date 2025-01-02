def calculate_letter_grade(mean):
    if mean >= 90:
        return 'A'
    elif 80 < mean <= 90:
        return 'B'
    elif 70 < mean <= 80:
        return 'C'
    elif 63 < mean <= 70:
        return 'D'
    else:
        return 'F'

def main():
    with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        for line in infile:
            name, *grades = line.strip().split()
            grades = [int(grade) for grade in grades]
            mean_grade = sum(grades) / len(grades)
            letter_grade = calculate_letter_grade(mean_grade)
            outfile.write(f"{name} {letter_grade}\n")

if __name__ == "__main__":
    main()