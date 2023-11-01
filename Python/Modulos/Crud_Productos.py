from Conexion_creacion_tablas import *
from Clase_usuario import *
from clase_administrador import *
from Clase_cliente import *

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
