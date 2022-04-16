import multiprocessing


class ShareToLoad:
    """
    Divide os dados para a quantidades de cpu
    """
    def __init__(self, **kwargs) -> None:
        self.__data_length: int = kwargs['data']
        self.__cpu_count: int = kwargs['cpu']

    @property
    def dataLength(self) -> int: return self.__data_length

    @property
    def cpuCount(self) -> int: return self.__cpu_count

    def breakData(self) -> list[int] or int:
        """
        Faz a divisão
        :return:
        """
        if self.dataLength % self.cpuCount == 0: return self.dataLength / self.cpuCount
        resto: int = self.dataLength % self.cpuCount
        first_cpu: int = resto + (self.dataLength // self.cpuCount)  # o ideal era colocar no núcleo oscioso
        others_cpu: int = self.dataLength // self.cpuCount
        return [first_cpu, others_cpu]
