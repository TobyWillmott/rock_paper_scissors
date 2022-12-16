import tkinter as tk
from game_objects import PlayerObject, HumanPlayer, ComputerPlayer, Game, RPS_OBJECTS, RPS_WIN_DICT
from functools import partial


class GameApp(tk.Tk):

    def __init__(self):
        super().__init__()

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
            "game_frame_two": GamePlayerMenu(self)
        }

        self.show_frame("game_frame_one")

        def show_frame(self, current_frame: str):
            widgets = self.winfo_children()

            for w in widgets:
                if w.winfo_class() == "Frame":
                    w.pack_froget()

            frame_to_show = self.frames[current_frame]
            frame_to_show.pack(expand=True, fill=tk.BOTH)
            frame_to_show.set_up()


class GameOptionsGui(tk.Frame):
    def __init__(self, controller: GameApp):
        super().__init__()
        self.controller = controller
        self.round_number = tk.StringVar()
        self.config(background="yellow")

        self.next_frame_button = tk.Button(self, text="Next Frame", command=self.next_frame)

        self.next_frame_button.grid(row=2, column=2, padx=10, pady=10)

    def next_frame(self):
        self.controller.show_frame("game_frame_two")


class GamePlayerMenu(tk.Frame):
    ...


class GameOver(tk.Frame):
    ...


if __name__ == "__main__":
    app = GameApp()
    app.mainloop()
