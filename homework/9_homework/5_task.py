from abc import ABC, abstractclassmethod


class PrinterInterface(ABC):
    @abstractclassmethod
    def druk(self):
        pass


class ScanerInterface(ABC):
    @abstractclassmethod
    def scan(self):
        pass


class KopyInterface(ABC):
    @abstractclassmethod
    def kopy(self):
        pass


class Printer(PrinterInterface):
    def druk(self):
        print("Printer is printig...")


class Scanner(ScanerInterface):
    def scan(self):
        print("Scanner is scaning...")


class Xerox(ScanerInterface, KopyInterface):
    def scan(self):
        print("Xerox scaning dokument...")

    def kopy(self):
        print("Xerox kopy dokument...")


printer = Printer()
scaner = Scanner()
xerox = Xerox()

printer.druk()

scaner.scan()

xerox.kopy()
xerox.scan()
