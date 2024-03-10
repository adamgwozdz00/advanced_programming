class Student:

    def __init__(self, name: str, marks: [int]) -> None:
        self.name = name
        self.marks = marks

    def is_passed(self):
        if not self.marks:
            return False
        return sum(self.marks) / len(self.marks) > 50


if __name__ == "__main__":
    print(Student("Adam", [50, 45, 60]).is_passed())
    print(Student("Weronika", [20, 60, 10]).is_passed())
