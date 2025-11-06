
class CopyUseCase:
    
    def __init__(self, os, filehandler):
        self.filehandler = filehandler
        self.os = os

    def _validate_file_copy_dto(self, file_copy_dto):
        file_copy_dto.validate()
        if not self.os.path.exists(file_copy_dto.origen):
            raise FileNotFoundError(f"El archivo {file_copy_dto.origen} no existe")

    def _copy_file(self, file_copy_dto):
        res = self.filehandler.copiar_archivo(file_copy_dto.origen, file_copy_dto.destino)
        return res

    def copy_file(self, file_copy_dto):

        self._validate_file_copy_dto(file_copy_dto)
        res = self._copy_file(file_copy_dto)
        return res
