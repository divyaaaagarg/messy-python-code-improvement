# Original version: intentionally repetitive for a refactoring demonstration.
names = ["Aarav", "Meera", "Kabir"]
marks = [78, 91, 67]

print("STUDENT RESULTS")
print("---------------")
print(names[0], "scored", marks[0])
print(names[1], "scored", marks[1])
print(names[2], "scored", marks[2])
total = marks[0] + marks[1] + marks[2]
average = total / 3
print("Total:", total)
print("Average:", average)
if marks[0] >= 40:
    print(names[0], "passed")
else:
    print(names[0], "failed")
if marks[1] >= 40:
    print(names[1], "passed")
else:
    print(names[1], "failed")
if marks[2] >= 40:
    print(names[2], "passed")
else:
    print(names[2], "failed")
