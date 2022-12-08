from game_objects import PlayerObject, HumanPlayer, ComputerPlayer, Game


class Cli_interface:
    def __init__(self):
        self.game = Game()
        self.name = None

    def set_up(self):
        print("Welcome to Rock-Paper-Scissors-Lizard-Spock")
        num_players = int(input("Enter how many players you would like to add: "))
        while num_players != 1 or num_players != 2:
            num_players = int(input("Enter a number of players that is 1 or 2"))

        if num_players == 1:
            name = input("Please enter your name: ")
            self.game.add_human_player(name)
            self.game.add_computer_player()
        elif num_players == 2:
            name1 = input("Please enter your name for Player 1: ")
            name2 = input("Please enter your name for Player 2: ")
            self.game_add_human_player(name1)
            self.game_add_human_player(name2)

    def input_max_rounds(self):
        max_rounds = int(input(f"Great, Hello {self.name} how many rounds would you like to play(1,3,5): "))
        while max_rounds != 1 or max_rounds != 3 or max_rounds != 5:
            max_rounds = int(input(f"Sorry that is not one of the options please re-enter: "))
        self.game.set_max_rounds(max_rounds)

    def get_choices(self):
        for player in self.game.players:
            if player.name != "Computer":
                choice = input(f"{player.name} what move would you like to play: ")
                while choice != "Rock" or choice != "Paper" or choice != "Lizard" or choice != "Scissors" or choice != "Spock":
                    choice = input("Enter a move from (Rock, Paper, Lizard, Scissors, Spock")
                player.choose_object(choice)
            else:
                player.choose_object()

    def run_game(self):
        ...

    def run_sequences(self):
        ...

    def display_scores(self):
        ...


if __name__ == "__main__":
    cli = Cli_interface()
    cli.run_sequence()
