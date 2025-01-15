# class Actions:
    
    def go(game, list_of_words, number_of_parameters):
        """
     Déplace le joueur dans la direction spécifiée par le paramètre.
    Le paramètre doit être une direction cardinale (N, E, S, O).

        Args:
            game (Game): L'objet jeu.
            list_of_words (list): La liste des mots dans la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.
        """
        
        player = game.player
        l = len(list_of_words)

        # Si le nombre de paramètres est incorrect, afficher un message d'erreur et retourner False.
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
