class Restaurant:
    def __init__(self):
        self.employees = []

    def hire_employee(
        self,
        employee,
    ):
        self.employees.append(employee)
        print(f"{employee.name} {employee.surname} a été embauché(e).")

    def fire_employee(
        self,
        registration_number,
    ):
        for employee in self.employees:
            if employee.registration_number == registration_number:
                self.employees.remove(employee)
                print(f"{employee.name} {employee.surname} a été licencié(e).")
                return
        print(f"Aucun employé trouvé avec le matricule {registration_number}.")

    def display_employees(self):
        if not self.employees:
            print("Aucun employé dans le restaurant.")
        else:
            print("Liste des employés :")
            for employee in self.employees:
                employee.display_info()
