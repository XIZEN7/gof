from abc import ABC, abstractmethod


# Documentos nesesarios para ingresar a la universidad
class Cedula(ABC):
    def implementacion(self):
        print("Fotocopia cedula")

    @abstractmethod
    def operacion(self):
        pass


class Icfes(ABC):
    def implementacion(self):
        print("Puntaje icfes")

    @abstractmethod
    def operacion(self):
        pass


class Diploma(ABC):
    def implementacion(self):
        print("Diploma bachillerato")

    @abstractmethod
    def operacion(self):
        pass


class Eps(ABC):
    def implementacion(self):
        print("Eps")

    @abstractmethod
    def operacion(self):
        pass


class Materias(ABC):
    def implementacion(self):
        print("Materias para homologar")

    @abstractmethod
    def operacion(self):
        pass


# Nuevo
class CedulaNuevo(ABC):
    def implementacion(self):
        print("Fotocopia cedula")

    @abstractmethod
    def operacion(self):
        pass


class IcfesNuevo(ABC):
    def implementacion(self):
        print("Puntaje icfes")

    @abstractmethod
    def operacion(self):
        pass


class DiplomaNuevo(ABC):
    def implementacion(self):
        print("Diploma bachillerato")

    @abstractmethod
    def operacion(self):
        pass


class EpsNuevo(ABC):
    def implementacion(self):
        print("Eps")

    @abstractmethod
    def operacion(self):
        pass


# Homologante
class CedulaHomologante(ABC):
    def implementacion(self):
        print("Fotocopia cedula")

    @abstractmethod
    def operacion(self):
        pass


class IcfesHomologante(ABC):
    def implementacion(self):
        print("Puntaje icfes")

    @abstractmethod
    def operacion(self):
        pass


class DiplomaHomologante(ABC):
    def implementacion(self):
        print("Diploma bachillerato")

    @abstractmethod
    def operacion(self):
        pass


class EpsHomologante(ABC):
    def implementacion(self):
        print("Eps")

    @abstractmethod
    def operacion(self):
        pass


# Materias para homologar de otra institución
class MateriasHomologante(ABC):
    def implementacion(self):
        print("Materias para homologar")

    @abstractmethod
    def operacion(self):
        pass
