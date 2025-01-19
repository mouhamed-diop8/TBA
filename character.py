# character.py

class Character:
    def __init__(self, name, description, current_room, msgs):
        self.name = name  # Nom du personnage
        self.description = description  # Description du personnage
        self.current_room = current_room  # Lieu où se trouve le personnage
        self.msgs = msgs  # Liste des messages à afficher quand le joueur interagit avec ce personnage

    def __str__(self):
        return f"{self.name} : {self.description}"  # Représentation textuelle du personnage

    def interact(self):
        """Méthode pour interagir avec le personnage et afficher les messages."""
        if self.msgs:
            print(f"\n{self.name} vous dit : {self.msgs[0]}")
        else:
            print(f"{self.name} ne semble rien dire...")
