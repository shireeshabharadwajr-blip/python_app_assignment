class Printer:
    def __init__(self, capacity, tone, printer_type):
        self.capacity = capacity
        self.tone = tone
        self.printer_type = printer_type

if __name__ == "__main__":
    printer1 = Printer(500, "Mono", "Laser")
    printer2 = Printer(300, "Color", "Inkjet")
    printer3 = Printer(1000, "Color", "Enterprise")

    print("printer1 identity:", id(printer1))
    print("printer2 identity:", id(printer2))
    print("printer3 identity:", id(printer3))
