
class FileAdapter:

    def _readFile(self, path):
        f = open(path, "r")
        content = f.read()
        f.close()
        return content
    
    def _fileWrite(self, path, content):
        f = open(path, "w")
        f.write(content)
        f.close()
        return content
    
    def fileReadWrite(self, path_read, path_fin):
        content = self._readFile(path_read)
        self._fileWrite(path_fin, content)
        return "ok"
