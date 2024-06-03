import tkinter as tk
from tkinter import Button
from tkinter import Menu
from tkinter import messagebox
from database_logic import *

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Pedidos")

        # Crear menú principal
        self.menu_principal = Menu(root)
        root.config(menu=self.menu_principal)

        # Menú Gestión de Clientes
        self.menu_gestion_clientes = Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Gestión de Clientes", menu=self.menu_gestion_clientes)
        self.menu_gestion_clientes.add_command(label="Agregar Cliente", command=self.agregar_cliente)
        self.menu_gestion_clientes.add_command(label="Modificar Cliente", command=self.modificar_cliente)
        self.menu_gestion_clientes.add_command(label="Eliminar Cliente", command=self.eliminar_cliente)
        self.menu_gestion_clientes.add_command(label="Listar Todos los Clientes", command=self.listar_clientes)
        self.menu_gestion_clientes.add_command(label="Buscar Cliente por Nombre", command=self.buscar_cliente)

        # Menú Gestión de Pedidos
        self.menu_gestion_pedidos = Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Gestión de Pedidos", menu=self.menu_gestion_pedidos)
        self.menu_gestion_pedidos.add_command(label="Agregar Pedido", command=self.agregar_pedido)
        self.menu_gestion_pedidos.add_command(label="Finalizar Pedido", command=self.finalizar_pedido)
        self.menu_gestion_pedidos.add_command(label="Revertir Pedido", command=self.revertir_pedido)
        self.menu_gestion_pedidos.add_command(label="Eliminar Pedido", command=self.eliminar_pedido)
        self.menu_gestion_pedidos.add_command(label="Consultar Pedidos de un Cliente", command=self.consultar_pedidos_cliente)
        self.menu_gestion_pedidos.add_command(label="Consultar Todos los Pedidos", command=self.consultar_todos_pedidos)
        self.menu_gestion_pedidos.add_command(label="Calcular Ganancias por Cliente", command=self.calcular_ganancias_cliente)
        self.menu_gestion_pedidos.add_command(label="Calcular Ganancias Totales", command=self.calcular_ganancias_totales)

        # Menú Gestión de Productos
        self.menu_gestion_productos = Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Gestión de Productos", menu=self.menu_gestion_productos)
        self.menu_gestion_productos.add_command(label="Agregar Producto de Venta", command=self.agregar_producto_venta)
        self.menu_gestion_productos.add_command(label="Agregar Producto de Servicio", command=self.agregar_producto_servicio)
        self.menu_gestion_productos.add_command(label="Modificar Producto", command=self.modificar_producto)
        self.menu_gestion_productos.add_command(label="Eliminar Producto", command=self.eliminar_producto)
        self.menu_gestion_productos.add_command(label="Listar Todos los Productos", command=self.listar_productos)

        # Menú Gestión de Inventario
        self.menu_gestion_inventario = Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Gestión de Inventario", menu=self.menu_gestion_inventario)
        self.menu_gestion_inventario.add_command(label="Agregar Producto a Inventario", command=self.agregar_producto_inventario)
        self.menu_gestion_inventario.add_command(label="Revisar Inventario", command=self.revisar_inventario)
        self.menu_gestion_inventario.add_command(label="Modificar Producto de Inventario", command=self.modificar_producto_inventario)

        # Menú Gestión Decorativa
        self.menu_gestion_decorativa = Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Gestión Decorativa", menu=self.menu_gestion_decorativa)
        self.menu_gestion_decorativa.add_command(label="Calcular Ganancias por Cliente", command=self.calcular_ganancias_cliente_decorativa)
        self.menu_gestion_decorativa.add_command(label="Calcular Ganancias Totales", command=self.calcular_ganancias_totales_decorativa)
        self.menu_gestion_decorativa.add_command(label="Calcular Costos por Cliente", command=self.calcular_costos_cliente)
        self.menu_gestion_decorativa.add_command(label="Calcular Costos Totales", command=self.calcular_costos_totales)
        self.menu_gestion_decorativa.add_command(label="Mostrar Total de Ganancias y Costos", command=self.mostrar_total_ganancias_costos)

        # Menú Configuración
        self.menu_configuracion = Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Configuración", menu=self.menu_configuracion)
        self.menu_configuracion.add_command(label="Reiniciar Base de Datos", command=self.reiniciar_base_datos)
        self.menu_configuracion.add_command(label="Salir", command=root.quit)

    # Funciones asociadas a las opciones del menú
    def agregar_cliente(self):
        menu_gestion_clientes.agregar_cliente()

    def modificar_cliente(self):
        menu_gestion_clientes.modificar_cliente()

    def eliminar_cliente(self):
        menu_gestion_clientes.eliminar_cliente()

    def listar_clientes(self):
        menu_gestion_clientes.listar_clientes()

    def buscar_cliente(self):
        menu_gestion_clientes.buscar_cliente()

    def agregar_pedido(self):
        menu_gestion_pedidos.agregar_pedido()

    def finalizar_pedido(self):
        menu_gestion_pedidos.finalizar_pedido()

    def revertir_pedido(self):
        menu_gestion_pedidos.revertir_pedido()

    def eliminar_pedido(self):
        menu_gestion_pedidos.eliminar_pedido()

    def consultar_pedidos_cliente(self):
        menu_gestion_pedidos.consultar_pedidos_cliente()

    def consultar_todos_pedidos(self):
        menu_gestion_pedidos.consultar_todos_pedidos()

    def calcular_ganancias_cliente(self):
        menu_gestion_pedidos.calcular_ganancias_cliente()

    def calcular_ganancias_totales(self):
        menu_gestion_pedidos.calcular_ganancias_totales()

    def agregar_producto_venta(self):
        menu_gestion_productos.agregar_producto_venta()

    def agregar_producto_servicio(self):
        menu_gestion_productos.agregar_producto_servicio()

    def modificar_producto(self):
        menu_gestion_productos.modificar_producto()

    def eliminar_producto(self):
        menu_gestion_productos.eliminar_producto()

    def listar_productos(self):
        menu_gestion_productos.listar_productos()

    def agregar_producto_inventario(self):
        menu_gestion_inventario.agregar_producto_inventario()

    def revisar_inventario(self):
        menu_gestion_inventario.revisar_inventario()

    def modificar_producto_inventario(self):
        menu_gestion_inventario.modificar_producto_inventario()

    def calcular_ganancias_cliente_decorativa(self):
        menu_gestion_decorativa.calcular_ganancias_cliente()

    def calcular_ganancias_totales_decorativa(self):
        menu_gestion_decorativa.calcular_ganancias_totales()

    def calcular_costos_cliente(self):
        menu_gestion_decorativa.calcular_costos_cliente()

    def calcular_costos_totales(self):
        menu_gestion_decorativa.calcular_costos_totales()

    def mostrar_total_ganancias_costos(self):
        menu_gestion_decorativa.mostrar_total_ganancias_costos()

    def reiniciar_base_datos(self):
        if messagebox.askokcancel("Reiniciar Base de Datos", "¿Estás seguro de que quieres reiniciar la base de datos?"):
            menu_configuracion.reiniciar_base_datos()

    def salir(self):
        if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir?"):
            self.master.destroy()

# Función principal
if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()