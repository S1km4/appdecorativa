import customtkinter as ctk
import app  # Importamos nuestro archivo app.py

# Paleta de colores moderna
COLOR_PRIMARY = "#1E88E5"
COLOR_SECONDARY = "#FFFFFF"
COLOR_BACKGROUND = "#F5F5F5"
COLOR_MENU_BACKGROUND = "#333333"
COLOR_BUTTON = "#4CAF50"
COLOR_BUTTON_TEXT = "#FFFFFF"

class AppGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Clientes y Pedidos")
        self.geometry("1024x768")
        self.configure(bg=COLOR_BACKGROUND)

        self.menu_frame = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color=COLOR_MENU_BACKGROUND)
        self.menu_frame.pack(side="left", fill="y")

        self.main_frame = ctk.CTkFrame(self, bg_color=COLOR_BACKGROUND)
        self.main_frame.pack(side="right", expand=True, fill="both")

        self.header_frame = ctk.CTkFrame(self, height=50, bg_color=COLOR_PRIMARY)
        self.header_frame.pack(side="top", fill="x")

        self.create_header()
        self.create_menu()

    def create_header(self):
        search_label = ctk.CTkLabel(self.header_frame, text="Buscar:", fg_color=COLOR_PRIMARY, text_color=COLOR_SECONDARY)
        search_label.pack(side="left", padx=10)
        search_entry = ctk.CTkEntry(self.header_frame, width=300)
        search_entry.pack(side="left", padx=10)
        
        # Simulación de iconos en el header
        icon_user = ctk.CTkLabel(self.header_frame, text="👤", fg_color=COLOR_PRIMARY, text_color=COLOR_SECONDARY, font=("Arial", 18))
        icon_user.pack(side="right", padx=10)
        icon_bell = ctk.CTkLabel(self.header_frame, text="🔔", fg_color=COLOR_PRIMARY, text_color=COLOR_SECONDARY, font=("Arial", 18))
        icon_bell.pack(side="right", padx=10)

    def create_menu(self):
        self.menu_items = {
            "Gestión de Clientes": {
                "Agregar Cliente": self.agregar_cliente,
                "Modificar Cliente": self.modificar_cliente,
                "Eliminar Cliente": self.eliminar_cliente,
                "Listar Todos los Clientes": self.listar_clientes,
                "Buscar Cliente por Nombre o Listar Todos": self.buscar_cliente_por_nombre_o_listar,
            },
            "Gestión de Pedidos": {
                "Agregar Pedido": self.agregar_pedido,
                "Finalizar Pedido": self.finalizar_pedido,
                "Revertir Pedido": self.revertir_pedido,
                "Eliminar Pedido": self.eliminar_pedido,
                "Consultar Pedidos de un Cliente": self.consultar_pedidos_cliente,
                "Consultar Todos los Pedidos": self.consultar_todos_los_pedidos,
                "Calcular Ganancias por Cliente": self.calcular_ganancias_por_cliente,
                "Calcular Ganancias Totales": self.calcular_ganancias_totales,
            },
            "Gestión de Productos": {
                "Agregar Producto de Venta": self.agregar_producto_venta,
                "Agregar Producto de Servicio": self.agregar_producto_servicio,
                "Modificar Producto": self.modificar_producto,
                "Eliminar Producto": self.eliminar_producto,
                "Listar Todos los Productos": self.listar_productos,
            },
            "Gestión de Inventario": {
                "Agregar Producto a Inventario": self.agregar_producto_inventario,
                "Revisar Inventario": self.revisar_inventario,
                "Modificar Producto de Inventario": self.modificar_producto_inventario,
            },
            "Gestión Decorativa": {
                "Calcular Ganancias por Cliente": self.calcular_ganancias_por_cliente,
                "Calcular Ganancias Totales": self.calcular_ganancias_totales,
                "Calcular Costos por Cliente": self.calcular_costos_por_cliente,
                "Calcular Costos Totales": self.calcular_costos_totales,
                "Mostrar Total de Ganancias y Costos": self.calcular_total_ganancias_costos,
            },
            "Configuración": {
                "Reiniciar Base de Datos": self.reiniciar_base_datos,
            },
            "Salir": {
                "Salir": self.quit,
            }
        }

        for menu, submenus in self.menu_items.items():
            btn = ctk.CTkButton(self.menu_frame, text=menu, command=lambda m=menu: self.show_submenu(m), fg_color=COLOR_BUTTON, text_color=COLOR_BUTTON_TEXT)
            btn.pack(fill="x", padx=5, pady=5)

    def show_submenu(self, menu):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        submenu_frame = ctk.CTkFrame(self.main_frame, bg_color=COLOR_BACKGROUND)
        submenu_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        for submenu, command in self.menu_items[menu].items():
            btn = ctk.CTkButton(submenu_frame, text=submenu, command=command, fg_color=COLOR_PRIMARY, text_color=COLOR_BUTTON_TEXT)
            btn.pack(fill="x", padx=5, pady=5)

    def agregar_cliente(self):
        agregar_cliente_window = ctk.CTk()
        agregar_cliente_window.title("Agregar Cliente")
        agregar_cliente_window.geometry("400x300")

        nombre_label = ctk.CTkLabel(agregar_cliente_window, text="Nombre:")
        nombre_label.pack(pady=5)
        nombre_entry = ctk.CTkEntry(agregar_cliente_window)
        nombre_entry.pack(pady=5)

        direccion_label = ctk.CTkLabel(agregar_cliente_window, text="Dirección:")
        direccion_label.pack(pady=5)
        direccion_entry = ctk.CTkEntry(agregar_cliente_window)
        direccion_entry.pack(pady=5)

        telefono_label = ctk.CTkLabel(agregar_cliente_window, text="Teléfono:")
        telefono_label.pack(pady=5)
        telefono_entry = ctk.CTkEntry(agregar_cliente_window)
        telefono_entry.pack(pady=5)

        def agregar():
            nombre = nombre_entry.get()
            direccion = direccion_entry.get()
            telefono = telefono_entry.get()
            app.agregar_cliente(nombre, direccion, telefono)
            agregar_cliente_window.destroy()

        agregar_button = ctk.CTkButton(agregar_cliente_window, text="Agregar", command=agregar, fg_color=COLOR_PRIMARY, text_color=COLOR_BUTTON_TEXT)
        agregar_button.pack(pady=20)

        agregar_cliente_window.mainloop()

    def modificar_cliente(self):
        modificar_cliente_window = ctk.CTk()
        modificar_cliente_window.title("Modificar Cliente")
        modificar_cliente_window.geometry("400x300")

        id_label = ctk.CTkLabel(modificar_cliente_window, text="ID del Cliente:")
        id_label.pack(pady=5)
        id_entry = ctk.CTkEntry(modificar_cliente_window)
        id_entry.pack(pady=5)

        nombre_label = ctk.CTkLabel(modificar_cliente_window, text="Nuevo Nombre:")
        nombre_label.pack(pady=5)
        nombre_entry = ctk.CTkEntry(modificar_cliente_window)
        nombre_entry.pack(pady=5)

        direccion_label = ctk.CTkLabel(modificar_cliente_window, text="Nueva Dirección:")
        direccion_label.pack(pady=5)
        direccion_entry = ctk.CTkEntry(modificar_cliente_window)
        direccion_entry.pack(pady=5)

        telefono_label = ctk.CTkLabel(modificar_cliente_window, text="Nuevo Teléfono:")
        telefono_label.pack(pady=5)
        telefono_entry = ctk.CTkEntry(modificar_cliente_window)
        telefono_entry.pack(pady=5)

        def modificar():
            id_cliente = id_entry.get()
            nombre = nombre_entry.get()
            direccion = direccion_entry.get()
            telefono = telefono_entry.get()
            app.modificar_cliente(id_cliente, nombre, direccion, telefono)
            modificar_cliente_window.destroy()

        modificar_button = ctk.CTkButton(modificar_cliente_window, text="Modificar", command=modificar, fg_color=COLOR_PRIMARY, text_color=COLOR_BUTTON_TEXT)
        modificar_button.pack(pady=20)

        modificar_cliente_window.mainloop()

    def eliminar_cliente(self):
        eliminar_cliente_window = ctk.CTk()
        eliminar_cliente_window.title("Eliminar Cliente")
        eliminar_cliente_window.geometry("300x200")

        id_label = ctk.CTkLabel(eliminar_cliente_window, text="ID del Cliente:")
        id_label.pack(pady=5)
        id_entry = ctk.CTkEntry(eliminar_cliente_window)
        id_entry.pack(pady=5)

        def eliminar():
            id_cliente = id_entry.get()
            app.eliminar_cliente(id_cliente)
            eliminar_cliente_window.destroy()

        eliminar_button = ctk.CTkButton(eliminar_cliente_window, text="Eliminar", command=eliminar, fg_color=COLOR_PRIMARY, text_color=COLOR_BUTTON_TEXT)
        eliminar_button.pack(pady=20)

        eliminar_cliente_window.mainloop()

    def listar_clientes(self):
        listar_clientes_window = ctk.CTk()
        listar_clientes_window.title("Listar Clientes")
        listar_clientes_window.geometry("600x400")

        clientes_text = ctk.CTkTextbox(listar_clientes_window)
        clientes_text.pack(expand=True, fill="both", padx=10, pady=10)

        clientes = app.listar_clientes()
        for cliente in clientes:
            clientes_text.insert("end", f"ID: {cliente['id']}, Nombre: {cliente['nombre']}, Dirección: {cliente['direccion']}, Teléfono: {cliente['telefono']}\n")

        listar_clientes_window.mainloop()

    def buscar_cliente_por_nombre_o_listar(self):
        buscar_cliente_window = ctk.CTk()
        buscar_cliente_window.title("Buscar Cliente")
        buscar_cliente_window.geometry("400x300")

        nombre_label = ctk.CTkLabel(buscar_cliente_window, text="Nombre del Cliente:")
        nombre_label.pack(pady=5)
        nombre_entry = ctk.CTkEntry(buscar_cliente_window)
        nombre_entry.pack(pady=5)

        def buscar():
            nombre = nombre_entry.get()
            cliente = app.buscar_cliente_por_nombre(nombre)
            if cliente:
                resultado_text = f"ID: {cliente['id']}, Nombre: {cliente['nombre']}, Dirección: {cliente['direccion']}, Teléfono: {cliente['telefono']}"
            else:
                resultado_text = "Cliente no encontrado"
            resultado_label.config(text=resultado_text)

        buscar_button = ctk.CTkButton(buscar_cliente_window, text="Buscar", command=buscar, fg_color=COLOR_PRIMARY, text_color=COLOR_BUTTON_TEXT)
        buscar_button.pack(pady=20)

        resultado_label = ctk.CTkLabel(buscar_cliente_window, text="")
        resultado_label.pack(pady=5)

        buscar_cliente_window.mainloop()

    def agregar_pedido(self):
        print("Agregar Pedido")

    def finalizar_pedido(self):
        print("Finalizar Pedido")

    def revertir_pedido(self):
        print("Revertir Pedido")

    def eliminar_pedido(self):
        print("Eliminar Pedido")

    def consultar_pedidos_cliente(self):
        print("Consultar Pedidos de un Cliente")

    def consultar_todos_los_pedidos(self):
        print("Consultar Todos los Pedidos")

    def calcular_ganancias_por_cliente(self):
        print("Calcular Ganancias por Cliente")

    def calcular_ganancias_totales(self):
        print("Calcular Ganancias Totales")

    def agregar_producto_venta(self):
        print("Agregar Producto de Venta")

    def agregar_producto_servicio(self):
        print("Agregar Producto de Servicio")

    def modificar_producto(self):
        print("Modificar Producto")

    def eliminar_producto(self):
        print("Eliminar Producto")

    def listar_productos(self):
        print("Listar Productos")

    def agregar_producto_inventario(self):
        print("Agregar Producto a Inventario")

    def revisar_inventario(self):
        print("Revisar Inventario")

    def modificar_producto_inventario(self):
        print("Modificar Producto de Inventario")

    def calcular_costos_por_cliente(self):
        print("Calcular Costos por Cliente")

    def calcular_costos_totales(self):
        print("Calcular Costos Totales")

    def calcular_total_ganancias_costos(self):
        print("Mostrar Total de Ganancias y Costos")

    def reiniciar_base_datos(self):
        print("Reiniciar Base de Datos")

if __name__ == "__main__":
    app = AppGUI()
    app.mainloop()
