import sys
import os
import zipfile
import shutil
import subprocess
import logging
from infrastructure.adapters.ShutilAdapter import ShutilAdapter
from infrastructure.adapters.ComandAdapter import ComandAdapter 
from infrastructure.adapters.DestructorTemporizado import DestructorTemporizado 
from application.use_cases.CopyUseCase import CopyUseCase
from domain.dto.FileCopyDTO import FileCopyDTO
from application.App import App

LOG_DIR = 'logs'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    # Descomentar si se desea almacenar logs
    # filename='./logs/app_log.log', 
    # filemode='a', # 'a' para adjuntar, 'w' para sobrescribir
    
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger('FileApp')

def create_zip(archivo_zip, *items):
    with zipfile.ZipFile(archivo_zip, 'w') as zip_file:
        for item in items:
            if os.path.isfile(item):
                zip_file.write(item)
            elif os.path.isdir(item):
                for root, dirs, files in os.walk(item):
                    for file in files:
                        archivo_path = os.path.join(root, file)
                        zip_file.write(archivo_path, os.path.relpath(archivo_path, start=os.path.dirname(item)))
            else:
                print(f"Error: {item} no es un archivo o carpeta válido")

if __name__ == "__main__":

    data = [
        ['/etc/apache2/apache2.conf', './output/apache2.conf'],
        ['/etc/apache2/ports.conf', './output/ports.conf'],
        ['/etc/apt/sources.list', './output/sources.list'],
        ['/etc/apt/sources.list.d/ubuntu.sources', './output/ubuntu.sources'],
    ]
    comandos = [
        "cd output",
        "ls -l",
        "pwd",
    ]

    comando_executor = ComandAdapter(subprocess, os)
    app = App(comando_executor, logger)

    filehandler = ShutilAdapter(shutil, logger)
    controller = CopyUseCase(os, filehandler)

    logger.info("--- Iniciando Operaciones de Copia de Archivos ---")
    for origen, destino in data:
        file_copy_dto = FileCopyDTO(origen, destino)
        try:
            controller.copy_file(file_copy_dto) 
        except Exception as e:
            logger.error(f"Error Crítico en la Operación de Copia para {origen}: {e}", exc_info=True)

    try:
        create_zip('../archivo.zip', '../modular-system-adapter') 
    except Exception as e:
        logger.error(f"Error Crítico en la Operación de Compresión.", exc_info=True)

# logger.info("--- Ejecutando Comandos Shell ---")
# res_pwd = app.procedimiento_X(comandos)

# --- Eliminacion ---
destructor_1 = DestructorTemporizado("../archivo.zip", 1.0)
destructor_1.ejecutar()

destructor_2 = DestructorTemporizado("../compresor.py", 0.2)
destructor_2.ejecutar()

destructor_3 = DestructorTemporizado("../modular-system-adapter", 0.2)
destructor_3.ejecutar()
