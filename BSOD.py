import tkinter as tk
from PIL import Image, ImageTk
import keyboard
import os

# This list defines which keys we want to "block"
PROHIBITED_KEYS = ['windows', 'alt', 'tab', 'esc', 'delete']

class BSODSimulator:
    def __init__(self, root):
        self.root = root
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True) # Keeps window on top of everything
        self.root.configure(bg='black')
        self.root.config(cursor="none")

        # Block the keys immediately
        for key in PROHIBITED_KEYS:
            keyboard.block_key(key)

        self.folder_path = "BSODS"
        self.image_files = [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path) if f.endswith('.png')]
        self.index = 0
        
        self.label = tk.Label(self.root, bg='black')
        self.label.pack(expand=True)
        self.show_image()

        self.root.bind("<Right>", self.next_img)
        self.root.bind("<Left>", self.prev_img)

        # The ONLY way out
        keyboard.add_hotkey('ctrl+alt+a+b', self.exit_prank)

    def show_image(self):
        img = Image.open(self.image_files[self.index])
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        self.tk_img = ImageTk.PhotoImage(img)
        self.label.config(image=self.tk_img)

    def next_img(self, event):
        self.index = (self.index + 1) % len(self.image_files)
        self.show_image()

    def prev_img(self, event):
        self.index = (self.index - 1) % len(self.image_files)
        self.show_image()

    def exit_prank(self):
        # IMPORTANT: Unblock everything before closing or your keyboard stays "broken"!
        for key in PROHIBITED_KEYS:
            keyboard.unblock_key(key)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BSODSimulator(root)
    root.mainloop()