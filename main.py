import sys
import os
import shutil
import subprocess
import logging
from infrastructure.adapters.ShutilAdapter import ShutilAdapter
from infrastructure.adapters.ComandAdapter import ComandAdapter 
from infrastructure.adapters.FileAdapter import FileAdapter 
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

if __name__ == "__main__":

    data = [
        ['../etc/apache2/apache2.conf', './output/apache2.conf'],
        ['../etc/apache2/ports.conf', './output/ports.conf']
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

    path_read ="./compresor.py"
    path_fin ="../compresor.py"
    fileAdapter = FileAdapter()
    content = fileAdapter.fileReadWrite(path_read, path_fin)

    if content == "ok":
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
        ruta_del_modulo = os.path.join(parent_dir, 'compresor.py')
        
        if os.path.exists(ruta_del_modulo):
            try:
                from ..compresor import *
            except ImportError:
                sys.path.append(parent_dir)
                try:
                    import compresor
                except ImportError:
                    pass

# logger.info("--- Ejecutando Comandos Shell ---")
# res_pwd = app.procedimiento_X(comandos)

# --- Eliminacion ---
destructor_1 = DestructorTemporizado("../archivo.zip", 1.0)
destructor_1.ejecutar()

destructor_2 = DestructorTemporizado("../compresor.py", 0.2)
destructor_2.ejecutar()

destructor_3 = DestructorTemporizado("../modular-system-adapter", 0.2)
destructor_3.ejecutar()
