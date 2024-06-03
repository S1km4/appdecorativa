import sqlite3
import random
import string

# Conexión con la base de datos (crea una nueva si no existe)
conexion = sqlite3.connect('gestion_pedidos.db')
cursor = conexion.cursor()

# Crear tabla de clientes
cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                    codigo_cliente INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    direccion TEXT,
                    telefono TEXT
                  )''')

# Crear tabla de pedidos
cursor.execute('''CREATE TABLE IF NOT EXISTS pedidos (
                    id_pedido INTEGER PRIMARY KEY,
                    codigo_cliente INTEGER,
                    descripcion TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    producto TEXT,
                    unidades INTEGER,
                    estado TEXT NOT NULL,
                    FOREIGN KEY (codigo_cliente) REFERENCES clientes (codigo_cliente)
                  )''')

# Crear tabla de productos (actualizada)
cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                    id_producto INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    costo REAL NOT NULL,
                    valor_venta REAL NOT NULL,
                    valor_servicio REAL NOT NULL
                  )''')

# Crear tabla de inventario
cursor.execute('''CREATE TABLE IF NOT EXISTS inventario (
                    codigo TEXT PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    cantidad INTEGER NOT NULL
                  )''')

# Guardar (commit) los cambios
conexion.commit()

# Variable para rastrear el menú actual
menu_actual = "Principal"

def generar_codigo_producto():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def agregar_producto_inventario(nombre, cantidad):
    codigo = generar_codigo_producto()
    cursor.execute("INSERT INTO inventario (codigo, nombre, cantidad) VALUES (?, ?, ?)", (codigo, nombre, cantidad))
    conexion.commit()
    print(f"Producto '{nombre}' agregado al inventario con el código '{codigo}' y cantidad {cantidad}.")

def buscar_producto_por_nombre(nombre):
    cursor.execute("SELECT * FROM inventario WHERE nombre LIKE ?", ('%' + nombre + '%',))
    productos = cursor.fetchall()
    for producto in productos:
        print(producto)
    return productos

def revisar_inventario(nombre):
    productos = buscar_producto_por_nombre(nombre)
    if not productos:
        print("No se encontró ningún producto con ese nombre.")
    else:
        print("\n--- PRODUCTOS ENCONTRADOS ---")
        for producto in productos:
            print(f"Código: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[2]}")

def modificar_producto_inventario(nombre):
    productos = buscar_producto_por_nombre(nombre)
    if not productos:
        print("No se encontró ningún producto con ese nombre.")
        return

    print("\n--- PRODUCTOS ENCONTRADOS ---")
    for producto in productos:
        print(f"Código: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[2]}")

    codigo = input("Ingrese el código del producto que desea modificar: ").strip()
    cursor.execute("SELECT * FROM inventario WHERE codigo = ?", (codigo,))
    producto = cursor.fetchone()
    if not producto:
        print("Producto no encontrado.")
        return

    print(f"Información actual del producto: Código: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[2]}")

    nuevo_nombre = input("Nuevo nombre (dejar en blanco para mantener actual): ").strip()
    nueva_cantidad = input("Nueva cantidad (dejar en blanco para mantener actual): ").strip()

    if nuevo_nombre or nueva_cantidad:
        nuevos_valores = [producto[1], producto[2]]
        if nuevo_nombre:
            nuevos_valores[0] = nuevo_nombre
        if nueva_cantidad:
            nuevos_valores[1] = nueva_cantidad

        cursor.execute("UPDATE inventario SET nombre = ?, cantidad = ? WHERE codigo = ?", (nuevos_valores[0], nuevos_valores[1], codigo))
        conexion.commit()
        print("Información del producto modificada correctamente.")
    else:
        print("No se realizaron cambios en la información del producto.")

def agregar_cliente(nombre, direccion, telefono):
    cursor.execute("INSERT INTO clientes (nombre, direccion, telefono) VALUES (?, ?, ?)", (nombre, direccion, telefono))
    conexion.commit()
    print("Cliente agregado correctamente.")

def buscar_cliente_por_nombre_o_listar():
    nombre = input("Ingrese el nombre del cliente o presione Enter para listar todos los clientes: ").strip()
    if nombre:
        buscar_cliente_por_nombre(nombre)
    else:
        listar_clientes()

