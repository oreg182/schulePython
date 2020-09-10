import time
import tkinter
import json


def load_data_from_file(file):
    with open(file) as f:
        data = json.load(f)
    return data


class Gui(tkinter.Tk):

    def __init__(self, data: list):
        super().__init__()
        self.state("zoomed")
        self.c = tkinter.Frame()
        self.c.pack(fill=tkinter.BOTH, expand=True)
        self.c.configure(bg="white")
        self.b = tkinter.Button(self.c, text="Start", command=lambda d=data: self.send_data(d))
        self.b.pack()
        self.mainloop()

    def send_data(self, data: list):
        for i in data:
            time.sleep(1)
            if i:
                print("b")
                self.switch_color("black")
                self.update()
            else:
                print("w")
                self.switch_color("white")
                self.update()

    def switch_color(self, color):  # "black" or "white"
        self.c.configure(bg=color)


if __name__ == '__main__':
    Gui([0, 1, 1, 0, 1])
