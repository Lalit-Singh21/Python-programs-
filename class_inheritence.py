class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        # to represent a connected device
        self.connected = True

    def __str__(self):
        # !r calls the repr method
        return f"<>Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected")

# printer = Device("Printer", "USB")
# print(printer)
# printer.disconnect()

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        # call to include methods defined in device init
        super().__init__(name, connected_by)
        self.capacity = capacity # max capacity
        self.remaining_pages = capacity # left capacity

    def __str__(self):
        #return f"<>Printer {self.name}, {self.connected_by}, {self.capacity}"
        return f"{super().__str__()} ({self.remaining_pages} remaining)"

    def print(self, pages):
        if not self.connected:
            print("printer not connected")
            return
        print(f"printing {pages} pages")
        self.remaining_pages -= pages

printer = Printer("printer1", "usb", 1000)
printer.print(20)
print(printer)
printer.disconnect()
printer.print(30)