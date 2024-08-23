from abc import ABCMeta, abstractmethod


class ClasseAbstrataExemplo(metaclass=ABCMeta):

    @abstractmethod
    def imprima(self):
        print("Implementação do método abstrato na classe abstrata.")


class ClasseFilha(ClasseAbstrataExemplo):

    def imprima(self):
        super().imprima()
        print("Método implementado na classe filha, sem uso da implementação da classe mãe.")
obj_um = ClasseFilha()
obj_um.imprima()
