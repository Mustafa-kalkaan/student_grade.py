class Exam:
    def __init__(self, subject, score):
        self.subject = subject
        self.score = score

    def is_passed(self):
        return self.score >= 50


class Student:
    def __init__(self, number, full_name, year):
        self.number = number
        self.full_name = full_name
        self.year = year
        self.exams = []

    def add_exam(self, exam):
        self.exams.append(exam)

    def calculate_average(self):
        if len(self.exams) == 0:
            return 0
        total = sum(e.score for e in self.exams)
        return total / len(self.exams)

    def print_transcript(self):
        print(f"Student: {self.full_name} ({self.number}) - Year {self.year}")
        for e in self.exams:
            status = "Passed" if e.is_passed() else "Failed"
            print(f" * {e.subject}: {e.score} ({status})")
        print(f"GPA / Average: {self.calculate_average():.2f}")


# Main program
if __name__ == "__main__":
    st1 = Student("20232602", "Mustafa Kalkan", 2)

    ex1 = Exam("Object Oriented Programming", 85)
    ex2 = Exam("Data Structures", 70)
    ex3 = Exam("Operating Systems", 45)

    st1.add_exam(ex1)
    st1.add_exam(ex2)
    st1.add_exam(ex3)

    st1.print_transcript()
