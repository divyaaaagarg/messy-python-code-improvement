"""Refactored student result summary with reusable functions."""

PASS_MARK = 40


def calculate_average(marks: list[int]) -> float:
    """Return the average of marks, or zero when no marks are supplied."""
    return sum(marks) / len(marks) if marks else 0.0


def validate_records(names: list[str], marks: list[int]) -> None:
    """Validate that each student has a mark between 0 and 100."""
    if len(names) != len(marks):
        raise ValueError("Each student must have exactly one mark.")
    if any(not 0 <= mark <= 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100.")


def display_results(names: list[str], marks: list[int]) -> None:
    """Print each student's result and the class summary."""
    validate_records(names, marks)
    print("STUDENT RESULTS")
    print("-" * 32)

    for name, mark in zip(names, marks):
        status = "passed" if mark >= PASS_MARK else "failed"
        print(f"{name} scored {mark} — {status}")

    total = sum(marks)
    print(f"Total: {total}")
    print(f"Average: {calculate_average(marks):.2f}")


def main() -> None:
    names = ["Aarav", "Meera", "Kabir"]
    marks = [78, 91, 67]
    display_results(names, marks)


if __name__ == "__main__":
    main()
