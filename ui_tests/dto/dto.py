from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    firstname: str = None
    lastname: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None

    def __str__(self):
        return (
            f"{self.firstname} "
            f"{self.lastname} "
            f"{str(self.age)} "
            f"{self.email} "
            f"{str(self.salary)} "
            f"{self.department}"
        )