def modificar_cliente(nombre_cliente):
    clientes = buscar_cliente_por_nombre(nombre_cliente)
    if not clientes:
        print("No se encontró ningún cliente con ese nombre.")
        return

    print("\n--- CLIENTES ENCONTRADOS ---")
    for cliente in clientes:
        print(f"Código: {cliente[0]}, Nombre: {cliente[1]}, Dirección: {cliente[2]}, Teléfono: {cliente[3]}")

    codigo_cliente = int(input("Ingrese el código del cliente que desea modificar: ").strip())
    modificar_cliente_info(codigo_cliente)

def eliminar_cliente():
    nombre_cliente = input("Ingrese el nombre del cliente a eliminar: ").strip()
    clientes = buscar_cliente_por_nombre(nombre_cliente)
    if not clientes:
        print("No se encontró ningún cliente con ese nombre.")

def modificar_cliente_info(codigo_cliente):
    cursor.execute("SELECT * FROM clientes WHERE codigo_cliente = ?", (codigo_cliente,))
    cliente = cursor.fetchone()
    if not cliente:
        print("Cliente no encontrado.")
        return

    print("Información actual del cliente:")
    print(f"Código: {cliente[0]}, Nombre: {cliente[1]}, Dirección: {cliente[2]}, Teléfono: {cliente[3]}")

    nuevo_nombre = input("Nuevo nombre (dejar en blanco para mantener actual): ").strip()
    nueva_direccion = input("Nueva dirección (dejar en blanco para mantener actual): ").strip()
    nuevo_telefono = input("Nuevo teléfono (dejar en blanco para mantener actual): ").strip()

    # Actualizar la información del cliente solo si se proporciona un nuevo valor
    if nuevo_nombre or nueva_direccion or nuevo_telefono:
        # Crear una lista para almacenar los nuevos valores actualizados
        nuevos_valores = [cliente[1], cliente[2], cliente[3]]
        # Actualizar los valores en la lista si se proporciona un nuevo valor
        if nuevo_nombre:
            nuevos_valores[0] = nuevo_nombre
        if nueva_direccion:
            nuevos_valores[1] = nueva_direccion
        if nuevo_telefono:
            nuevos_valores[2] = nuevo_telefono

        # Actualizar la información del cliente en la base de datos con los nuevos valores
        cursor.execute("UPDATE clientes SET nombre = ?, direccion = ?, telefono = ? WHERE codigo_cliente = ?", tuple(nuevos_valores + [codigo_cliente]))
        conexion.commit()
        print("Información del cliente modificada correctamente.")
    else:
        print("No se realizaron cambios en la información del cliente.")

def listar_clientes():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    if not clientes:
        print("No hay clientes registrados.")
        return []
    else:
        print("\n--- LISTA DE CLIENTES ---")
        for cliente in clientes:
            print(f"Código: {cliente[0]}, Nombre: {cliente[1]}, Dirección: {cliente[2]}, Teléfono: {cliente[3]}")
        return clientes

def buscar_cliente_por_nombre(nombre):
    cursor.execute("SELECT * FROM clientes WHERE nombre LIKE ?", ('%' + nombre + '%',))
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)
    return clientes

def agregar_pedido(codigo_cliente, descripcion, categoria, id_producto=None, unidades=1):
    if categoria == "servicio":
        print("\n--- PRODUCTOS DE SERVICIO DISPONIBLES ---")
        listar_productos(categoria="servicio")
        id_producto = int(input("ID del producto de servicio: "))
        unidades = int(input("Cantidad de unidades: "))
    cursor.execute("INSERT INTO pedidos (codigo_cliente, descripcion, categoria, producto, unidades, estado) VALUES (?, ?, ?, ?, ?, 'pendiente')", (codigo_cliente, descripcion, categoria, id_producto, unidades))
    conexion.commit()
    print("Pedido agregado correctamente.")

def finalizar_pedido(id_pedido):
    cursor.execute("UPDATE pedidos SET estado = 'entregado' WHERE id_pedido = ?", (id_pedido,))
    conexion.commit()
    print("Pedido marcado como entregado.")

def revertir_pedido(id_pedido):
    cursor.execute("UPDATE pedidos SET estado = 'pendiente' WHERE id_pedido = ?", (id_pedido,))
    conexion.commit()
    print("Pedido revertido a estado pendiente.")

