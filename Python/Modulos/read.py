from python_fullstack import *
from Clase_usuario import *
from clase_administrador import *
from Class_Admin_MENU import *
from Clase_cliente import *


class Read:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()

    def obtener_producto(self, id_producto):
        try:
            self.cursor.execute("SELECT * FROM Producto WHERE id_producto = ?", (id_producto,))
            producto = self.cursor.fetchone()
            return producto

        except Exception as e:
            return str(e) 

    def cerrar_conexion(self):
        self.conn.close()

# Ejemplo de uso
if __name__ == "__main":
    read = Read(conn)

    # Leer un producto
    producto = read.obtener_producto(1)  # Cambiar el ID del producto según tus datos
    print(producto)   

    read.cerrar_conexion()
    conn.close()