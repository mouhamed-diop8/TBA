# This file contains the Command class.

class Command:
    """
    This class represents a command. A command is composed of a command word, a help string, an action and a number of parameters.

    Attributes:
        command_word (str): The command word.
        help_string (str): The help string.
        action (function): The action to execute when the command is called.
        number_of_parameters (int): The number of parameters expected by the command.

    Methods:
        __init__(self, command_word, help_string, action, number_of_parameters) : The constructor.
        __str__(self) : The string representation of the command.

    Examples:

    >>> from actions import go
    >>> command = Command("go", "Permet de se déplacer dans une direction.", go, 1)
    >>> command.command_word
    'go'
    >>> command.help_string
    'Permet de se déplacer dans une direction.'
    >>> type(command.action)
    <class 'function'>
    >>> command.number_of_parameters
    1

    """

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
    def go(self, direction):
        if direction in self.valid_directions:
            # Exécuter l'action de déplacement ici, par exemple, en appelant une méthode correspondante.
            print(f"Vous vous déplacez vers la direction : {direction}")
            # Code d'action pour le déplacement...
        else:
            print(f"Erreur : La direction '{direction}' n'est pas valide.")


