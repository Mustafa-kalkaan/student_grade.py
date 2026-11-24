# Student Exam & Transcript System - Mapping Design to Code

This repository contains a Python Object-Oriented Programming (OOP) implementation mapped from a **Student - Exam UML Class Diagram**.

## UML Class Diagram

```text
+-----------------------------------+          +-----------------------------------+
|              Student              |          |               Exam                |
+-----------------------------------+          +-----------------------------------+
| - number: String                  |          | - subject: String                 |
| - full_name: String               |          | - score: int                      |
| - year: int                       |  1    *  |                                   |
| - exams: List                     |----------|                                   |
+-----------------------------------+          +-----------------------------------+
| + add_exam(exam)                  |          | + is_passed(): bool               |
| + calculate_average(): float      |          |                                   |
| + print_transcript()              |          |                                   |
+-----------------------------------+          +-----------------------------------+
```

## Files
- `student_grade.py`: Contains the `Student` and `Exam` classes along with an example transcript calculation.
