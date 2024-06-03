import tkinter as tk
from gui import GUI

def main():
    # Crear la ventana principal de la aplicación
    root = tk.Tk()
    root.title("Sistema de Gestión")

    # Crear una instancia de la interfaz gráfica
    app = GUI(root)

    # Ejecutar el bucle principal de la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
