import os
import platform
from threading import Thread
# from glob import glob
# from Controllers.SearchPrimerNumberController import SearchPrimerNumberController
from Controllers.PrimerIndetify import choiceNumber, capture


class Performer(Thread):
    """
    Esta classe implementa threads para utilizar mais núcleos
    """
    MAX_VALUE = 0

    def __init__(self, init: int = 0, count: int or list[int] = 0, path: str = '') -> None:
        super().__init__()
        self.__max: int = 0
        self.count = count
        self.path = path
        self.init = init
        self.max__ = 0

    @property
    def max(self):
        return self.__max

    @max.setter
    def max(self, value):
        self.__max = value

    @classmethod
    def max_v(cls, value):
        if value > cls.MAX_VALUE:
            cls.MAX_VALUE = value
            # print(f"VALOR MÁXIMO ENCONTRADO: {cls.MAX_VALUE}")
        return cls.MAX_VALUE

    # override
    def run(self) -> int:
        # self.teste = str(self.max)
        # Performer.max_v(self.openDir())
        capture(self.openDir())
        # print("AQUI ", self.max)

    def openDir(self) -> list:
        """
        abre o diretorio e subdiretorios em busca de arquivos txt
        :return:
        """
        response: int = 1
        for_read: list[str] = os.listdir(self.path)
        os.chdir(self.path)
        path_bar: str
        NAME: str = ""
        if platform.system() == 'Linux':
            path_bar = '/'
        else:
            path_bar = '\\'
        ways: list[str] = [self.path + path_bar + files for files in for_read[self.init:]]
        print("ANALISANDO: ")
        for path in ways:
            # content = glob(path + "/*/*/*/", recursive=True)
            print(path)
            content = [dir[0] for dir in os.walk(path)]
            for c in content:
                hit = [file for file in os.listdir(c) if 'txt' in os.path.splitext(file)[1]]
                if len(hit) > 0:
                    os.chdir(c)
                    for name_file in hit:
                        print("NAME: ",c + name_file)
                        with open(c + "\\" + name_file) as f:
                            try:
                                finder = f.read().split(',')
                            except Exception as e:
                                ...
                            else:
                                for itens in finder:
                                   response = choiceNumber(itens)
                                   # print(response)
                                   if response > self.max:
                                       NAME = name_file
                                       self.max = response
        return [self.max, NAME]