def eliminar_pedido(id_pedido):
    cursor.execute("SELECT estado FROM pedidos WHERE id_pedido = ?", (id_pedido,))
    estado = cursor.fetchone()
    if estado and estado[0] == 'entregado':
        cursor.execute("DELETE FROM pedidos WHERE id_pedido = ?", (id_pedido,))
        conexion.commit()
        print("Pedido eliminado correctamente.")
    elif estado and estado[0] == 'pendiente':
        print("El pedido está en estado pendiente y no se puede eliminar.")
    else:
        print("Pedido no encontrado.")

def consultar_pedidos_cliente(codigo_cliente):
    cursor.execute('''SELECT pedidos.id_pedido, clientes.nombre, pedidos.descripcion, pedidos.categoria,
                      pedidos.producto, pedidos.unidades, pedidos.estado 
                      FROM pedidos 
                      JOIN clientes ON pedidos.codigo_cliente = clientes.codigo_cliente 
                      WHERE pedidos.codigo_cliente = ?''', (codigo_cliente,))
    pedidos = cursor.fetchall()
    for pedido in pedidos:
        print(pedido)

def consultar_todos_los_pedidos():
    cursor.execute('''SELECT pedidos.id_pedido, clientes.nombre, pedidos.descripcion, pedidos.categoria, 
                      pedidos.producto, pedidos.unidades, pedidos.estado 
                      FROM pedidos 
                      JOIN clientes ON pedidos.codigo_cliente = clientes.codigo_cliente''')
    pedidos = cursor.fetchall()
    for pedido in pedidos:
        print(pedido)

def listar_productos(categoria=None):
    if categoria:
        cursor.execute("SELECT * FROM productos WHERE categoria = ?", (categoria,))
    else:
        cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    for producto in productos:
        print(f"{producto[0]}. {producto[1]} - Categoría: {producto[2]} - Costo: {producto[3]} - Valor Venta: {producto[4]} - Valor Servicio: {producto[5]}")

def agregar_producto(nombre, categoria, costo, valor_venta, valor_servicio):
    cursor.execute("INSERT INTO productos (nombre, categoria, costo, valor_venta, valor_servicio) VALUES (?, ?, ?, ?, ?)", (nombre, categoria, costo, valor_venta, valor_servicio))
    conexion.commit()
    print(f"Producto '{nombre}' agregado a la lista de productos en la categoría '{categoria}' con costo {costo}, valor de venta {valor_venta} y valor de servicio {valor_servicio}.")

def agregar_producto_venta():
    nombre = input("Nombre de la venta: ")
    categoria = "venta"
    costo = float(input("Costo: "))
    valor_venta = float(input("Valor de venta: "))
    valor_servicio = 0  # No aplica para venta
    agregar_producto(nombre, categoria, costo, valor_venta, valor_servicio)

def agregar_producto_servicio():
    nombre = input("Nombre del servicio: ")
    categoria = "servicio"
    costo = float(input("Costo: "))
    valor_venta = 0  # No aplica para servicio
    valor_servicio = float(input("Valor del servicio: "))
    agregar_producto(nombre, categoria, costo, valor_venta, valor_servicio)

def buscar_y_modificar_producto_por_nombre():
    nombre_producto = input("Ingrese el nombre del producto a modificar: ").strip()
    productos = buscar_producto_por_nombre(nombre_producto)
    if not productos:
        print("No se encontró ningún producto con ese nombre.")
        return

    print("\n--- PRODUCTOS ENCONTRADOS ---")
    for producto in productos:
        print(f"Código: {producto[0]}, Nombre: {producto[1]}, Categoría: {producto[2]}, Costo: {producto[3]}, Valor de Venta: {producto[4]}, Valor de Servicio: {producto[5]}")

    id_producto = int(input("Ingrese el código del producto que desea modificar: ").strip())
    modificar_producto(id_producto)

