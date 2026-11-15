"""Analyze marks entered for a class of students."""

PASS_MARK = 50


def get_valid_student_count():
    """Ask for a positive whole number of students."""
    while True:
        raw_count = input("How many students are in the class? ").strip()
        try:
            count = int(raw_count)
        except ValueError:
            print("Invalid input: enter a whole number.")
            continue
        if count > 0:
            return count
        print("Invalid count: enter at least 1 student.")


def get_student_mark(student_name):
    """Ask repeatedly until a student's mark is a whole number from 0 to 100."""
    while True:
        raw_mark = input(f"Enter marks for {student_name} (0-100): ").strip()
        try:
            mark = int(raw_mark)
        except ValueError:
            print("Invalid input: enter a whole number.")
            continue
        if 0 <= mark <= 100:
            return mark
        print("Invalid marks: value must be between 0 and 100.")


def display_class_analysis(student_names, student_marks):
    """Calculate and display class statistics and ranked student marks."""
    class_average = sum(student_marks) / len(student_marks)
    highest_marks = max(student_marks)
    lowest_marks = min(student_marks)

    highest_students = [
        name for name, mark in zip(student_names, student_marks)
        if mark == highest_marks
    ]
    lowest_students = [
        name for name, mark in zip(student_names, student_marks)
        if mark == lowest_marks
    ]

    passing_count = sum(1 for mark in student_marks if mark >= PASS_MARK)
    failing_count = len(student_marks) - passing_count

    print("\n" + "=" * 48)
    print("               CLASS MARKS ANALYSIS")
    print("=" * 48)
    print(f"Number of students : {len(student_names)}")
    print(f"Class average      : {class_average:.2f}")
    print(f"Highest marks      : {highest_marks} ({', '.join(highest_students)})")
    print(f"Lowest marks       : {lowest_marks} ({', '.join(lowest_students)})")
    print(f"Passing students   : {passing_count}")
    print(f"Failing students   : {failing_count}")

    above_average = [
        (name, mark) for name, mark in zip(student_names, student_marks)
        if mark > class_average
    ]
    print("\nStudents above class average:")
    if above_average:
        for name, mark in above_average:
            print(f"- {name}: {mark}")
    else:
        print("- None")

    ranked_students = sorted(
        zip(student_names, student_marks),
        key=lambda student: student[1],
        reverse=True
    )
    print("\nMarks sorted from highest to lowest:")
    for name, mark in ranked_students:
        print(f"- {name}: {mark}")
    print("=" * 48)


def main():
    """Collect class names and marks, then show the class analysis."""
    print("CLASS MARKS ANALYZER")
    student_names = []
    student_marks = []

    student_count = get_valid_student_count()
    for student_number in range(1, student_count + 1):
        print(f"\nStudent {student_number}")
        while True:
            student_name = input("Enter student name: ").strip()
            if student_name:
                student_names.append(student_name.title())
                break
            print("Invalid name: the name cannot be empty.")

        student_marks.append(get_student_mark(student_names[-1]))

    display_class_analysis(student_names, student_marks)


if __name__ == "__main__":
    main()
