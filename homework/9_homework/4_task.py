from abc import ABC, abstractclassmethod


class NetworkPrinter(ABC):
    @abstractclassmethod
    def druk(self):
        pass

    @abstractclassmethod
    def scan(self):
        pass

    @abstractclassmethod
    def kopy(self):
        pass


class Printer(NetworkPrinter):
    def druk(self):
        print("Printing of the dokument...")

    def scan(self):
        print("Printer cannot scan.")

    def kopy(self):
        print("Printer cannot kopy.")


class Scanner(NetworkPrinter):
    def scan(self):
        print("Scaning of the dokument...")

    def kopy(self):
        print("Scanner cannot kopy.")

    def druk(self):
        print("Scanner cannot print.")


printer = Printer()
scaner = Scanner()

printer.druk()
printer.kopy()
printer.scan()
scaner.scan()
scaner.druk()
scaner.kopy()
