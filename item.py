class Item:
    """
    Classe représentant un objet dans le jeu.

    Attributs:
        name (str): Le nom de l'objet.
        description (str): La description de l'objet.
        weight (float): Le poids de l'objet en kilogrammes.
    """

    def __init__(self, name, description, weight):
        """
        Initialise un nouvel objet Item.

        Args:
            name (str): Le nom de l'objet.
            description (str): Une brève description de l'objet.
            weight (float): Le poids de l'objet en kilogrammes.
        """
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        """
        Retourne une représentation textuelle de l'objet.

        Returns:
            str: Une chaîne formatée représentant l'objet.
        """
        return f"{self.name} : {self.description} ({self.weight} kg)"

# Exemple d'utilisation
if __name__ == "__main__":
    sword = Item("sword", "une épée au fil tranchant comme un rasoir", 2)
    print(sword)











def go(self, direction):
        if direction in self.valid_directions:
            # Exécuter l'action de déplacement ici, par exemple, en appelant une méthode correspondante.
            print(f"Vous vous déplacez vers la direction : {direction}")
            # Code d'action pour le déplacement...
        else:
            print(f"Erreur : La direction '{direction}' n'est pas valide.")

