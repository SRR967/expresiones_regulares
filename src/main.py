import tkinter as tk
from interfaz import InterfazUsuario

def main():
    root = tk.Tk()
    app = InterfazUsuario(root)
    root.mainloop()

if __name__ == "__main__":
    main()
