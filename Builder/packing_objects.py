from Builder import interfaces


class Wrapper(interfaces.Packing):
    def pack(self):
        return "Wrapper"


class Bottle(interfaces.Packing):
    def pack(self):
        return "Bottle"
