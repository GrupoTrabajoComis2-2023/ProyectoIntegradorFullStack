from python_fullstack import *
from Clase_usuario import *

# Clase para la gestión de administradores
class Administrador(Usuario):
    def __init__(self, db_name="intento_menu"):
        super().__init__(db_name)
        self.producto_crud = ProductoCRUD(self.conn)

    def menu_administrador(self):
        while True:
            print("Menú Administrador:")
            print("1: Ver productos")
            print("2: Agregar producto")
            print("3: Modificar producto")
            print("4: Eliminar producto")
            print("5: Salir")
            opcion = input("Elija una opción: ")

            if opcion == "1":
                # Ver productos
                self.ver_productos()
            elif opcion == "2":
                # Agregar producto
                nombre = input("Ingrese el nombre del producto: ")
                descripcion = input("Ingrese la descripción del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                stock = int(input("Ingrese el stock del producto: "))
                resultado = self.producto_crud.crear_producto(nombre, descripcion, precio, stock)
                print(resultado)
            elif opcion == "3":
                # Modificar producto
                id_producto = int(input("Ingrese el ID del producto a modificar: "))
                nombre = input("Ingrese el nuevo nombre del producto: ")
                descripcion = input("Ingrese la nueva descripción del producto: ")
                precio = float(input("Ingrese el nuevo precio del producto: "))
                stock = int(input("Ingrese el nuevo stock del producto: "))
                resultado = self.producto_crud.actualizar_producto(id_producto, nombre, descripcion, precio, stock)
                print(resultado)
            elif opcion == "4":
                # Eliminar producto
                id_producto = int(input("Ingrese el ID del producto a eliminar: "))
                resultado = self.producto_crud.eliminar_producto(id_producto)
                print(resultado)
            elif opcion == "5":
                print("¡Hasta luego, administrador!")
                break
            else:
                print("Opción no válida. Por favor, elija una opción válida.")
def insertar_administrador():
    # Conexión a la base de datos
    conn = sqlite3.connect("intento_menu")
    cursor = conn.cursor()

    # Credenciales del administrador
    usuario_admin = "admin"
    contraseña_admin = "1234admin"

    # Insertar al administrador
    cursor.execute("INSERT INTO Administrador (usuario_admin, contraseña_admin) VALUES (?, ?)",
                   (usuario_admin, contraseña_admin))
    conn.commit()
    conn.close()
# Llamamos a la función para insertar al administrador
insertar_administrador()