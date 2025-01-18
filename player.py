# Defini le joueur

#les attributs de cette classe sont , name, current_room

# la methode de cette classe est move

#player = Player("Alice", room1) >>> print(player.name) >>>Alice


class Player():

# Define the constructor.
    def __init__(self, name,max_weight=10):
        self.name = name
        self.current_room = None
        self.used_directions = []
        self.history = []
        self.inventory = []  # Inventaire du joueur
        self.max_weight = max_weight  # Poids maximum que le joueur peut transporter
        self.current_weight = 0  # Poids total actuel des objets dans l'inventaire
    
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


        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
        return False
        
        

    def get_history (self):
        
        #Retourne une chaîne de caractères représentant l'historique des pièces visitées.
        if not self.history:
            return "Aucune pièce visitée pour le moment."
        return "Historique des pièces visitées : " + " -> ".join(room.name for room in self.history)


    def add_item_to_inventory(self, item):
        """
        Ajoute un objet à l'inventaire du joueur.
        """
        if item.name in self.inventory:
            print(f"L'objet '{item.name}' est déjà dans votre inventaire.")
        else:
            self.inventory[item.name] = item
            print(f"Vous avez ajouté '{item.name}' à votre inventaire.")

    def remove_item_from_inventory(self, item_name):
        """
        Retire un objet de l'inventaire du joueur.
        """
        if item_name in self.inventory:
            removed_item = self.inventory.pop(item_name)
            print(f"Vous avez retiré '{item_name}' de votre inventaire.")
            return removed_item
        else:
            print(f"L'objet '{item_name}' n'est pas dans votre inventaire.")
            return None

    def get_inventory(self):
        """
        Retourne une chaîne de caractères représentant le contenu de l'inventaire.
        """
        if not self.inventory:
            return "Votre inventaire est vide."
        else:
            inventory_description = "Vous disposez des items suivants :"
            for item in self.inventory.values():
                inventory_description += f"\n    - {item}"
            return inventory_description


    
    











class Beamer:
    def __init__(self):
        self.loaded_room = None  # La pièce chargée dans le beamer

    def load(self, room):
        """Charger la pièce dans le beamer."""
        self.loaded_room = room
        print(f"Vous avez chargé la pièce '{room.description}' dans le beamer.")

    def use(self, player):
        """Utiliser le beamer pour se téléporter."""
        if self.loaded_room:
            player.move_to(self.loaded_room)
            print(f"Vous avez été téléporté dans la pièce : '{self.loaded_room.description}'.")
        else:
            print("Erreur : Le beamer n'a pas encore de pièce chargée.")




class Door:
    def __init__(self, locked=True):
        self.locked = locked  # La porte est verrouillée par défaut
        self.key = None  # La clé de la porte

    def unlock(self, player):
        """Déverrouiller la porte avec la clé."""
        if self.key in player.inventory:
            self.locked = False
            print("Vous avez déverrouillé la porte avec la clé.")
        else:
            print("Erreur : Vous n'avez pas la clé pour déverrouiller la porte.")
