import uuid


class Usuario:

    def __init__(self, nombre: str, email: str):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.email = email

    def is_admin(self) -> bool:
        return False


class Cliente(Usuario):

    def __init__(self, nombre: str, email: str, direccion: str):
        super().__init__(nombre, email)
        self.direccion = direccion


class Administrador(Usuario):

    def __init__(self, nombre: str, email: str):
        super().__init__(nombre, email)

    def is_admin(self) -> bool:
        return True