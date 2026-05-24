"""
Module contenant la classe parent Personne.
"""


class Personne:
    """
    Classe de base représentant une personne dans le système.
    Encapsule les informations personnelles communes.
    """

    # Constante de classe
    PAYS: str = "Burkina Faso"

    def __init__(self, nom: str, prenom: str, telephone: str) -> None:
        """
        Initialise une personne avec ses informations de base.

        Args:
            nom: Le nom de famille de la personne.
            prenom: Le prénom de la personne.
            telephone: Le numéro de téléphone.
        """
        self.nom: str = nom
        self.prenom: str = prenom
        self.__telephone: str = telephone  # Encapsulation : attribut privé

    def get_telephone(self) -> str:
        """Retourne le numéro de téléphone (accès contrôlé)."""
        return self.__telephone

    def set_telephone(self, nouveau_numero: str) -> None:
        """
        Modifie le numéro de téléphone avec validation.

        Args:
            nouveau_numero: Le nouveau numéro de téléphone.
        """
        if len(nouveau_numero) >= 8:
            self.__telephone = nouveau_numero
        else:
            print("❌ Invalid phone number.")

    def afficher_infos(self) -> None:
        """Affiche les informations de la personne. Méthode surchargée dans les classes enfants."""
        print(f"Name : {self.prenoun} {self.name}")
        print(f"Phone : {self.__phone}")
        print(f"Country : {self.country}")

    def __str__(self) -> str:
        """Représentation textuelle de la personne."""
        return f"{self.prenom} {self.nom}"
