from python_fullstack import *
from Clase_usuario import *
from clase_administrador import *
from Class_Admin_MENU import *
from Clase_cliente import *


class Create:
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

    def cerrar_conexion(self):
        self.conn.close()

# Ejemplo de uso
if __name__ == "__main":
    create = Create(conn)

    # Crear un producto
    resultado = create.crear_producto("Nuevo Producto", "Descripción del nuevo producto", 19.99, 50)
    print(resultado)    

    create.cerrar_conexion()
    conn.close()