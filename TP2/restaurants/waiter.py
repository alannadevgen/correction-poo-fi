from employee import Employee

class Waiter(Employee):
    def __init__(self, name, surname, registration_number, tables_served=0):
        super().__init__(name, surname, registration_number)
        self.tables_served = tables_served

    def serve_table(self):
        print(f"{self.name} {self.surname} est en train de servir une table.")
        self.tables_served += 1

    def display_info(self):
        super().display_info()
        print(f"Tables servies: {self.tables_served}")