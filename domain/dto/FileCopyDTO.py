
class FileCopyDTO:

    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino

    def validate(self):
        if not self.origen or not self.destino:
            raise ValueError("Origen y destino deben estar establecidos")

    def __str__(self):
        return f"Origen: {self.origen}, Destino {self.destino}"
