from employee import Employee


class Cook(Employee):
    def __init__(
        self,
        name,
        surname,
        registration_number,
        specialty,
    ):
        super().__init__(
            name,
            surname,
            registration_number,
        )
        self.specialty = specialty

    def cook(self):
        print(
            f"{self.name} {self.surname}, spécialiste en {self.specialty}, est en train de cuisiner."
        )
