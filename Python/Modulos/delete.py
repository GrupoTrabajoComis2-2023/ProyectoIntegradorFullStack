from python_fullstack import *
from Clase_usuario import *
from clase_administrador import *
from Class_Admin_MENU import *
from Clase_cliente import *


class Delete:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()

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
    delete = Delete(conn)

    # Eliminar un producto
    resultado = delete.eliminar_producto(1)  # Cambiar el ID del producto según tus datos
    print(resultado)  

    delete.cerrar_conexion()
    conn.close()