from employee import Employee
from waiter import Waiter
from cook import Cook
from cashier import Cashier
from manager import Manager
from restaurant import Restaurant

def main():
    # Création d'une instance de Restaurant
    restaurant = Restaurant()

    # Embauche de différents types d'employés
    waiter = Waiter(name="Alice", surname="Dupont", registration_number="W001", tables_served=5)
    cook = Cook(name="Bob", surname="Martin", registration_number="C001", specialty="Pâtisserie")
    cashier = Cashier(name="Claire", surname="Durand", registration_number="Ca001", cash_register="Caisse 1")
    manager = Manager(name="David", surname="Bernard", registration_number="M001", department="Service")

    # Ajouter les employés au restaurant
    restaurant.hire_employee(waiter)
    restaurant.hire_employee(cook)
    restaurant.hire_employee(cashier)
    restaurant.hire_employee(manager)

    # Afficher la liste des employés
    print("\n--- Liste des employés ---")
    restaurant.display_employees()

    # Les employés effectuent leurs actions spécifiques
    print("\n--- Actions des employés ---")
    waiter.serve_table()
    cook.cook()
    cashier.handle_payment()
    manager.organize_meeting()

    # Utilisation des méthodes de la classe Employee
    print("\n--- Informations et actions générales ---")
    waiter.display_info()
    waiter.swipe_card()
    cook.work()

    # Licencier un employé
    print("\n--- Licenciement d'un employé ---")
    restaurant.fire_employee("Ca001")

    # Afficher la liste des employés après le licenciement
    print("\n--- Liste des employés après licenciement ---")
    restaurant.display_employees()

if __name__ == "__main__":
    main()