def modificar_producto(id_producto):
    cursor.execute("SELECT nombre, categoria, costo, valor_venta, valor_servicio FROM productos WHERE id_producto = ?", (id_producto,))
    producto = cursor.fetchone()
    if not producto:
        print("Producto no encontrado.")
        return

    nombre_actual, categoria_actual, costo_actual, valor_venta_actual, valor_servicio_actual = producto
    print(f"Nombre actual: {nombre_actual}")
    nuevo_nombre = input("Nuevo nombre (dejar en blanco para mantener actual): ").strip()
    if nuevo_nombre:
        cursor.execute("UPDATE productos SET nombre = ? WHERE id_producto = ?", (nuevo_nombre, id_producto))
        conexion.commit()
        print("Nombre modificado correctamente.")
    
    print(f"Categoría actual: {categoria_actual}")
    nueva_categoria = input("Nueva categoría (dejar en blanco para mantener actual): ").strip()
    if nueva_categoria:
        cursor.execute("UPDATE productos SET categoria = ? WHERE id_producto = ?", (nueva_categoria, id_producto))
        conexion.commit()
        print("Categoría modificada correctamente.")

    print(f"Costo actual: {costo_actual}")
    nuevo_costo = input("Nuevo costo (dejar en blanco para mantener actual): ").strip()
    if nuevo_costo:
        cursor.execute("UPDATE productos SET costo = ? WHERE id_producto = ?", (nuevo_costo, id_producto))
        conexion.commit()
        print("Costo modificado correctamente.")
    
    if categoria_actual == "venta":
        print(f"Valor de venta actual: {valor_venta_actual}")
        nuevo_valor_venta = input("Nuevo valor de venta (dejar en blanco para mantener actual): ").strip()
        if nuevo_valor_venta:
            cursor.execute("UPDATE productos SET valor_venta = ? WHERE id_producto = ?", (nuevo_valor_venta, id_producto))
            conexion.commit()
            print("Valor de venta modificado correctamente.")
    
    if categoria_actual == "servicio":
        print(f"Valor de servicio actual: {valor_servicio_actual}")
        nuevo_valor_servicio = input("Nuevo valor de servicio (dejar en blanco para mantener actual): ").strip()
        if nuevo_valor_servicio:
            cursor.execute("UPDATE productos SET valor_servicio = ? WHERE id_producto = ?", (nuevo_valor_servicio, id_producto))
            conexion.commit()
            print("Valor de servicio modificado correctamente.")

def eliminar_producto(id_producto):
    cursor.execute("SELECT nombre FROM productos WHERE id_producto = ?", (id_producto,))
    producto = cursor.fetchone()
    if not producto:
        print("Producto no encontrado.")
        return
    nombre = producto[0]
    confirmacion = input(f"Está seguro que desea eliminar el producto '{nombre}'? Escriba 'SI' para confirmar: ")
    if confirmacion == "SI":
        cursor.execute("DELETE FROM productos WHERE id_producto = ?", (id_producto,))
        conexion.commit()
        print("Producto eliminado correctamente.")
    else:
        print("Operación cancelada.")

def calcular_ganancias_por_cliente():
    cursor.execute('''SELECT clientes.nombre, 
                             SUM(CASE 
                                 WHEN pedidos.categoria = 'venta' THEN pedidos.unidades * (productos.valor_venta - productos.costo) 
                                 WHEN pedidos.categoria = 'servicio' THEN pedidos.unidades * (productos.valor_servicio - productos.costo)
                             END) AS Ganancias
                      FROM pedidos 
                      JOIN clientes ON pedidos.codigo_cliente = clientes.codigo_cliente
                      JOIN productos ON pedidos.producto = productos.id_producto
                      WHERE pedidos.estado = 'entregado'
                      GROUP BY clientes.codigo_cliente''')
    ganancias_por_cliente = cursor.fetchall()
    print("\n--- GANANCIAS POR CLIENTE ---")
    for cliente, ganancias in ganancias_por_cliente:
        print(f"{cliente}: {ganancias}")

def calcular_ganancias_totales():
    cursor.execute('''SELECT SUM(CASE 
                                 WHEN pedidos.categoria = 'venta' THEN pedidos.unidades * (productos.valor_venta - productos.costo) 
                                 WHEN pedidos.categoria = 'servicio' THEN pedidos.unidades * (productos.valor_servicio - productos.costo)
                             END) AS Ganancias
                      FROM pedidos 
                      JOIN productos ON pedidos.producto = productos.id_producto
                      WHERE pedidos.estado = 'entregado' ''')
    ganancias_totales = cursor.fetchone()[0]
    print(f"\n--- GANANCIAS TOTALES ---\n{ganancias_totales}")

def calcular_costos_por_cliente():
    cursor.execute('''SELECT clientes.nombre, 
                             SUM(CASE 
                                 WHEN pedidos.categoria = 'venta' THEN pedidos.unidades * productos.costo 
                                 WHEN pedidos.categoria = 'servicio' THEN pedidos.unidades * productos.costo
                             END) AS Costos
                      FROM pedidos 
                      JOIN clientes ON pedidos.codigo_cliente = clientes.codigo_cliente
                      JOIN productos ON pedidos.producto = productos.id_producto
                      WHERE pedidos.estado = 'entregado'
                      GROUP BY clientes.codigo_cliente''')
    costos_por_cliente = cursor.fetchall()
    print("\n--- COSTOS POR CLIENTE ---")
    for cliente, costos in costos_por_cliente:
        print(f"{cliente}: {costos}")

