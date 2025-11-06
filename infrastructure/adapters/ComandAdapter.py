
class ComandAdapter:
    """
    Ejecutar comandos externos usando subprocess.
    Manejo especial para el comando 'cd' usando os.chdir() para asegurar la persistencia del cambio de directorio.
    """
    def __init__(self, subprocess_module, os):
        self.subprocess = subprocess_module
        self.os = os

    def ejecutar(self, comando: str)->str:
        """
        Ejecuta un comando en un nuevo proceso shell o cambia el directorio (cd).
        """
        comando_limpio = comando.strip()
        if comando_limpio.startswith("cd "):
            
            path = comando_limpio[3:].strip()
            if not path:
                path = self.os.path.expanduser('~')
                
            try:
                self.os.chdir(path)
                return f"Directorio cambiado exitosamente a: {self.os.getcwd()}"
            except FileNotFoundError:
                raise FileNotFoundError(f"Directorio no encontrado: {path}")
            except Exception as e:
                raise Exception(f"Error al cambiar de directorio: {e}")

        try:
            resultado = self.subprocess.run(
                comando_limpio, 
                shell=True, 
                check=True,
                capture_output=True,
                text=True,   
            )
            return resultado.stdout.strip()
        
        except self.subprocess.CalledProcessError as e:
            stderr_output = e.stderr.strip()
            raise Exception(f"Comando falló (Código: {e.returncode}). Stderr: {stderr_output if stderr_output else 'Sin salida de error.'}")
        
        except FileNotFoundError:
            raise FileNotFoundError("Comando no encontrado.")
        except Exception as e:
            raise Exception(f"Error desconocido al ejecutar comando: {e}")
