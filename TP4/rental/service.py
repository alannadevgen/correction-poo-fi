class Service:
    """
    Cette classe représente un service disponible pour un véhicule.
    """

    def __init__(self, name: str, description: str, price: float):
        """
        Initialisation d'un service avec un nom, une description et un prix.

        Parameters
        ----------
        name : str
            Nom du service
        description : str
            Description du service
        price : float
            Prix du service
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant les informations du service.

        Returns
        -------
        str
            Informations du service
        """
        return f"Service: {self.name}, Description: {self.description}, Prix: {self.price}€"
