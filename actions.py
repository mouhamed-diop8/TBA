# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Obtenir la direction de la liste de mots.
        direction_input = list_of_words[1].lower()  # Convertir la direction en minuscules

        # Dictionnaire des synonymes pour les directions
        valid_directions = {
            "n": "N", "nord": "N", "nord": "N",
            "s": "S", "sud": "S", "sud": "S",
            "e": "E", "est": "E", "est": "E",
            "o": "O", "ouest": "O", "ouest": "O",
            "u": "U", "haut": "U", "haut": "U",
            "d": "D", "bas": "D", "bas": "D"
        }

        # Vérifier si la direction entrée est valide
        if direction_input in valid_directions:
            direction = valid_directions[direction_input]
            # Vérifier si la sortie existe dans la direction choisie
            if player.current_room.exits[direction]:
                player.current_room = player.current_room.exits[direction]
                game.player.used_directions.append(direction)  # Ajouter la direction à la liste des directions utilisées
                print(f"\nVous êtes maintenant dans {player.current_room.name}.")
                print(player.current_room.get_long_description())
            else:
                print(f"\nIl n'y a pas de sortie dans cette direction.")
        else:
            print(f"\nDirection '{list_of_words[1]}' non reconnue.\n")
            print(player.current_room.get_long_description())

        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

        
    # Autres méthodes...

    
    def history(game, list_of_words, number_of_parameters):
        """
        Affiche l'historique des pièces visitées par le joueur.
        """
        player = game.player
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Afficher l'historique des pièces visitées
        print(player.get_history())
        return True

    

    
    def back(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de revenir à la pièce précédente.
        """
        player = game.player
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Vérifier si l'historique contient une pièce précédente
        if len(player.history) < 2:
            print("\nImpossible de revenir en arrière : aucune pièce précédente dans l'historique.\n")
            return False

        # Retirer la pièce actuelle de l'historique et définir la pièce précédente comme pièce actuelle
        player.history.pop()  # Supprime la pièce actuelle
        player.current_room = player.history[-1]  # Définit la pièce précédente comme actuelle

        print(f"\nVous êtes retourné dans : {player.current_room.name}\n")
        return True
