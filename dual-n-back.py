# Need 3x3 grid in the middle
    # each square in the grid should display one of two colors
    # at each time step exactly one of the 9 will be colored and
    # when that square is colored, it will trigger a random letter to be played
# Need two buttons on the bottom

import tkinter as tk
from random import randint
from time import sleep

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Dual N Back")

        self.objects = {}

        for i in range(3):
            # window.columnconfigure(i, minsize=75)
            # window.rowconfigure(i, minsize=50)
            for j in range(3):

                frame = tk.Frame(
                                master=self.window,
                                #  height=100,
                                #  width=100,
                                relief=tk.RAISED,
                                borderwidth=1,
                                #  bg="green"
                                )
                frame.grid(row=i,column=j) # columnspan=10, rowspan=10
                # label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
                label = tk.Label(master=frame, text="         \n         ", background="green")
                label.pack()

                self.objects[(i,j)] = (frame, label)

                # frame.pack(fill=tk.X)

        self.audio_same = tk.Button(master=self.window, width=1, text="a")
        self.audio_same.grid(row=4, column=0)

        self.visual_same = tk.Button(master=self.window, width=1, text="v")
        self.visual_same.grid(row=4, column=2)

        self.update_clock()
        self.window.bind("<Key>", self.handle_keypress)

        self.window.mainloop()

    def update_clock(self):
        random_col = randint(0,2)
        random_row = randint(0,2)

        # reset?
        for _, l in self.objects.values():
            l.configure(background="green")

        lab = self.objects[(random_row, random_col)][1]
        lab.configure(background="blue")
        self.window.after(1000, self.update_clock)

    def handle_keypress(self, event):
        """Print the character associated to the key pressed"""
        print(event.char)


app=App()







# https://stackoverflow.com/questions/44909066/tkinter-how-to-set-a-background-color-to-a-cell-of-a-grid/44921885





