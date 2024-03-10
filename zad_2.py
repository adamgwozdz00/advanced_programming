import datetime


class Student:

    def __init__(self, name: str, marks: [int]) -> None:
        self.name = name
        self.marks = marks

    def is_passed(self):
        if not self.marks:
            return False
        return sum(self.marks) / len(self.marks) > 50


class Library:
    def __init__(
        self, city: str, street: str, zip_code: str, open_hours: str, phone: int
    ) -> None:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Library(city='{self.city}', street='{self.street}', zip_code='{self.zip_code}"
                f"', open_hours='{self.open_hours}', phone='{self.phone}')")


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: datetime.date,
        birth_date: datetime.date,
        city: str,
        street: str,
        zip_code: str,
        phone: int,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Employee(first_name='{self.first_name}', last_name='{self.last_name}', hire_date='{self.hire_date}"
                f"', birth_date='{self.birth_date}', city='{self.city}', street='{self.street}"
                f"', zip_code='{self.zip_code}', phone='{self.phone}')")


class Book:
    def __init__(
        self,
        library: Library,
        publication_date: datetime.date,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Book(library='{self.library}', publication_date='{self.publication_date}"
                f"', author_name='{self.author_name}', author_surname='{self.author_surname}"
                f"', number_of_pages={self.number_of_pages})")


class Order:
    def __init__(
        self,
        employee: Employee,
        student: Student,
        books: [Book],
        order_date: datetime.date,
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books = ", ".join([book.__str__() for book in self.books])
        return (f"Order(employee='{self.employee}', student='{self.student}"
                f"', books=[{books}], order_date='{self.order_date}')")


if __name__ == "__main__":
    libraries = [
        Library(
            city="Gliwice",
            street="Akademicka",
            zip_code="44-100",
            open_hours="9-17",
            phone=555666777,
        ),
        Library(
            city="Katowice",
            street="Bogucicka",
            zip_code="40-227",
            open_hours="9-17",
            phone=333444555,
        ),
    ]
    books = [
        Book(
            library=libraries[0],
            publication_date=datetime.date.today(),
            author_name="Jan",
            author_surname="Kowalski",
            number_of_pages=255,
        ),
        Book(
            library=libraries[1],
            publication_date=datetime.date.today(),
            author_name="Grzegorz",
            author_surname="Gaśnica",
            number_of_pages=411,
        ),
        Book(
            library=libraries[0],
            publication_date=datetime.date.today(),
            author_name="Robert",
            author_surname="Iks",
            number_of_pages=522,
        ),
        Book(
            library=libraries[1],
            publication_date=datetime.date.today(),
            author_name="Zygmunt",
            author_surname="Ha",
            number_of_pages=123,
        ),
        Book(
            library=libraries[0],
            publication_date=datetime.date.today(),
            author_name="Przemysław",
            author_surname="Jot",
            number_of_pages=333,
        ),
    ]

    students = [
        Student("Adam", [3, 4, 5]),
        Student("Weronika", [5, 5, 5]),
        Student("Katarzyna", [2, 3, 2]),
    ]
    employees = [
        Employee(
            first_name="Grzegorz",
            last_name="Gaśnica",
            zip_code="44-100",
            street="Sezamkowa",
            city="Katowice",
            phone=555888222,
            hire_date=datetime.date.fromtimestamp(1646382436),
            birth_date=datetime.date.fromtimestamp(74161636),
        ),
        Employee(
            first_name="Mariola",
            last_name="Rosz",
            zip_code="44-100",
            street="Zachlapana",
            city="Katowice",
            phone=455888232,
            hire_date=datetime.date.fromtimestamp(1665127636),
            birth_date=datetime.date.fromtimestamp(402827236),
        ),
        Employee(
            first_name="Grzegorz",
            last_name="Gaśnica",
            zip_code="44-100",
            street="Morska",
            city="Katowice",
            phone=655887222,
            hire_date=datetime.date.fromtimestamp(1644222436),
            birth_date=datetime.date.fromtimestamp(276683236),
        ),
    ]
    orders = [
        Order(
            order_date=datetime.datetime.today(),
            employee=employees[0],
            student=students[0],
            books=[books[0], books[1]],
        ),
        Order(
            order_date=datetime.datetime.today(),
            employee=employees[2],
            student=students[1],
            books=[books[2], books[4], books[3]],
        ),
    ]

    for order in orders:
        print(order)
