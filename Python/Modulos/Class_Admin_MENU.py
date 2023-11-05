from python_fullstack import *
from Clase_usuario import *
from Clase_carrito import *
from Clase_cliente import *
from clase_administrador import *
from create import *
from delete import *
from update import *
from read import *



class Admin:
    def __init__(self, database):
        # Constructor de la clase Admin
        self.database = database

    def ver_productos(self):
        # Lógica para mostrar productos
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Producto")
        productos = cursor.fetchall()
        conn.close()
        return productos

    def agregar_producto(self, nombre, descripcion, precio, stock):
        # Lógica para agregar un producto
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO producto (nombre, descripcion, precio, stock) VALUES (?, ?, ?, ?)", (nombre, descripcion, precio, stock))
        conn.commit()
        conn.close()
        return "Producto agregado exitosamente."

    def modificar_producto(self, id_producto, nombre, descripcion, precio, stock):
        # Lógica para modificar un producto
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("UPDATE producto SET nombre=?, descripcion=?, precio=?, stock=? WHERE id_producto=?", (nombre, descripcion, precio, stock, id_producto))
        conn.commit()
        conn.close()
        return "Producto modificado exitosamente."

    def eliminar_producto(self, id_producto):
        # Lógica para eliminar un producto
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM producto WHERE id_producto=?", (id_producto,))
        conn.commit()
        conn.close()
        return "Producto eliminado exitosamente"


if __name__ == "__main__":
    print("¡Bienvenido al sistema de gestión!")

    admin = Admin("intento_menu")



    while True:
        print("Menú de opciones:")
        print("1: Acceder como invitado (Ver productos)")
        print("2: Registrarse como nuevo usuario")
        print("3: Iniciar sesión como usuario")
        print("4: Iniciar sesión como administrador")
        print("5: Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            # Acceder como invitado (ver productos)
            print("Accediendo como invitado (productos):")

            # Aquí debes agregar la lógica para mostrar todos los productos
            productos = admin.ver_productos()

            if productos:
                print("Productos disponibles:")
            for producto in productos:
                print(f"ID: {producto[0]}")
                print(f"Nombre: {producto[1]}")
                print(f"Descripción: {producto[2]}")
                print(f"Precio: {producto[3]}")
                print(f"Stock: {producto[4]}")
                print("------------------")
            else:
                print("No hay productos disponibles.")

        elif opcion == "2":
            # Registrarse como nuevo usuario
            nuevo_nombre_usuario = input("Ingrese un nombre de usuario único: ")
            nueva_contraseña = input("Ingrese una contraseña: ")

            # Verificar si el nombre de usuario es único en la base de datos
            usuario = Usuario("intento_menu")
            if usuario.verificar_nombre_usuario_unico(nuevo_nombre_usuario):
                resultado = usuario.registrarse(nuevo_nombre_usuario, nueva_contraseña)
                print(resultado)
            else:
                print("El nombre de usuario ya está en uso. Intente con otro nombre de usuario.")

        elif opcion == "3":
            # Iniciar sesión como usuario
            nombre_usuario = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña: ")

            # Verificar las credenciales y permitir el acceso
            usuario = Usuario("intento_menu")
            resultado = usuario.login(nombre_usuario, contraseña)
            if resultado == "Inicio de sesión exitoso.":
                print("Acceso como usuario exitoso.")

                while True:
                    print("Menú de usuario:")
                    print("1: Ver productos")
                    print("2: Comprar producto")
                    print("3: Ver carrito de compras")
                    print("4: Salir")

                    opcion_usuario = input("Elija una opción: ")

                    if opcion_usuario == "1":
                        # Ver productos disponibles
                        productos = usuario.ver_productos()
                        if productos:
                            print("Productos disponibles:")
                            for producto in productos:
                                print(f"ID: {producto[0]}")
                                print(f"Nombre: {producto[1]}")
                                print(f"Descripción: {producto[2]}")
                                print(f"Precio: {producto[3]}")
                                print(f"Stock: {producto[4]}")
                                print("------------------")
                        else:
                            print("No hay productos disponibles.")
                    elif opcion_usuario == "2":
                        # lógica para comprar productos
                        id_producto = input("Ingrese el ID del producto que desea comprar: ")
                        cantidad = int(input("Ingrese la cantidad que desea comprar: "))
                        resultado = usuario.comprar_producto(id_producto, cantidad)
                        print(resultado)

                    elif opcion_usuario == "3":
                        # Ver carrito de compras
                        carrito = usuario.ver_carrito()
                        if carrito:
                            print("Productos en el carrito:")
                            for item in carrito:
                                if len(item) == 3:
                                    id_carrito_producto, nombre_producto, cantidad = item
                                    print(f"ID del producto en el carrito: {id_carrito_producto}")
                                    print(f"Nombre del producto: {nombre_producto}")
                                    print(f"Cantidad en el carrito: {cantidad}")
                                    print("------------------")
                                else:()
                        else:
                            print("El carrito de compras está vacío.")
                    elif opcion_usuario == "4":
                        print("Cerrando sesión de usuario.")
                        break
                    else:
                        print("Opción no válida. Por favor, elija una opción válida.")
            else:
                print("Acceso denegado. Credenciales incorrectas.")

        elif opcion == "4":
            # Iniciar sesión como administrador (credenciales preestablecidas)
            nombre_admin = input("Ingrese el nombre de administrador : ")
            contraseña_admin = input("Ingrese la contraseña de administrador: ")

            if nombre_admin == "admin" and contraseña_admin == "1234admin":
                print("Accediendo como administrador.")

                while True:
                    print("Menú de administrador:")
                    print("1: Ver productos")
                    print("2: Agregar producto")
                    print("3: Modificar producto")
                    print("4: Eliminar producto")
                    print("5: Salir")
                    opcion_admin = input("Elija una opción: ")

                    if opcion_admin == "1":
                        # Ver productos
                        admin.ver_productos()
                    elif opcion_admin == "2":
                        # Agregar producto
                        nombre = input("Ingrese el nombre del producto: ")
                        descripcion = input("Ingrese la descripción del producto: ")
                        precio = float(input("Ingrese el precio del producto: "))
                        stock = int(input("Ingrese el stock del producto: "))
                        resultado = admin.agregar_producto(nombre, descripcion, precio, stock)
                        print(resultado)
                    elif opcion_admin == "3":
                        # Modificar producto
                        id_producto = int(input("Ingrese el ID del producto a modificar: "))
                        nombre = input("Ingrese el nuevo nombre del producto: ")
                        descripcion = input("Ingrese la nueva descripción del producto: ")
                        precio = float(input("Ingrese el nuevo precio del producto: "))
                        stock = int(input("Ingrese el nuevo stock del producto: "))
                        resultado = admin.modificar_producto(id_producto, nombre, descripcion, precio, stock)
                        print(resultado)
                    elif opcion_admin == "4":
                        # Eliminar producto
                        id_producto = int(input("Ingrese el ID del producto a eliminar: "))
                        resultado = admin.eliminar_producto(id_producto)
                        print(resultado)
                    elif opcion_admin == "5":
                        print("Cerrando sesión de administrador.")
                        break
                    else:
                        print("Opción no válida. Por favor, elija una opción válida.")

            else:
                print("Acceso denegado. Credenciales incorrectas.")

        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")
