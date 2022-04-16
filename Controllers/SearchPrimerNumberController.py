# import operator
import os
from Datas.FindDataBase import FindDataBase
import multiprocessing
from Controllers.ShareToLoadController import ShareToLoad
from Controllers.PerformerController import Performer
from Controllers.PrimerIndetify import CAPTURE


class SearchPrimerNumberController:
    """
    Classe que pesquisa e abre os arquivos em busca do maior número primo
    """
    def __init__(self) -> None:
        self.__count_main_dir: int = 0
        self.__count_file: int = 0
        self.__max: int = 0
        self.__name_of_file: str = ""
        self.__base_path: FindDataBase = FindDataBase('Users\\Marcu\\Desktop\\AtividadesEmPython\\file')
        self.path: str = self.basePath.findFiles()
        self.T: list = []

    @property
    def countMainDir(self) -> int: return self.__count_main_dir

    @property
    def countFile(self) -> int: return self.__count_file

    @property
    def max(self) -> int: return self.__max

    @property
    def nameOfFile(self) -> str: return self.__name_of_file

    @property
    def basePath(self): return self.__base_path

    def listDirAndShare(self):
        """
        Lista o diretório e divide a quantidade
        :return:
        """
        max_values: list[int] = list()
        threads: list[Performer] = []
        count: int or list[int] = len(os.listdir(path=self.path))
        _cpu_count: int = multiprocessing.cpu_count()
        share_to: ShareToLoad = ShareToLoad(data=count, cpu=_cpu_count)
        if count < _cpu_count:
            [threads.append(Performer(0, m, self.path)) for m in range(count)]
        elif count == _cpu_count:
            [threads.append(Performer(n, self.path)) for n in range(count)]
        else:
            count = share_to.breakData()
            cont: int = 0
            i: int = 0
            print(count)
            xlimit = list(range(count[0], len(os.listdir(self.path))))
            print(xlimit)
            for qnt in range(_cpu_count):
                if cont == 0:
                    threads.append(Performer(0, count[0], self.path))
                    cont += 1
                else:
                    threads.append(Performer(xlimit[i], xlimit[i + 1], self.path))
                    i += 2
        for th in range(len(threads)): threads[th].start()
        for th in threads: th.join()
        print(f"Maior número primo encontrado:: { max(CAPTURE)}")
        return None


if __name__ == '__main__':
    from Controllers.PerformerController import Performer



