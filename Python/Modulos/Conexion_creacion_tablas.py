import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect("FULLSTACK_DB")
cursor = conn.cursor()

# Creación de las tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS Registro (
    id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    apellido TEXT,
    email TEXT,
    contraseña TEXT
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Administrador (
    id_administrador INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_admin TEXT,
    contraseña_admin TEXT
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Producto (
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    descripcion TEXT,
    precio REAL,
    stock INTEGER
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_usuario TEXT,
    contraseña TEXT,
    id_cliente INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES Cliente (id_cliente)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Cliente (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    telefono TEXT,
    direccion TEXT,
    pais TEXT,
    codigo_postal TEXT
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Carrito (
    id_carrito INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES Cliente (id_cliente)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ProductoEnCarrito (
    id_carrito_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    id_carrito INTEGER,
    id_producto INTEGER,
    cantidad INTEGER,
    FOREIGN KEY (id_carrito) REFERENCES Carrito (id_carrito),
    FOREIGN KEY (id_producto) REFERENCES Producto (id_producto)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Compra (
    id_compra INTEGER PRIMARY KEY AUTOINCREMENT,
    num_factura INTEGER,
    precio_total REAL,
    fecha_compra DATE,
    productos TEXT,
    medio_pago TEXT,
    id_carrito INTEGER,
    FOREIGN KEY (id_carrito) REFERENCES Carrito (id_carrito)
)""")

# Commit de la transacción y cierre de la conexión
conn.commit()
conn.close()