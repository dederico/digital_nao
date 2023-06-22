import tkinter as tk
from tkinter import ttk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.selected_color = "black"
        self.is_drawing = False

        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        self.create_color_buttons()
        self.create_clear_button()

    def draw(self, event):
        if self.is_drawing:
            x, y = event.x, event.y
            self.canvas.create_oval(x-2, y-2, x+2, y+2, fill=self.selected_color, outline="")

    def start_drawing(self, event):
        self.is_drawing = True

    def stop_drawing(self, event):
        self.is_drawing = False

    def select_color(self, color):
        self.selected_color = color

    def clear_canvas(self):
        self.canvas.delete("all")

    def create_color_buttons(self):
        colors = ["black", "red", "blue", "green", "yellow"]
        for color in colors:
            button = ttk.Button(self.root, text=color, width=10, command=lambda c=color: self.select_color(c))
            button.configure(style=f"ColorButton.{color}.TButton")
            button.pack(side="left", padx=5, pady=5)

    def create_clear_button(self):
        clear_button = ttk.Button(self.root, text="Clear", width=10, command=self.clear_canvas)
        clear_button.pack(side="bottom", padx=5, pady=10)

root = tk.Tk()
app = PaintApp(root)

style = ttk.Style()
style.theme_create("ColorTheme", parent="alt", settings={
    "TButton": {
        "configure": {
            "padding": 5,
            "foreground": "white"  # Cambiar el color del texto a blanco
        },
        "map": {"background": [("active", "!disabled", "background")]},
    }
})

for color in ["black", "red", "blue", "green", "yellow"]:
    style.configure(f"ColorButton.{color}.TButton", background=color)

style.theme_use("ColorTheme")

root.mainloop()
