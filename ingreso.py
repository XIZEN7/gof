from abc import ABC, abstractmethod

from .papeles import *


class Documento(ABC):

    @abstractmethod
    def creaCedula(self):
        pass

    @abstractmethod
    def crearIcfes(self):
        pass

    @abstractmethod
    def crearDiploma(self):
        pass

    @abstractmethod
    def crearEps(self):
        pass

    @abstractmethod
    def crearMaterias(self):
        pass


class DocumentoNuevo(Documento):

    def crearCedula(self):
        return CedulaNuevo()

    def crearIcfes(self):
        return IcfesNuevo()

    def crearDiploma(self):
        return DiplomaNuevo()

    def crearEps(self):
        return EpsNuevo()


class DocumentoHomologante(Documento):

    def crearCedula(self):
        return CedulaHomologante()

    def crearIcfes(self):
        return IcfesHomologante()

    def crearDiploma(self):
        return DiplomaHomologante()

    def crearEps(self):
        return EpsHomologante()

    def crearMaterias(self):
        return MateriasHomologante()
