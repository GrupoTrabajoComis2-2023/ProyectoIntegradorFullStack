from python_fullstack import *
from Clase_usuario import *
from clase_administrador import *
from Class_Admin_MENU import *

# Clase para la gestión de clientes
class Cliente(Usuario):
    def __init__(self, db_name="intento_menu"):
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