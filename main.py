# main.py
import tkinter as tk
from views.main_menu import MainMenuView

def main():
    root = tk.Tk()
    root.title("Medical Records System")
    root.geometry("400x300")

    main_menu_view = MainMenuView(root)
    main_menu_view.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
