
class App:
    """
    Centraliza la lógica de ejecución de comandos.
    """
    def __init__(self, comando_instancia, logger):
        self.comando_executor = comando_instancia
        self.logger = logger

    def comando(self, comando_a_ejecutar):
        try:
            resultado = self.comando_executor.ejecutar(comando_a_ejecutar)
            
            self.logger.info(f'"{comando_a_ejecutar}" ejecutado con éxito.')
            
            return resultado
        
        except Exception as e:
            self.logger.error(f'Fallo al ejecutar "{comando_a_ejecutar}". Tipo: {type(e).__name__}, Detalle: {e}')
            return None

    def procedimiento_X(self, comandos):
        separador = '='*60
        self.logger.info(f'\n{separador}\nIniciando secuencia de comandos\n{separador}')
        for i in comandos:
            resultado_comando = self.comando(i)
            if resultado_comando is not None:
                self.logger.info(f'\n--- Comando "{i}" Output ---\n{resultado_comando}')
