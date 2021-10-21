class Header:
    def print_header(self, message):
        """Print a header above the current game section."""
        print(f"""\n
        -+---------------------------+-
        | {message.center(27, " ")} |
        -+---------------------------+-\n""")

class Player:
    """Get the player's name"""
    def __init__(self):
        self.player = ""

    def get_player(self):
        while True:
            self.player = input("Hi, what's your name? ")
            if self.player == '' or not self.player[0].isalpha():
                print("Please enter a name.")
                continue
            else:
                break
        return self.player


def option_check(options):
    """Allow quit game or validate chosen option."""
    while True:
        for key in options.keys():
            print(options[key])
        option = input("\nWhat do you do? ")
        if option.lower() == 'q' or option.lower() == 'quit':
            print("\nThank you for playing SUSHI QUEST!\n>> Leaving game.")
            exit()
        elif option not in options.keys():
            print(">> Please enter a valid option.")
            continue
        else:
            return option
