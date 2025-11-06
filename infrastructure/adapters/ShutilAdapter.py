
class ShutilAdapter:
    """
    Esta clase es la que gestiona los archivos
    """
    def __init__(self, shutil, logger):
        self.shutil = shutil
        self.logger = logger

    def copiar_archivo(self, origen, destino) -> str:
        """
        Copia archivos de un origen a un destino
        """
        try:
            self.shutil.copyfile(origen, destino)
            self.logger.info(f'Archivo copiado correctamente a: "{destino}"')
            return None

        except FileNotFoundError as e:
            raise e

        except Exception as e:
            raise e
