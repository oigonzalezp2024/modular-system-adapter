import os
import shutil
import time

class DestructorTemporizado:
    def __init__(self, ruta: str, minutos: float):
        self._ruta = ruta
        self._espera_segundos = minutos * 60

    def _eliminar(self):
        if os.path.isfile(self._ruta):
            os.remove(self._ruta)
            print(f"🗑️ Archivo eliminado: {os.path.basename(self._ruta)}")
        elif os.path.isdir(self._ruta):
            # ¡Cuidado! Borra la carpeta y TODO su contenido.
            shutil.rmtree(self._ruta)
            print(f"🗑️ Carpeta eliminada: {os.path.basename(self._ruta)}")
        else:
            print(f"⚠️ Advertencia: '{os.path.basename(self._ruta)}' no existe o no es un elemento válido.")

    def ejecutar(self):
        if not os.path.exists(self._ruta):
            print(f"❌ Error: La ruta '{self._ruta}' no existe.")
            return

        print(f"⏳ Esperando {self._espera_segundos} segundos para eliminar: {self._ruta}")
        
        try:
            time.sleep(self._espera_segundos)
            self._eliminar()
            print("✅ Tarea finalizada.")
        except PermissionError:
            print(f"❌ Error de Permiso: No se pudo eliminar '{os.path.basename(self._ruta)}'.")
        except Exception as e:
            print(f"🔥 Error inesperado: {e}")

