# Defintion de la classe Room

# cette classe defini l'ensemble des les lieux , les connections entre eux 

# les attributs de cette classe sont name, description, exits

#les methodes sont get_exist, get_exist_string, get_long_description

# room1 = Room("Forêt enchantée", "Une clairière mystérieuse illuminée par des lucioles.", {"nord": None}) >>> print(room1.name) >>>Forêt enchantée

class Room:

    # Define the constructor. 
    def __init__(self, name, description,items=None, dark=False):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.items = items if items else [] 
        self.dark = dark 
        self.characters = []
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
  

    def get_long_description(self):
        items_description = ', '.join([str(item) for item in self.items]) if self.items else "Aucun objet"
        characters_description = ', '.join([str(character) for character in self.characters]) if self.characters else "Aucun personnage"
        return f"{self.description}\nVous voyez ici :\nObjets : {items_description}\nPersonnages : {characters_description}"




    def add_item_to_inventory(self, item):
        """
        Ajoute un objet à l'inventaire de la pièce.
        """
        if item.name in self.inventory:
            print(f"L'objet '{item.name}' est déjà dans cette pièce.")
        else:
            self.inventory[item.name] = item
            print(f"'{item.name}' a été ajouté à la pièce '{self.name}'.")

    def remove_item_from_inventory(self, item_name):
        """
        Retire un objet de l'inventaire de la pièce.
        """
        if item_name in self.inventory:
            removed_item = self.inventory.pop(item_name)
            print(f"'{item_name}' a été retiré de la pièce '{self.name}'.")
            return removed_item
        else:
            print(f"L'objet '{item_name}' n'est pas dans cette pièce.")
            return None

    def get_inventory(self):
        """
        Retourne une chaîne de caractères représentant le contenu de l'inventaire de la pièce.
        """
        if not self.inventory:
            return "Il n'y a rien ici."
        else:
            inventory_description = "La pièce contient :"
            for item in self.inventory.values():
                inventory_description += f"\n    - {item}"
            return inventory_description

    
  
    