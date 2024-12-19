from customer import Customer
from rental import Rental
from service import Service
from vehicle import Vehicle


def main():
    # Création du client
    customer = Customer("Jacqueline Dupont", "jacqueline.dupont@mail.com")

    # Création du véhicule
    vehicle = Vehicle("Renault", "Clio", 2018, 25000)

    # Création des services
    service1 = Service("Entretien moteur", "Service d'entretien du moteur", 150)
    service2 = Service(
        "Assurance véhicule", "Assurance pour la durée de la location", 50
    )

    # Création de la location
    rental = Rental(vehicle, customer, 7)

    # Ajout des services à la location
    rental.add_service(service1)
    rental.add_service(service2)

    # Affichage du prix total
    print(f"Prix total de la location: {rental.total_price()}€")

    # Affichage des détails de la commande
    print("\nDétails de la commande:")
    print(rental)


if __name__ == "__main__":
    main()
