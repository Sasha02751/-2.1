import doctest

class Cafeteria:
    """
    Абстрактный класс, описывающий столовую.
    """

    def __init__(self, name: str, capacity: int):
        if capacity <= 0:
            raise ValueError("Вместимость столовой должна быть больше нуля.")
        self.name = name
        self.capacity = capacity

    def order_food(self, food_item: str) -> None:
        """
        Заказать еду в столовой.
        Args:
        food_item (str): Название блюда.
        Returns:
        None
        Пример использования:
       cafeteria.order_food("Паста карбонара")
        """
        pass

    def pay_bill(self, amount: float) -> None:
        """
         Оплатить счет за еду.
         Args:
        amount (float): Сумма к оплате.
        Returns:
        None
        Пример использования:
        cafeteria.pay_bill(500.0)
        """
        pass

    def leave_review(self, review_text: str) -> None:
        """
        Оставить отзыв о столовой.
    Args:
        review_text (str): Текст отзыва.
    Returns:
        None
    Пример использования:
     cafeteria.leave_review("Отличное обслуживание и вкусная еда!")
        """
        pass

if __name__ == "__main__":
    doctest.testmod()