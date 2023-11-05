import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect("FULLSTACK_DB")
cursor = conn.cursor()

# Creación de las tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS Registro (
    id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    apellido TEXT,
    email TEXT,
    contraseña TEXT
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Administrador (
    id_administrador INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_admin TEXT,
    contraseña_admin TEXT
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Producto (
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    descripcion TEXT,
    precio REAL,
    stock INTEGER
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_usuario TEXT,
    contraseña TEXT,
    id_cliente INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES Cliente (id_cliente)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Cliente (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    telefono TEXT,
    direccion TEXT,
    pais TEXT,
    codigo_postal TEXT
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Carrito (
    id_carrito INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES Cliente (id_cliente)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ProductoEnCarrito (
    id_carrito_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    id_carrito INTEGER,
    id_producto INTEGER,
    cantidad INTEGER,
    FOREIGN KEY (id_carrito) REFERENCES Carrito (id_carrito),
    FOREIGN KEY (id_producto) REFERENCES Producto (id_producto)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Compra (
    id_compra INTEGER PRIMARY KEY AUTOINCREMENT,
    num_factura INTEGER,
    precio_total REAL,
    fecha_compra DATE,
    productos TEXT,
    medio_pago TEXT,
    id_carrito INTEGER,
    FOREIGN KEY (id_carrito) REFERENCES Carrito (id_carrito)
)""")

# Commit de la transacción y cierre de la conexión
conn.commit()
conn.close()

# Clase para la gestión de usuarios
class Usuario:
    def __init__(self, db_name="FULLSTACK_DB"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def registrarse(self, nombre_usuario, contraseña, email):
        try:
            # Verificar si el usuario ya existe
            self.cursor.execute("SELECT id_usuario FROM Usuario WHERE nombre_usuario = ?", (nombre_usuario,))
            usuario_existente = self.cursor.fetchone()

            if usuario_existente:
                return "El nombre de usuario ya está en uso."

            # Insertar nuevo usuario
            self.cursor.execute("INSERT INTO Usuario (nombre_usuario, contraseña, email) VALUES (?, ?, ?)",
                                (nombre_usuario, contraseña, email))
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

    def editar_perfil(self, id_usuario, nuevo_nombre, nueva_contraseña, nuevo_email):
        try:
            # Actualizar los datos del usuario
            self.cursor.execute("UPDATE Usuario SET nombre_usuario = ?, contraseña = ?, email = ? WHERE id_usuario = ?",
                                (nuevo_nombre, nueva_contraseña, nuevo_email, id_usuario))
            self.conn.commit()
            return "Perfil actualizado correctamente."

        except Exception as e:
            return str(e)

    def contraseña_olvidada(self, nombre_usuario, nueva_contraseña):
        try:
            # Actualizar la contraseña del usuario
            self.cursor.execute("UPDATE Usuario SET contraseña = ? WHERE nombre_usuario = ?",
                                (nueva_contraseña, nombre_usuario))
            self.conn.commit()
            return "Contraseña actualizada correctamente."

        except Exception as e:
            return str(e)

    def cerrar_conexion(self):
        self.conn.close()

# Clase para la gestión de administradores
class Administrador(Usuario):
    def __init__(self, db_name="FULLSTACK_DB"):
        super().__init__(db_name)

    def ver_productos(self):
        try:
            # Consultar la lista de productos
            self.cursor.execute("SELECT * FROM Producto")
            productos = self.cursor.fetchall()
            return productos

        except Exception as e:
            return str(e)

    def agregar_producto(self, nombre, descripcion, precio, stock):
        try:
            # Insertar un nuevo producto
            self.cursor.execute("INSERT INTO Producto (nombre, descripcion, precio, stock) VALUES (?, ?, ?, ?)",
                                (nombre, descripcion, precio, stock))
            self.conn.commit()
            return "Producto agregado correctamente."

        except Exception as e:
            return str(e)

    def eliminar_producto(self, id_producto):
        try:
            # Eliminar un producto por su ID
            self.cursor.execute("DELETE FROM Producto WHERE id_producto = ?", (id_producto,))
            self.conn.commit()
            return "Producto eliminado correctamente."

        except Exception as e:
            return str(e)

    def modificar_producto(self, id_producto, nuevo_nombre, nueva_descripcion, nuevo_precio, nuevo_stock):
        try:
            # Modificar los datos de un producto
            self.cursor.execute("UPDATE Producto SET nombre = ?, descripcion = ?, precio = ?, stock = ? WHERE id_producto = ?",
                                (nuevo_nombre, nueva_descripcion, nuevo_precio, nuevo_stock, id_producto))
            self.conn.commit()
            return "Producto modificado correctamente."

        except Exception as e:
            return str(e)

# Clase para la gestión de clientes
class Cliente(Usuario):
    def __init__(self, db_name="FULLSTACK_DB"):
        super().__init__(db_name)

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

            # Registrar la compra en la tabla ProductoEnCarrito
            self.cursor.execute("INSERT INTO ProductoEnCarrito (id_carrito, id_producto, cantidad) "
                                "SELECT C.id_carrito, ?, ? FROM Carrito AS C WHERE C.id_cliente = ?",
                                (id_producto, cantidad, self.id_usuario))
            self.conn.commit()

            # Actualizar el stock del producto
            self.cursor.execute("UPDATE Producto SET stock = stock - ? WHERE id_producto = ?", (cantidad, id_producto))
            self.conn.commit()

            return f"Compra de {cantidad} {nombre_producto}(s) realizada con éxito. Precio total: ${precio_total}"

        except Exception as e:
            return str(e)

    def ver_producto(self, id_producto):
        try:
            # Consultar los detalles de un producto por su ID
            self.cursor.execute("SELECT * FROM Producto WHERE id_producto = ?", (id_producto,))
            producto = self.cursor.fetchone()
            return producto

        except Exception as e:
            return str(e)

    def añadir_al_carrito(self, id_producto, cantidad):
        try:
            # Verificar si el producto existe y tiene suficiente stock
            self.cursor.execute("SELECT nombre, stock, precio FROM Producto WHERE id_producto = ?", (id_producto,))
            producto = self.cursor.fetchone()

            if not producto:
                return "El producto no existe."

            nombre_producto, stock_producto, precio_producto = producto

            if stock_producto < cantidad:
                return "No hay suficiente stock disponible para este producto."

            # Verificar si el cliente tiene un carrito activo
            self.cursor.execute("SELECT id_carrito FROM Carrito WHERE id_cliente = ? AND id_producto IS NULL", (self.id_usuario,))
            carrito = self.cursor.fetchone()

            if carrito:
                id_carrito = carrito[0]
            else:
                # Crear un nuevo carrito
                self.cursor.execute("INSERT INTO Carrito (id_cliente) VALUES (?)", (self.id_usuario,))
                self.conn.commit()
                id_carrito = self.cursor.lastrowid

            # Verificar si el producto ya está en el carrito y actualizar la cantidad
            self.cursor.execute("SELECT id_carrito_producto, cantidad FROM ProductoEnCarrito WHERE id_carrito = ? AND id_producto = ?", (id_carrito, id_producto))
            producto_en_carrito = self.cursor.fetchone()

            if producto_en_carrito:
                # El producto ya está en el carrito, actualizar la cantidad
                cantidad_actual = producto_en_carrito[1]
                nueva_cantidad = cantidad_actual + cantidad
                self.cursor.execute("UPDATE ProductoEnCarrito SET cantidad = ? WHERE id_carrito_producto = ?", (nueva_cantidad, producto_en_carrito[0]))
            else:
                # El producto no está en el carrito, añadirlo
                self.cursor.execute("INSERT INTO ProductoEnCarrito (id_carrito, id_producto, cantidad) VALUES (?, ?, ?)",
                                    (id_carrito, id_producto, cantidad))

            self.conn.commit()
            return f"{cantidad} {nombre_producto}(s) añadidos al carrito."

        except Exception as e:
            return str(e)

    def borrar_del_carrito(self, id_carrito_producto):
        try:
            # Verificar si el producto está en el carrito
            self.cursor.execute("SELECT C.id_carrito FROM Carrito AS C "
                                "INNER JOIN ProductoEnCarrito AS PEC ON C.id_carrito = PEC.id_carrito "
                                "WHERE C.id_cliente = ? AND PEC.id_carrito_producto = ?",
                                (self.id_usuario, id_carrito_producto))
            carrito = self.cursor.fetchone()

            if carrito:
                id_carrito = carrito[0]

                # Eliminar el producto del carrito
                self.cursor.execute("DELETE FROM ProductoEnCarrito WHERE id_carrito = ? AND id_carrito_producto = ?", (id_carrito, id_carrito_producto))
                self.conn.commit()
                return "Producto eliminado del carrito."
            else:
                return "El carrito está vacío."

        except Exception as e:
            return str(e)

    def hacer_pago(self):
        try:
            # Calcular el precio total del carrito
            self.cursor.execute("SELECT C.id_carrito, SUM(P.precio * PEC.cantidad) FROM Carrito AS C "
                                "INNER JOIN ProductoEnCarrito AS PEC ON C.id_carrito = PEC.id_carrito "
                                "INNER JOIN Producto AS P ON PEC.id_producto = P.id_producto "
                                "WHERE C.id_cliente = ? AND PEC.id_producto IS NOT NULL",
                                (self.id_usuario,))
            carrito = self.cursor.fetchone()

            if carrito:
                id_carrito, precio_total = carrito

                # Registrar la compra (simulada)
                self.cursor.execute("INSERT INTO Compra (num_factura, precio_total, id_carrito) VALUES (?, ?, ?)",
                                    (1, precio_total, id_carrito))

                # Vaciar el carrito
                self.cursor.execute("DELETE FROM ProductoEnCarrito WHERE id_carrito = ?", (id_carrito,))
                self.conn.commit()

                return f"Compra realizada con éxito. Total a pagar: ${precio_total}"
            else:
                return "El carrito está vacío."

        except Exception as e:
            return str(e)

# Clase para la gestión del carrito
class Carrito:
    def __init__(self, db_name="FULLSTACK_DB"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def ver_carrito(self, id_usuario):
        try:
            # Consultar los productos en el carrito del usuario
            self.cursor.execute("SELECT PEC.id_carrito_producto, P.nombre, PEC.cantidad FROM ProductoEnCarrito AS PEC "
                                "INNER JOIN Producto AS P ON PEC.id_producto = P.id_producto "
                                "INNER JOIN Carrito AS C ON PEC.id_carrito = C.id_carrito "
                                "WHERE C.id_cliente = ?", (id_usuario,))
            carrito = self.cursor.fetchall()
            return carrito

        except Exception as e:
            return str(e)

    def cerrar_conexion(self):
        self.conn.close()

# Clase para realizar operaciones CRUD en la tabla Producto
class ProductoCRUD:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()

    def crear_producto(self, nombre, descripcion, precio, stock):
        try:
            self.cursor.execute("INSERT INTO Producto (nombre, descripcion, precio, stock) VALUES (?, ?, ?, ?)",
                                (nombre, descripcion, precio, stock))
            self.conn.commit()
            return "Producto agregado correctamente."

        except Exception as e:
            return str(e)

    def obtener_producto(self, id_producto):
        try:
            self.cursor.execute("SELECT * FROM Producto WHERE id_producto = ?", (id_producto,))
            producto = self.cursor.fetchone()
            return producto

        except Exception as e:
            return str(e)

    def actualizar_producto(self, id_producto, nuevo_nombre, nueva_descripcion, nuevo_precio, nuevo_stock):
        try:
            self.cursor.execute("UPDATE Producto SET nombre = ?, descripcion = ?, precio = ?, stock = ? WHERE id_producto = ?",
                                (nuevo_nombre, nueva_descripcion, nuevo_precio, nuevo_stock, id_producto))
            self.conn.commit()
            return "Producto modificado correctamente."

        except Exception as e:
            return str(e)

    def eliminar_producto(self, id_producto):
        try:
            self.cursor.execute("DELETE FROM Producto WHERE id_producto = ?", (id_producto,))
            self.conn.commit()
            return "Producto eliminado correctamente."

        except Exception as e:
            return str(e)

    def cerrar_conexion(self):
        self.conn.close()

# Ejemplo de uso
if __name__ == "__main":
    producto_crud = ProductoCRUD(conn)

    # Crear un producto
    resultado = producto_crud.crear_producto("Nuevo Producto", "Descripción del nuevo producto", 19.99, 50)
    print(resultado)

    # Leer un producto
    producto = producto_crud.obtener_producto(1)  # Cambiar el ID del producto según tus datos
    print(producto)

    # Actualizar un producto
    resultado = producto_crud.actualizar_producto(1, "Producto Actualizado", "Nueva descripción", 29.99, 75)
    print(resultado)

    # Eliminar un producto
    resultado = producto_crud.eliminar_producto(1)  # Cambiar el ID del producto según tus datos
    print(resultado)

    producto_crud.cerrar_conexion()
    conn.close()
