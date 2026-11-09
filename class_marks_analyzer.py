"""
Task 2: Class Marks Analyzer
Topics: Lists (append, len, sum, max, min, sorted) and Loops
"""

PASS_MARK = 50


def get_valid_count():
    """Ask for the number of students until a whole number >= 1 is given."""
    while True:
        try:
            count = int(input("How many students are in the class? ").strip())
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if count >= 1:
            return count
        print("There must be at least 1 student.")


def get_valid_mark(student_name):
    """Ask for one student's mark until it is a number from 0 to 100."""
    while True:
        text = input(f"  Marks of {student_name} (0-100): ").strip()
        try:
            mark = float(text)
        except ValueError:
            print("  Invalid input. Please enter a number.")
            continue
        if 0 <= mark <= 100:
            return mark
        print("  Marks must be between 0 and 100.")


def get_valid_student_name(number):
    """Ask for a non-empty student name."""
    while True:
        name = input(f"Name of student {number}: ").strip().title()
        if name:
            return name
        print("Name cannot be empty.")


def find_students_with_mark(student_names, student_marks, target):
    """Return the list of students whose mark equals target."""
    found = []
    for i in range(len(student_marks)):
        if student_marks[i] == target:
            found.append(student_names[i])
    return found


def count_pass_fail(student_marks):
    """Return (passing, failing) counts using the pass mark of 50."""
    passing = 0
    failing = 0
    for mark in student_marks:
        if mark >= PASS_MARK:
            passing += 1
        else:
            failing += 1
    return passing, failing


def main():
    print("=" * 50)
    print("              CLASS MARKS ANALYZER")
    print("=" * 50)

    student_names = []
    student_marks = []

    total_students = get_valid_count()

    # Collect data with .append()
    for i in range(1, total_students + 1):
        print(f"\n--- Student {i} of {total_students} ---")
        name = get_valid_student_name(i)
        mark = get_valid_mark(name)
        student_names.append(name)
        student_marks.append(mark)

    # Statistics using len(), sum(), max(), min()
    class_average = sum(student_marks) / len(student_marks)
    highest = max(student_marks)
    lowest = min(student_marks)
    top_students = find_students_with_mark(student_names, student_marks, highest)
    bottom_students = find_students_with_mark(student_names, student_marks, lowest)
    passing, failing = count_pass_fail(student_marks)

    print("\n" + "=" * 50)
    print("                 ANALYSIS REPORT")
    print("=" * 50)
    print(f"Total students  : {len(student_names)}")
    print(f"Class average   : {class_average:.2f}")
    print(f"Highest marks   : {highest:.2f} -> {', '.join(top_students)}")
    print(f"Lowest marks    : {lowest:.2f} -> {', '.join(bottom_students)}")
    print(f"Passing (>= {PASS_MARK}) : {passing}")
    print(f"Failing (< {PASS_MARK})  : {failing}")

    # Students above the class average
    print("\nStudents above class average:")
    above_found = False
    for i in range(len(student_marks)):
        if student_marks[i] > class_average:
            print(f"  - {student_names[i]}: {student_marks[i]:.2f}")
            above_found = True
    if not above_found:
        print("  None")

    # Marks sorted highest to lowest (names stay paired with their marks)
    print("\nMarks (highest to lowest):")
    ranking = sorted(zip(student_marks, student_names), reverse=True)
    for position, (mark, name) in enumerate(ranking, start=1):
        print(f"  {position}. {name}: {mark:.2f}")
    print("=" * 50)


if __name__ == "__main__":
    main()