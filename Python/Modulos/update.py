from python_fullstack import *
from Clase_usuario import *
from clase_administrador import *
from Class_Admin_MENU import *
from Clase_cliente import *


class Update:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()

    def actualizar_producto(self, id_producto, nuevo_nombre, nueva_descripcion, nuevo_precio, nuevo_stock):
        try:
            self.cursor.execute("UPDATE Producto SET nombre = ?, descripcion = ?, precio = ?, stock = ? WHERE id_producto = ?",
                                (nuevo_nombre, nueva_descripcion, nuevo_precio, nuevo_stock, id_producto))
            self.conn.commit()
            return "Producto modificado correctamente."

        except Exception as e:
            return str(e)  

    def cerrar_conexion(self):
        self.conn.close()

# Ejemplo de uso
if __name__ == "__main":
    update = Update(conn)

    # Actualizar un producto
    resultado = update.actualizar_producto(1, "Producto Actualizado", "Nueva descripción", 29.99, 75)
    print(resultado)   

    update.cerrar_conexion()
    conn.close()