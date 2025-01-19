# This file contains the Command class.

class Command:

    #This class represents a command. A command is composed of a command word, a help string, an action and a number of parameters.

    #Attributes: command_word (str): The command word.help_string (str): The help string.action (function): The action to execute when the command is called.number_of_parameters (int): The number of parameters expected by the command.

    #Methods: __init__(self, command_word, help_string, action, number_of_parameters) : The constructor.  __str__(self) : The string representation of the command.




    # The constructor.
    def __init__(self, command_word, help_string, action, number_of_parameters):
        self.command_word = command_word
        self.help_string = help_string
        self.action = action
        self.number_of_parameters = number_of_parameters
        self.valid_directions = {"N", "S", "E", "O", "U", "D"}  # Initialisation des directions valides.
    
    # The string representation of the command.
    def __str__(self):
        return  self.command_word \
                + self.help_string
    
 # Fonction pour exécuter l'action de déplacement et vérifier si la direction est valide.
    def go(game, list_of_words, number_of_parameters):
        if number_of_parameters == 1:
            direction_input = list_of_words[1].lower()  # Convertir la direction en minuscules
            valid_directions = {
                "n": "N", "nord": "N", "nord": "N",
                "s": "S", "sud": "S", "sud": "S",
                "e": "E", "est": "E", "est": "E",
                "o": "O", "ouest": "O", "ouest": "O",
                "u": "U", "haut": "U", "haut": "U",
                "d": "D", "bas": "D", "bas": "D"
            }
            
            # Vérification de la validité de la direction
            if direction_input not in valid_directions:
                print(f"\nDirection '{list_of_words[1]}' non reconnue.\n")
                return False
            
            direction = valid_directions[direction_input]
            
            # Vérifier que la direction est valide dans les sorties de la pièce
            if direction not in game.player.current_room.exits:
                print(f"\nIl n'y a pas de sortie dans cette direction.\n")
                return False
            
            # Déplacer le joueur
            if game.player.move(direction):
                print(f"\nDirection '{direction}' utilisée. Vous vous déplacez avec succès.")
            else:
                print(f"\nLe déplacement dans la direction '{direction}' a échoué.")
        else:
            print("\nCommande invalide. Entrez 'go <direction>' pour vous déplacer.")
