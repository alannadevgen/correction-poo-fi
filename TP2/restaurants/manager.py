from employee import Employee


class Manager(Employee):
    def __init__(
        self,
        name,
        surname,
        registration_number,
        department,
    ):
        super().__init__(
            name,
            surname,
            registration_number,
        )
        self.department = department

    def organize_meeting(self):
        print(
            f"{self.name} {self.surname}, "
            f"manager du département {self.department}, "
            f"organise une réunion."
        )
