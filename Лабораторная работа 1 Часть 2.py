# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Wood:
    def __init__(self, density: float,  type_wood: str, cut: str):
        """
        Создание и подготовка к работе объекта дерево

        :param density: Плотность дерева
        :param type_wood: Порода дерева
        :param cut: Вид разреза

        Пример:
        >>> wood = Wood(600, "дуб", "радиальный") # инициализация экземпляра класса
        """
        if not(isinstance(density, float) or isinstance(type_wood, str) or isinstance(cut, str)):
            raise TypeError("Неправильно введены данные древесины")
        elif density < 0:
            raise ValueError("Плотность древесины не может быть отрицательным")
        self.density = density
        self.type_wood = type_wood
        self.cut = cut

        def wood_cutting(self):
            """
            Вырезание из дерева

            :return: Вырезанное деерво

            Пример:
            >>> wood = Wood(600, "дуб", "радиальный")
            >>> wood.wood_cutting()
            """
        def burning(self):
            """
            Сжигание дерева

            :return: Пепел)

            Пример:
            >>> wood = Wood(600, "дуб", "радиальный")
            >>> wood.burning()
            """

class Steel:
    def __init__(self, carbon_content: float, weight: float):
        """
        Создание и подготовка к работе объекта "Сталь"

        :param carbon_content: содержание карбона в сплаве
        :param weight: масса стали

        Примеры:
        >>> steel = Steel(2, 200) # инициализация экземпляра класса
        """
        if not (isinstance(carbon_content, (int, float)) or isinstance(weight, (int, float))):
            raise TypeError("Количесвто содержания углерода и масса стали должны быть в int или float ")
        elif carbon_content < 0.06 or weight < 0:
            raise ValueError("Значения меньше минимально возможных")
        self.carbon_content = carbon_content
        self.weight = weight

    def volume_steal(self):
        """
        подсчет объема стали

        :return: Масса стали

        Примеры:
        >>> steel = Steel(2, 200)
        >>> steel.volume_steal()
        """
    def new_alloy(self, carbon_content_sec: float, weight_sec: float):
        """
        Расчет нового сплава при добавлении сплава другого металла

        :param carbon_content_sec: Содержание карбона во втором сплаве
        :param weight_sec: Масса второго сплава

        :raise ValueError Значение углерода во втором слпаве не может быть меньше минимального

        :return: Содержание карбона в новом сплаве

        Пример:
        >>> steel = Steel(2, 200)
        >>> steel.new_alloy(3, 400)
        """

        if not (isinstance(carbon_content_sec, (int, float)) or isinstance(weight_sec, (int, float))):
            raise TypeError("Количесвто содержания углерода и масса второго сплава должны быть в int или float ")
        elif carbon_content_sec < 0.06 or weight_sec < 0:
            raise ValueError("Значения второго сплава меньше минимально возможных")

class Pen:
    def __init__(self, len : float, width: float, color: str):
        """
        Создание и подготовка к работе объекта "Ручка"

        :param len: Длина ручки
        :param width: Ширина ручки
        :param color: Цвет ручки

        Пример:
        >>> pen = Pen(10, 1, "rad")
        """
        if not(isinstance(len or width, float) or isinstance(color, str)):
            raise TypeError("Непривально введены данные")
        if len < 0 or width < 0:
            raise ValueError("Значения длины и ширины не могут быть меньше 0")

        self.len = len
        self.width = width
        self.color = color

    def replace_ink(self, color2: str):
        """
        Замена чернил в ручке

        :param color: Цвет новых чернил

        :return: В ручке заменят чернила
        Пример:
        >>> pen = Pen(10, 2, "rad")
        >>> pen.replace_ink("green")
        """
        if not isinstance(color2, str):
            raise TypeError("Цвет введен в неверном формате")

    def put_cap(self):
        """
        Надеть колпачек на ручку

        :return:Уолпочек находится на ручке

        Пример:
        >>> pen = Pen(10,2, "rad")
        >>> pen.put_cap()
        """

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
