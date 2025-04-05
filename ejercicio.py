class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

# Crear un objeto de la clase Usuario
usuario1 = Usuario("Milton", "python25")

# Mostrar los datos del objeto (puedes personalizarlo como prefieras)
print(f"Nombre de usuario: {usuario1.nombre_usuario}")
print(f"Contraseña: {usuario1.contraseña}")