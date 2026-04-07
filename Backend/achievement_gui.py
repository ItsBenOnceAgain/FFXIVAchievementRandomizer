import api_caller
import achievement_data_structs
import tkinter as tk

class MainApp():
    achievements = []

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1280x720")
        self.root.title("FFXIV Achievement Randomizer")

        label = tk.Label(self.root, text="Hello World!", font=('Arial', 96))
        label.pack()