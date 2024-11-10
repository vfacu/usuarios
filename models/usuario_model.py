from models.base_model import Base


class Usuario(Base):
    filename = 'usuarios.json'

    def __init__(self, legajo, dni, nombre, apellido, email, telefono) -> None:
        self.legajo = legajo
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def __str__(self) -> str:
        return (
            f"Legajo: {self.legajo}, DNI: {self.dni}, Nombre: {self.nombre}, "
            f"Apellido: {self.apellido}, Email: {self.email}, Teléfono: {self.telefono}"
        )
