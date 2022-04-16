import os
from pathlib import Path


class FindDataBase:
    def __init__(self, database: str):
        """
        :encontra o local do arquivo
        :param database:
        """
        self.__database: str = database

    @property
    def database(self) -> str:
        return self.__database

    def findFiles(self):
        """
        Encontra os diretórios dos arquivos
        :return:
        """
        FILE_PATH: Path = Path(self.database)
        root: str = "C:\\"
        filepath: str = os.path.join(root, FILE_PATH)
        os.chdir(filepath)
        return filepath


if __name__ == '__main__':
    fdb = FindDataBase('Users\\Marcu\\Desktop\\AtividadesEmPython\\file')
    fdb.findFiles()