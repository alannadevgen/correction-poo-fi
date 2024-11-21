from employee import Employee


class Cashier(Employee):
    def __init__(
        self,
        name,
        surname,
        registration_number,
        cash_register,
    ):
        super().__init__(
            name,
            surname,
            registration_number,
        )
        self.cash_register = cash_register

    def handle_payment(self):
        print(
            f"{self.name} {self.surname} est en train de gérer un paiement "
            f"à la caisse {self.cash_register}."
        )