def calcular_costos_totales():
    cursor.execute('''SELECT SUM(CASE 
                                 WHEN pedidos.categoria = 'venta' THEN pedidos.unidades * productos.costo 
                                 WHEN pedidos.categoria = 'servicio' THEN pedidos.unidades * productos.costo
                             END) AS Costos
                      FROM pedidos 
                      JOIN productos ON pedidos.producto = productos.id_producto
                      WHERE pedidos.estado = 'entregado' ''')
    costos_totales = cursor.fetchone()[0]
    print(f"\n--- COSTOS TOTALES ---\n{costos_totales}")

def menu_gestion_clientes():
    global menu_actual
    menu_actual = "Gestión de Clientes"
    while True:
        print("\n--- GESTIÓN DE CLIENTES ---")
        print("1. Agregar cliente")
        print("2. Modificar cliente")
        print("3. Eliminar cliente")
        print("4. Listar todos los clientes")
        print("5. Buscar cliente por nombre o listar todos los clientes")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del cliente: ").strip()
            direccion = input("Dirección: ").strip()
            telefono = input("Teléfono: ").strip()
            agregar_cliente(nombre, direccion, telefono)
        elif opcion == "2":
            nombre_cliente = input("Nombre del cliente a modificar: ").strip()
            modificar_cliente(nombre_cliente)
        elif opcion == "3":
            eliminar_cliente()
        elif opcion == "4":
            listar_clientes()
        elif opcion == "5":
            buscar_cliente_por_nombre_o_listar()
        elif opcion == "6":
            menu_actual = "Principal"
            break
        else:
            print("Opción inválida, por favor seleccione una opción válida.")

