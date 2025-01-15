import doctest

class Ship:
    """
    Абстрактный класс, описывающий корабль.
    """

    def __init__(self, name: str, max_cargo_capacity: float):
        if max_cargo_capacity <= 0:
            raise ValueError("Максимальная грузоподъемность должна быть больше нуля.")
        self.name = name
        self.max_cargo_capacity = max_cargo_capacity

    def set_sail(self) -> None:
        """
        Поднять паруса и отправиться в плавание.
       Returns:
        None
       Пример использования:
       ship.set_sail()
        """
        pass

    def sail_to_destination(self, destination: str) -> None:
        """
        Плыть к определённому пункту назначения.
    Args:
        destination (str): Название пункта назначения.
    Returns:
        None
    Пример использования:
     ship.sail_to_destination("Treasure Island")
        """
        pass

    def load_cargo(self, cargo: float) -> None:
        """
        Загрузить груз на корабль.
    Args:
        cargo (float): Количество груза для погрузки.
    Returns:
        None
    Пример использования:
     ship.load_cargo(100)
        """
        pass

if __name__ == "__main__":
    doctest.testmod()