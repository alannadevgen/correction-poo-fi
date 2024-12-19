class Vehicle:
    """
    Cette classe représente un véhicule avec des attributs pour la marque, le modèle, l'année et le kilométrage.
    """

    def __init__(self, brand: str, model: str, year: int, mileage: int):
        """
        Initialisation d'un véhicule avec sa marque, modèle, année et kilométrage.

        Parameters
        ----------
        brand : str
            Marque du véhicule
        model : str
            Modèle du véhicule
        year : int
            Année du véhicule
        mileage : int
            Kilométrage du véhicule
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, km: int):
        """
        Ajoute des kilomètres au kilométrage du véhicule.

        Parameters
        ----------
        km : int
            Kilomètres parcourus
        """
        self.mileage += km

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant les informations du véhicule.

        Returns
        -------
        str
            Informations du véhicule
        """
        return (
            f"{self.brand} {self.model} ({self.year}), Kilométrage: {self.mileage} km"
        )