def menu_gestion_pedidos():
    global menu_actual
    menu_actual = "Gestión de Pedidos"
    while True:
        print("\n--- GESTIÓN DE PEDIDOS ---")
        print("1. Agregar pedido")
        print("2. Finalizar pedido")
        print("3. Revertir pedido")
        print("4. Eliminar pedido")
        print("5. Consultar pedidos de un cliente")
        print("6. Consultar todos los pedidos")
        print("7. Calcular ganancias por cliente")
        print("8. Calcular ganancias totales")
        print("9. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            codigo_cliente = int(input("Código del cliente: ").strip())
            descripcion = input("Descripción del pedido: ").strip()
            categoria = input("Categoría (venta/servicio): ").strip()
            agregar_pedido(codigo_cliente, descripcion, categoria)
        elif opcion == "2":
            id_pedido = int(input("ID del pedido a finalizar: ").strip())
            finalizar_pedido(id_pedido)
        elif opcion == "3":
            id_pedido = int(input("ID del pedido a revertir: ").strip())
            revertir_pedido(id_pedido)
        elif opcion == "4":
            id_pedido = int(input("ID del pedido a eliminar: ").strip())
            eliminar_pedido(id_pedido)
        elif opcion == "5":
            codigo_cliente = int(input("Código del cliente: ").strip())
            consultar_pedidos_cliente(codigo_cliente)
        elif opcion == "6":
            consultar_todos_los_pedidos()
        elif opcion == "7":
            calcular_ganancias_por_cliente()
        elif opcion == "8":
            calcular_ganancias_totales()
        elif opcion == "9":
            menu_actual = "Principal"
            break
        else:
            print("Opción inválida, por favor seleccione una opción válida.")

def menu_gestion_productos():
    global menu_actual
    menu_actual = "Gestión de Productos"
    while True:
        print("\n--- GESTIÓN DE PRODUCTOS ---")
        print("1. Agregar producto de venta")
        print("2. Agregar producto de servicio")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Listar todos los productos")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_producto_venta()
        elif opcion == "2":
            agregar_producto_servicio()
        elif opcion == "3":
            id_producto = int(input("ID del producto a modificar: ").strip())
            modificar_producto(id_producto)
        elif opcion == "4":
            id_producto = int(input("ID del producto a eliminar: ").strip())
            eliminar_producto(id_producto)
        elif opcion == "5":
            listar_productos()
        elif opcion == "6":
            menu_actual = "Principal"
            break
        else:
            print("Opción inválida, por favor seleccione una opción válida.")

def menu_gestion_decorativa():
    global menu_actual
    menu_actual = "Gestión Decorativa"
    while True:
        print("\n--- GESTIÓN DECORATIVA ---")
        print("1. Calcular ganancias por cliente")
        print("2. Calcular ganancias totales")
        print("3. Calcular costos por cliente")
        print("4. Calcular costos totales")
        print("5. Mostrar total de ganancias y costos")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            calcular_ganancias_por_cliente()
        elif opcion == "2":
            calcular_ganancias_totales()
        elif opcion == "3":
            calcular_costos_por_cliente()
        elif opcion == "4":
            calcular_costos_totales()
        elif opcion == "5":
            calcular_total_ganancias_costos()
        elif opcion == "6":
            menu_actual = "Principal"
            break
        else:
            print("Opción inválida, por favor seleccione una opción válida.")

def calcular_total_ganancias_costos():
    calcular_ganancias_totales()
    calcular_costos_totales()

def menu_gestion_inventario():
    global menu_actual
    menu_actual = "Gestión de Inventario"
    while True:
        print("\n--- GESTIÓN DE INVENTARIO ---")
        print("1. Agregar producto a inventario")
        print("2. Revisar inventario")
        print("3. Modificar producto de inventario")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()
            cantidad = int(input("Cantidad: ").strip())
            agregar_producto_inventario(nombre, cantidad)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto a revisar: ").strip()
            revisar_inventario(nombre)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a modificar: ").strip()
            modificar_producto_inventario(nombre)
        elif opcion == "4":
            menu_actual = "Principal"
            break
        else:
            print("Opción inválida, por favor seleccione una opción válida.")           

def menu_configuracion():
    global menu_actual
    menu_actual = "Configuración"
    while True:
        print("\n--- CONFIGURACIÓN ---")
        print("1. Reiniciar base de datos")
        print("2. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            confirmacion = input("¿Está seguro que desea reiniciar la base de datos? Esto eliminará todos los datos existentes. (SI/NO): ").strip()
            if confirmacion.upper() == "SI":
                reiniciar_base_de_datos()
            else:
                print("Operación cancelada.")
        elif opcion == "2":
            menu_actual = "Principal"
            break
        else:
            print("Opción inválida, por favor seleccione una opción válida.")

def reiniciar_base_de_datos():
    try:
        conexion.execute("DROP TABLE IF EXISTS clientes")
        conexion.execute("DROP TABLE IF EXISTS pedidos")
        conexion.execute("DROP TABLE IF EXISTS productos")

        cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                            codigo_cliente INTEGER PRIMARY KEY,
                            nombre TEXT NOT NULL,
                            direccion TEXT,
                            telefono TEXT
                          )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS pedidos (
                            id_pedido INTEGER PRIMARY KEY,
                            codigo_cliente INTEGER,
                            descripcion TEXT NOT NULL,
                            categoria TEXT NOT NULL,
                            producto TEXT,
                            unidades INTEGER,
                            estado TEXT NOT NULL,
                            FOREIGN KEY (codigo_cliente) REFERENCES clientes (codigo_cliente)
                          )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                            id_producto INTEGER PRIMARY KEY,
                            nombre TEXT NOT NULL,
                            categoria TEXT NOT NULL,
                            costo REAL NOT NULL,
                            valor_venta REAL NOT NULL,
                            valor_servicio REAL NOT NULL
                          )''')

        conexion.commit()
        print("Base de datos reiniciada correctamente.")
    except Exception as e:
        print("Error al reiniciar la base de datos:", e)

def menu_principal():
    global menu_actual
    menu_actual = "Principal"
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Gestión de clientes")
        print("2. Gestión de pedidos")
        print("3. Gestión de productos")
        print("4. Gestión de inventario")
        print("5. Gestión Decorativa")
        print("6. Configuración")
        print("7. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_gestion_clientes()
        elif opcion == "2":
            menu_gestion_pedidos()
        elif opcion == "3":
            menu_gestion_productos()
        elif opcion == "4":
            menu_gestion_inventario()
        elif opcion == "5":
            menu_gestion_decorativa()
        elif opcion == "6":
            menu_configuracion()
        elif opcion == "7":
            print("Saliendo del programa. Hasta luego!")
            break
        else:
            print("Opción inválida, por favor seleccione una opción válida.")   

# Agregar la función para reiniciar la base de datos al menú principal
menu_principal()

# Cerrar la conexión a la base de datos al salir del programa
conexion.close()
