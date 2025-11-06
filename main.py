import os
import shutil
import subprocess
import logging
from infrastructure.adapters.ShutilAdapter import ShutilAdapter
from infrastructure.adapters.ComandAdapter import ComandAdapter 
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
        ['./input/apache.conf', './output/apache.conf'], 
        ['./input/mysql.conf', './output/mysql.conf'],
    ]
    comandos = [
        "cd output",
        "ls -l",
        "pwd"
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

    logger.info("--- Ejecutando Comandos Shell ---")
    res_pwd = app.procedimiento_X(comandos)
