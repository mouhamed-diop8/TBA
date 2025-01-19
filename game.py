#MON CODE GAME.PY EST : "# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions


class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.current_room = None  # Pièce actuelle
        
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        history = Command("history", " : afficher l'historique", Actions.history, 0)
        self.commands["history"] = history
        back = Command("back", " : revenir en arriere", Actions.back, 0)
        self.commands["back"] = back
        take = Command("take", " <item> : prendre un objet", Actions.take, 1) 
        self.commands["take"] = take
        drop = Command("drop", " <item> : déposer un objet", Actions.drop, 1)  
        self.commands["drop"] = drop
        check = Command("check", " : vérifier l'inventaire du joueur", Actions.check, 0) 
        self.commands["check"] = check
        look = Command("look", " : observer l'environnement actuel", Actions.look, 0)  
        self.commands["look"] = look

        # Setup rooms

        demeure_inventeur = Room("Demeure de l’Inventeur", "Une villa en ruines avec des secrets enfouis.")
        self.rooms.append(demeure_inventeur)
        foret_ombres = Room("Forêt des Ombres", "Une forêt dense où la lumière est absorbée par les arbres.")
        self.rooms.append(foret_ombres)
        bibliotheque_engloutie = Room("Bibliothèque Engloutie", "Un temple submergé rempli de livres magiques.")
        self.rooms.append(bibliotheque_engloutie)
        volcan_eteint = Room("Volcan Éteint", "Une montagne endormie renfermant une forge abandonnée.")
        self.rooms.append(volcan_eteint)
        labyrinthe_verre = Room("Labyrinthe de Verre", "Un labyrinthe où les murs reflètent des illusions.")
        self.rooms.append(labyrinthe_verre)
        tour_etoiles = Room("Tour des Étoiles", "Une tour utilisée comme observatoire astronomique.")
        self.rooms.append(tour_etoiles)
        cimetiere_navires = Room("Cimetière des Navires", "Une baie où plusieurs épaves sont échouées.")
        self.rooms.append(cimetiere_navires)
        palais_reflets = Room("Palais des Reflets", "Une ancienne forteresse avec des salles couvertes de miroirs.")
        self.rooms.append(palais_reflets)
        sanctuaire_idees = Room("Sanctuaire des Idées", "Une salle secrète sous la Demeure de l’Inventeur.")
        self.rooms.append(sanctuaire_idees)
        forge_cachee = Room("Forge Cachée", "Une forge ancienne au cœur du volcan.")
        self.rooms.append(forge_cachee)
        plateforme_mystique = Room("Plateforme Mystique", "Une plateforme flottante au-dessus du Labyrinthe de Verre.")
        self.rooms.append(plateforme_mystique)
        niveaux_submerges = Room("Niveaux Submergés", "Les parties inondées de la Bibliothèque Engloutie.")
        self.rooms.append(niveaux_submerges)
        cales_sous_marines = Room("Cales Sous-Marines", "Les cales immergées des épaves du Cimetière des Navires.")
        self.rooms.append(cales_sous_marines)
        salle_sommet_palais = Room("Salle Sommet du Palais", "Une pièce secrète au sommet du Palais des Reflets.")
        self.rooms.append(salle_sommet_palais)

        # Create exits for rooms
        
        demeure_inventeur.exits = {"N": foret_ombres, "S": None, "E": volcan_eteint, "O": None, "U": None, "D": sanctuaire_idees}
        foret_ombres.exits = {"N": labyrinthe_verre, "S": demeure_inventeur, "E": None, "O": cimetiere_navires, "U": None, "D": None}
        bibliotheque_engloutie.exits = {"N": None, "S": tour_etoiles, "E": None, "O": None, "U": None, "D": niveaux_submerges}
        volcan_eteint.exits = {"N": labyrinthe_verre, "S": None, "E": None, "O": demeure_inventeur, "U": None, "D": forge_cachee}
        labyrinthe_verre.exits = {"N": None, "S": volcan_eteint, "E": palais_reflets, "O": None, "U": plateforme_mystique, "D": None}
        tour_etoiles.exits = {"N": None, "S": bibliotheque_engloutie, "E": None, "O": labyrinthe_verre, "U": plateforme_mystique, "D": None}
        cimetiere_navires.exits = {"N": None, "S": None, "E": foret_ombres, "O": None, "U": None, "D": cales_sous_marines}
        palais_reflets.exits = {"N": None, "S": None, "E": None, "O": labyrinthe_verre, "U": salle_sommet_palais, "D": None}

        



        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = demeure_inventeur
        self.player.history.append(self.player.current_room)

        # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]

    # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
    # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)


    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue dans {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())






        

    def move_to(self, room):
        self.current_room = room  # Déplacer le joueur dans une nouvelle pièce

    def execute_command(self, command, *args):
        if command == "look":
            self.current_room.look()  # Afficher les items dans la pièce
        elif command == "take" and args:
            self.player.take(args[0], self.current_room)  # Prendre l'item
        elif command == "drop" and args:
            self.player.drop(args[0], self.current_room)  # Reposer l'item
        elif command == "check":
            self.player.check()  # Vérifier l'inventaire du joueur


def main():
    # Create a game object and play the game
    Game().play()


if __name__ == "__main__":
    main()
  