from Conexion_creacion_tablas import *

# Clase para la gestión de usuarios
class Usuario:
    def __init__(self, db_name="FULLSTACK_DB"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def registrarse(self, nombre_usuario, contraseña, email):
        try:
            # Verificar si el usuario ya existe
            self.cursor.execute("SELECT id_usuario FROM Usuario WHERE nombre_usuario = ?", (nombre_usuario,))
            usuario_existente = self.cursor.fetchone()

            if usuario_existente:
                return "El nombre de usuario ya está en uso."

            # Insertar nuevo usuario
            self.cursor.execute("INSERT INTO Usuario (nombre_usuario, contraseña, email) VALUES (?, ?, ?)",
                                (nombre_usuario, contraseña, email))
            self.conn.commit()
            return "Registro exitoso."

        except Exception as e:
            return str(e)

    def login(self, nombre_usuario, contraseña):
        try:
            # Verificar las credenciales de inicio de sesión
            self.cursor.execute("SELECT id_usuario FROM Usuario WHERE nombre_usuario = ? AND contraseña = ?",
                                (nombre_usuario, contraseña))
            usuario = self.cursor.fetchone()

            if usuario:
                return "Inicio de sesión exitoso."
            else:
                return "Credenciales incorrectas."

        except Exception as e:
            return str(e)

    def editar_perfil(self, id_usuario, nuevo_nombre, nueva_contraseña, nuevo_email):
        try:
            # Actualizar los datos del usuario
            self.cursor.execute("UPDATE Usuario SET nombre_usuario = ?, contraseña = ?, email = ? WHERE id_usuario = ?",
                                (nuevo_nombre, nueva_contraseña, nuevo_email, id_usuario))
            self.conn.commit()
            return "Perfil actualizado correctamente."

        except Exception as e:
            return str(e)

    def contraseña_olvidada(self, nombre_usuario, nueva_contraseña):
        try:
            # Actualizar la contraseña del usuario
            self.cursor.execute("UPDATE Usuario SET contraseña = ? WHERE nombre_usuario = ?",
                                (nueva_contraseña, nombre_usuario))
            self.conn.commit()
            return "Contraseña actualizada correctamente."

        except Exception as e:
            return str(e)

    def cerrar_conexion(self):
        self.conn.close()
