import tkinter as tk
from game_objects import Game
class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.game = create_game()

        title_string = "Rock, Paper, Scissors, Lizard, Spock Game"
        self.title(title_string)
        self.resizable(False, False)

        title_label = tk.Label(self,
                               text=title_string,
                               bg="blue", fg="white",
                               width=40,
                               font=("Arial", 20))
        title_label.pack(side=tk.TOP)

        self.frames = {
            "game_frame_one": GameOptionsGui(self),
            "game_frame_two": GamePlayerMenu(self),
            "game_frame_three": GameResultsMenu(self),
            "game_frame_four": FinishedGame(self)
        }

        self.show_frame("game_frame_one")

    def show_frame(self, current_frame: str):
        widgets = self.winfo_children()
        for w in widgets:
            if w.winfo_class() == "Frame":
                w.pack_forget()

        frame_to_show = self.frames[current_frame]
        frame_to_show.pack(expand=True, fill=tk.BOTH)
        frame_to_show.set_up()


class GameOptionsGui(tk.Frame):
    def __init__(self, controller: GameApp):
        super().__init__()
        self.controller = controller
        self.game = controller.game
        self.config(background="yellow")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.user_name_1 = tk.StringVar()
        self.num_rounds = tk.IntVar()
        title_label = tk.Label(self, text="Welcome to Rock-Paper-Scissors-Lizard-Spock")
        self.num_rounds_label = tk.Label(self, text="How many rounds would you like to add(1,3,5): ")
        self.num_rounds_value = tk.Entry(self)
        self.player_name_1 = tk.Label(self, text="Player 1 please enter your name ")
        self.player_name_1_input = tk.Entry(self)
        self.next_frame_button = tk.Button(self, text="Next Frame", command=self.next_frame)

        self.next_frame_button.grid(row=2, column=2, padx=10, pady=10)
        title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="news")
        self.player_name_1.grid(row=1, column=0, padx=10, pady=10)
        self.player_name_1_input.grid(row=1, column=1)
        self.num_rounds_label.grid(row=3, column=0, padx=10, pady=10)
        self.num_rounds_value.grid(row=3, column=1)

        self.game.add_human_player()
        self.game.add_computer_player()

    def set_up_final(self):
        self.game.set_max_rounds(int(self.num_rounds_value.get())-1)
        self.game.add_name(self.player_name_1_input.get())
    def set_up(self):
        ...
    def next_frame(self):
        self.set_up_final()
        name_index_1 = False

        round_index = False
        name_1 = self.player_name_1_input.get()
        num_rounds = int(self.num_rounds_value.get())
        if len(name_1) > 0:
            name_index_1 = True

        if num_rounds == 1 or num_rounds == 3 or num_rounds == 5:
            round_index = True
        if name_index_1 == True and round_index == True:
            self.controller.show_frame("game_frame_two")


class GamePlayerMenu(tk.Frame):
    def __init__(self, controller: GameApp):
        super().__init__()
        self.controller = controller
        self.game = controller.game
        self.player = self.game.players[0]
        self.computer = self.game.players[1]

        self.player_name_1 = tk.StringVar()
        self.player_name_2 = tk.StringVar()
        self.report_score = tk.StringVar()

        self.config(background="purple")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)

        title_label = tk.Label(self, text=f"What move would you like to play: ")
        round_number_output = tk.Label(self, textvariable=self.report_score)
        self.next_frame_button = tk.Button(self, text="Next Frame", command=self.next_frame)
        self.options_buttons = (tk.Button(self, text="Rock", command=self.rock_button),
                                tk.Button(self, text="Paper", command=self.paper_button),
                                tk.Button(self, text="Scissors", command=self.scissors_button),
                                tk.Button(self, text="Lizard", command=self.lizard_button),
                                tk.Button(self, text="Spock", command=self.spock_button))

        title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        round_number_output.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        for i, btn in enumerate(self.options_buttons):
            btn.grid(row=2, column=i, padx=10, pady=10)
        self.next_frame_button.grid(row=3, column=2, padx=10, pady=10)

    def set_up(self):
        self.player_name_1.set(self.game.players[0].name)
        self.computer.choose_object()
        self.report_score.set(self.game.report_score())

    def rock_button(self):
        self.player.choose_object("Rock")

    def paper_button(self):
        self.player.choose_object("Paper")

    def scissors_button(self):
        self.player.choose_object("Scissors")

    def lizard_button(self):
        self.player.choose_object("Lizard")

    def spock_button(self):
        self.player.choose_object("Spock")

    def next_frame(self):
        self.controller.show_frame("game_frame_three")


class GameResultsMenu(tk.Frame):
    def __init__(self, controller: GameApp):
        super().__init__()
        self.controller = controller
        self.game = controller.game

        self.report_round = tk.StringVar()


        self.config(background="blue")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        title_label = tk.Label(self, text="Results!!")
        self.report_round_label = tk.Label(self, textvariable=self.report_round)

        self.next_frame_button = tk.Button(self, text="Next Frame", command=self.next_frame)

        title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.next_frame_button.grid(row=3, column=1, padx=10, pady=10)
        self.report_round_label.grid(row=1, column=0)


    def next_frame(self):
        if self.game.is_finished():
            self.controller.show_frame("game_frame_four")
        else:
            self.game.next_round()
            self.controller.show_frame("game_frame_two")

    def set_up(self):
        self.game.find_winner()
        self.report_round.set(self.controller.game.report_round())



class FinishedGame(tk.Frame):
    def __init__(self, controller: GameApp):
        super().__init__()
        self.controller = controller
        self.game = controller.game

        self.title = tk.Label(self, text="The game has finished here are the final results: ")
        self.report_winner = tk.StringVar()
        self.report_winner_label = tk.Label(self, textvariable=self.report_winner)
        self.play_again_button = tk.Button(self, text="Play Again", command=self.play_again)

        self.title.grid(row=0, column=0)
        self.report_winner_label.grid(row=1, column=0)
        self.play_again_button.grid(row=2, column=0)
    def set_up(self):
        self.report_winner.set(self.game.report_winner())

    def play_again(self):
        self.game.reset()
        self.controller.show_frame("game_frame_one")


def create_game():
    game = Game()
    return game


if __name__ == "__main__":
    app = GameApp()
    app.mainloop()
