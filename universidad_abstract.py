from .ingreso import *


class EjemploAbstractFactory:
    def obtener_nombre(self):
        return "Documento"

    def operacion(self):
        print("Ejemplo Abstract Factory")
        print("seleccione si es Nuevo u Homologante: \n\t 0 - Nuevo \n\t 1 - Homologante")
        ingresos = [DocumentoNuevo(), DocumentoHomologante(), ]

        ingreso = ingresos[int(input())]

        documentos = [ingreso.crearCedula(), ingreso.crearDiploma(),
                      ingreso.crearIcfes(), ingreso.crearEps(), ingreso.crearNotas()]

        for p in documentos:
            p.implementacion()
            p.operacion()
