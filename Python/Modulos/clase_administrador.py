from Conexion_creacion_tablas import *
from Clase_usuario import *

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