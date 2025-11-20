class Cliente:
    def __init__(self, dni, nombre, apellido, telefono, email):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"[{self.dni}] {self.nombre} {self.apellido} - Tel: {self.telefono} - Email: {self.email}"
