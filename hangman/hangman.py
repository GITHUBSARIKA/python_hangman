import sys
import random
import tkinter as tk

class Hangman(tk.Tk):
    dict_word_list = None

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.entered_text = tk.StringVar()
        self.label = None
        self.random_word = None
        self.initialize()

    def initialize(self):
        # Open and read large words file once if necessary
        self.read_words_file()

        self.label = tk.Label(self, bg='light grey', textvariable=self.entered_text)
        self.label.place(relwidth=1, relheight=1)

        self.random_word = self.get_random_word()
        print(self.random_word)

    def key_pressed(self, event):
        print("pressed " + str(event.char))
        self.entered_text.set(self.entered_text.get() + str(event.char))

    def read_words_file(self):
        # Only need to be read once
        if Hangman.dict_word_list is None:
            file_handle = None
            word_file = "dictionary.txt"

            # 'with' statement will automatically close the file afterwards
            with open(word_file) as file_handle:
                # Populate list with all words read from file
                Hangman.dict_word_list = file_handle.read().splitlines()

                # Sort the list so it'll be easier to find plurals
                Hangman.dict_word_list.sort()

    def get_random_word(self):
        if Hangman.dict_word_list is None or len(Hangman.dict_word_list) == 0:
            print("ERROR: Dictionary text file not loaded")
            return

        random_word = random.choice(Hangman.dict_word_list)

        return random_word

if __name__ == '__main__':
    # make a new Hangman game
    game = Hangman(None)

    # set your game title
    game.title("Hangman")

    # Add a key listener to your game
    game.bind("<Key>", game.key_pressed)

    # run your game's mainloop()
    game.mainloop()
