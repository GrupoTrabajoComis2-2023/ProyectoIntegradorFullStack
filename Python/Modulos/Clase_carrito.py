from Conexion_creacion_tablas import *
from Clase_usuario import *
from clase_administrador import *
from Clase_cliente import *
from Crud_Productos import *

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
