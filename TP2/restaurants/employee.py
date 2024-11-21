class Employee:
    def __init__(
        self,
        name,
        surname,
        registration_number,
    ):
        self.name = name
        self.surname = surname
        self.registration_number = registration_number

    def work(self):
        print(f"{self.name} {self.surname} est en train de travailler.")

    def display_info(self):
        print(
            f"Nom: {self.surname}, "
            f"Prénom: {self.name}, "
            f"Matricule: {self.registration_number}"
        )

    def swipe_card(self):
        print(f"{self.name} {self.surname} a badgé.")
