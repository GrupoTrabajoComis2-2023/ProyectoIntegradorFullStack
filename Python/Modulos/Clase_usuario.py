from python_fullstack import *

# Clase para la gestión de usuarios
class Usuario:
    def __init__(self, db_name="intento_menu"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def registrarse(self, nombre_usuario, contraseña):
        try:
            # Verificar si el usuario ya existe
            self.cursor.execute("SELECT id_usuario FROM Usuario WHERE nombre_usuario = ?", (nombre_usuario,))
            usuario_existente = self.cursor.fetchone()

            if usuario_existente:
                return "El nombre de usuario ya está en uso."

            # Insertar nuevo usuario
            self.cursor.execute("INSERT INTO Usuario (nombre_usuario, contraseña) VALUES (?, ?)",
                                (nombre_usuario, contraseña))
            self.conn.commit()
            return "Registro exitoso."

        except Exception as e:
            return str(e)

    def login(self, nombre_usuario, contraseña):
        try:
            # Verificar las credenciales de inicio de sesión
            self.cursor.execute("SELECT id_usuario FROM Usuario WHERE nombre_usuario = ? AND contraseña = ?",
                                (nombre_usuario, contraseña))
            usuario = self.cursor.fetchone()

            if usuario:
                return "Inicio de sesión exitoso."
            else:
                return "Credenciales incorrectas."

        except Exception as e:
            return str(e)

    def verificar_nombre_usuario_unico(self, nombre_usuario):
        try:
            # Verificar si el usuario ya existe
            self.cursor.execute("SELECT id_usuario FROM Usuario WHERE nombre_usuario = ?", (nombre_usuario,))
            usuario_existente = self.cursor.fetchone()

            return usuario_existente is None  # Devuelve True si el nombre de usuario es único, de lo contrario, False

        except Exception as e:
            return str(e)
        
    def ver_productos(self):
        try:
            self.cursor.execute("SELECT id_producto, nombre, descripcion, precio, stock FROM Producto")
            productos = self.cursor.fetchall()
            return productos
        except Exception as e:
            return str(e)


    def comprar_producto(self, id_producto, cantidad):
        try:
            # Verificar si el producto existe y tiene suficiente stock
            self.cursor.execute("SELECT nombre, stock, precio FROM Producto WHERE id_producto = ?", (id_producto,))
            producto = self.cursor.fetchone()

            if not producto:
                return "El producto no existe."

            nombre_producto, stock_producto, precio_producto = producto

            if stock_producto < cantidad:
                return "No hay suficiente stock disponible para este producto."

            # Calcular el precio total de la compra
            precio_total = precio_producto * cantidad

            return f"Compra de {cantidad} {nombre_producto}(s) realizada con éxito. Precio total: ${precio_total}"
        except Exception as e:
            return str(e)


    def ver_carrito(self):
        try:
            # Consultar los productos en el carrito del usuario
            self.cursor.execute("SELECT PEC.id_carrito_producto, P.nombre, PEC.cantidad FROM ProductoEnCarrito AS PEC "
                                "INNER JOIN Producto AS P ON PEC.id_producto = P.id_producto "
                                "INNER JOIN Carrito AS C ON PEC.id_carrito = C.id_carrito "
                                "WHERE C.id_cliente = ?", (self.id_usuario,))
            carrito = self.cursor.fetchall()
            return carrito
        except Exception as e:
            return str(e)

    def cerrar_conexion(self):
        self.conn.close()