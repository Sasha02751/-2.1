import doctest

class Smartphone:
    """
    Абстрактный класс, описывающий смартфон.
    """

    def __init__(self, brand: str, price: float):
        if price <= 0:
            raise ValueError("Цена должна быть больше нуля.")
        self.brand = brand
        self.price = price

    def play_music(self, song_title: str) -> None:
        """
        Воспроизвести музыку.
    Args:
        song_title (str): Название песни для проигрывания.
    Returns:
        None
    Пример использования:
     headphones.play_music("Bohemian Rhapsody")
        """
        pass

    def adjust_volume(self, level: int) -> None:
        """
         Изменить громкость.
    Args:
        level (int): Уровень громкости (от 0 до 100).
    Returns:
        None
    Пример использования:
     headphones.adjust_volume(75)
        """
        pass

    def answer_call(self) -> None:
        """
         Ответить на звонок.
    Returns:
        None
    Пример использования:
     headphones.answer_call()
        """
        pass

if __name__ == "__main__":
    doctest.testmod()