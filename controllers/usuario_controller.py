from typing import Optional
from termcolor import colored
from models.usuario_model import Usuario
import utils.console_handler as console


class UsuarioController:
    @classmethod
    def start(cls) -> None:
        Usuario.load()
        console.clear()
        while True:
            print("\nMenú CRUD de Usuarios")
            print("1. Crear Usuario")
            print("2. Leer Usuarios")
            print("3. Actualizar Usuario")
            print("4. Eliminar Usuario")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                cls.add()
            elif opcion == '2':
                cls.list_all()
            elif opcion == '3':
                cls.update()
            elif opcion == '4':
                cls.delete()
            elif opcion == '5':
                Usuario.save()
                print("Datos guardados. Saliendo...")
                break
            else:
                print(colored("Opción inválida.", "red"))

    @classmethod
    def add(cls) -> None:
        console.clear()
        try:
            legajo = int(input("Número de legajo: "))
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")
            new_user = Usuario(legajo, dni, nombre, apellido, email, telefono)
            Usuario.all.append(new_user)
            Usuario.save()
            print(colored("Usuario creado con éxito.", "green"))
        except ValueError as e:
            print(colored(f"Error al crear el usuario: {e}", "red"))

    @classmethod
    def list_all(cls) -> None:
        console.clear()
        if not Usuario.all:
            print(colored("No hay usuarios registrados.", "red"))
        for usuario in Usuario.all:
            print(usuario)

    @classmethod
    def update(cls) -> None:
        cls.list_all()
        try:
            legajo = int(
                input("Ingrese el número de legajo del usuario a actualizar: "))
            usuario = cls.load_user(legajo)
            if usuario:
                usuario.nombre = input("Nuevo Nombre: ")
                usuario.apellido = input("Nuevo Apellido: ")
                usuario.email = input("Nuevo Email: ")
                usuario.telefono = input("Nuevo Teléfono: ")
                print(colored("Usuario actualizado.", "green"))
            else:
                print(colored("Usuario no encontrado.", "red"))
        except ValueError as e:
            print(colored(f"Error: {e}", "red"))

    @classmethod
    def delete(cls) -> None:
        try:
            legajo = int(
                input("Ingrese el número de legajo del usuario a eliminar: "))
            usuario = cls.load_user(legajo)
            if usuario:
                Usuario.all.remove(usuario)
                print(colored("Usuario eliminado.", "green"))
            else:
                print(colored("Usuario no encontrado.", "red"))
        except ValueError as e:
            print(colored(f"Error: {e}", "red"))

    @classmethod
    def load_user(cls, legajo: int) -> Optional[Usuario]:
        for usuario in Usuario.all:
            if usuario.legajo == legajo:
                return usuario
        return None
