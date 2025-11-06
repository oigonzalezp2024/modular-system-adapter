import zipfile
import os

def crear_zip(archivo_zip, *items):
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

# Ejemplo de uso
crear_zip('../archivo.zip', '../modular-system-adapter')
