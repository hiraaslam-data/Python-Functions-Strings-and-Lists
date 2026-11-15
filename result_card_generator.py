"""Generate a formatted result card for one student."""

SUBJECTS = ("English", "Mathematics", "Science", "Computer", "Urdu")
MARKS_PER_SUBJECT = 100


def get_valid_marks(subject):
    """Ask repeatedly until a whole-number mark between 0 and 100 is entered."""
    while True:
        raw_marks = input(f"Enter marks for {subject} (0-100): ").strip()
        try:
            marks = int(raw_marks)
        except ValueError:
            print("Invalid input: enter a whole number.")
            continue

        if 0 <= marks <= 100:
            return marks
        print("Invalid marks: value must be between 0 and 100.")


def calculate_percentage(total, max_total):
    """Return the percentage obtained out of the maximum possible marks."""
    if max_total <= 0:
        raise ValueError("Maximum total must be greater than zero.")
    return (total / max_total) * 100


def get_grade(percentage):
    """Convert a percentage into the assessment's letter grade."""
    if percentage >= 90:
        return "A+"
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 50:
        return "D"
    return "Fail"


def format_name(name):
    """Remove surrounding whitespace and capitalize each name part."""
    return name.strip().title()


def get_student_name():
    """Ask for a non-empty student name."""
    while True:
        name = input("Enter student name: ")
        if name.strip():
            return format_name(name)
        print("Invalid name: the name cannot be empty.")


def get_roll_number():
    """Ask until the roll number contains digits only."""
    while True:
        roll_number = input("Enter roll number: ").strip()
        if roll_number.isdigit():
            return roll_number
        print("Invalid roll number: use digits only.")


def display_result_card(name, roll_number, marks):
    """Calculate the result and print the student's formatted result card."""
    total = sum(marks.values())
    max_total = len(SUBJECTS) * MARKS_PER_SUBJECT
    percentage = calculate_percentage(total, max_total)
    grade = get_grade(percentage)
    has_subject_below_40 = any(mark < 40 for mark in marks.values())
    status = "Pass" if not has_subject_below_40 and percentage >= 50 else "Fail"

    print("\n" + "=" * 42)
    print("             STUDENT RESULT CARD")
    print("=" * 42)
    print(f"Student Name : {name}")
    print(f"Roll Number  : {roll_number}")
    print("-" * 42)
    print(f"{'Subject':<20}{'Marks':>10}")
    print("-" * 42)
    for subject, mark in marks.items():
        print(f"{subject:<20}{mark:>10}")
    print("-" * 42)
    print(f"{'Total Marks':<20}{total:>10} / {max_total}")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Letter Grade : {grade}")
    print(f"Final Status : {status}")
    if has_subject_below_40:
        print("Note         : At least one subject mark is below 40.")
    print("=" * 42)


def main():
    """Collect student details and generate the result card."""
    print("STUDENT RESULT CARD GENERATOR")
    name = get_student_name()
    roll_number = get_roll_number()
    marks = {subject: get_valid_marks(subject) for subject in SUBJECTS}
    display_result_card(name, roll_number, marks)


if __name__ == "__main__":
    main()
