# Defini le joueur

#les attributs de cette classe sont , name, current_room

# la methode de cette classe est move

#player = Player("Alice", room1) >>> print(player.name) >>>Alice


class Player():

# Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.used_directions = []
        self.history = []
    
    # Define the move method.
    def move(self, direction):
    
    # Normaliser la direction (e.g., "NORD" -> "N")
        normalized_direction = direction.upper()
        
        if normalized_direction in self.current_room.exits:
            next_room = self.current_room.exits[normalized_direction]
            self.history.append(self.current_room)  # Ajouter la pièce actuelle à l'historique
            self.current_room = next_room  # Mettre à jour la pièce actuelle
            self.used_directions.append(normalized_direction)  # Enregistrer la direction utilisée
            print(f"Déplacement vers {self.current_room.name}")

        def get_history(self):
        
        #Retourne une chaîne de caractères représentant l'historique des pièces visitées.
            if not self.history:
                return "Aucune pièce visitée pour le moment."
            return "Historique des pièces visitées : " + " -> ".join(room.name for room in self.history)



        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True
