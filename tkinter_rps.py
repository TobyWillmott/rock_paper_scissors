import tkinter as tk
from game_objects import PlayerObject, HumanPlayer, ComputerPlayer, Game, RPS_OBJECTS, RPS_WIN_DICT

class GameApp(tk.Tk):

    def __init__(self):
        super().__init__()


        title_game = "Rock, Paper, Scissors, Lizard, Spock Game"
        self.title = title_game

        title_tk


class GameOptionsGUi(tk.Frame):
    def __init__(self):
        super().__init__()

        self.players = tk.Label(self, text = "How many players would you like: ")

        value_out = tk.StringVar(root)
        value_out.set("1 or 2")
        values_in = [1,2]
        self.players_input = tk.OptionMenu(self, value_out, *values_in)




class PlayerMenu(tk.Frame):
    ...

class GameOver(tk.Frame):
    ...


if __name__ == "__main__":
    app = GameApp()