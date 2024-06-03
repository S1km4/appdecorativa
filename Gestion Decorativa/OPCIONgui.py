# app.py

def agregar_cliente(nombre, direccion):
    # Lógica para agregar un cliente con el nombre y la dirección proporcionados
    pass

# Definir el resto de las funciones para las otras opciones del menú

# gui.py

import tkinter as tk
import tkinter.simpledialog as sd

class AppGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Clientes y Pedidos")
        self.geometry("800x600")

        self.menu_frame = tk.Frame(self, width=200)
        self.menu_frame.pack(side="left", fill="y")

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(side="right", expand=True, fill="both")

        self.create_menu()

    def create_menu(self):
        self.menu_items = {
            "Gestión de Clientes": {
                "Agregar Cliente": self.agregar_cliente,
                # Otros elementos del menú
            },
            # Otros menús
        }

        for menu, submenus in self.menu_items.items():
            for submenu, command in submenus.items():
                btn = tk.Button(self.menu_frame, text=submenu, command=command)
                btn.pack(fill="x")

    def agregar_cliente(self):
        nombre = sd.askstring("Agregar Cliente", "Ingrese el nombre del cliente:")
        direccion = sd.askstring("Agregar Cliente", "Ingrese la dirección del cliente:")
        if nombre and direccion:
            app.agregar_cliente(nombre, direccion)

# Resto de tu código aquí

if __name__ == "__main__":
    app = AppGUI()
    app.mainloop()
