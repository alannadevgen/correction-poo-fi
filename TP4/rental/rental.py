from customer import Customer
from service import Service
from vehicle import Vehicle


class Rental:
    """
    Cette classe représente une location d'un véhicule par un client, incluant les services associés.
    """

    def __init__(self, vehicle: Vehicle, customer: Customer, rental_period: int):
        """
        Initialisation d'une location avec un véhicule, un client et une période de location.

        Parameters
        ----------
        vehicle : Vehicle
            Véhicule loué
        customer : Customer
            Client louant le véhicule
        rental_period : int
            Durée de la location
        """
        self.vehicle = vehicle
        self.customer = customer
        self.rental_period = rental_period
        self.services = []

    def add_service(self, service: Service):
        """
        Ajoute un service à la commande de location.

        Parameters
        ----------
        service : Service
            Service à ajouter à la location
        """
        self.services.append(service)

    def total_price(self) -> float:
        """
        Calcule le prix total de la location, en prenant en compte la durée et les services associés.

        Returns
        -------
        float
            Prix total de la location
        """
        base_price = (
            self.rental_period * 30
        )  # Supposons un tarif de base de 30€ par jour
        services_price = sum(service.price for service in self.services)
        return base_price + services_price

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant les détails de la location.

        Returns
        -------
        str
            Détails de la location
        """
        services_info = "\n  ".join(str(service) for service in self.services)
        return (
            f"Location:\nClient: {self.customer}\nVéhicule: {self.vehicle}\n"
            f"Période de location: {self.rental_period} jours\nServices: \n  {services_info}\n"
            f"Prix total: {self.total_price()}€"
        )
