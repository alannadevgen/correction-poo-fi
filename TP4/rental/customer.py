class Customer:
    """
    Cette classe représente un client avec des attributs de base : nom et email.
    """

    def __init__(self, name: str, email: str):
        """
        Initialisation d'un client avec un nom et un email.

        Parameters
        ----------
        name : str
            Nom du client
        email : str
            Email du client
        """
        self.name = name
        self.email = email

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant les informations du client.

        Returns
        -------
        str
            Informations du client
        """
        return f"Client: {self.name}, Email: {self.email}"
