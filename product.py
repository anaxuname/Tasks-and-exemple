"""
Создать класс Product c полями: название, цена
Добавить миксин, который приносил бы метод get_discounted_price и получал бы значение скидки (0-100)
Создать StoreProduct на основе Product, миксина который бы вы возвращал цену со скидкой
"""

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class PriceMixin:

    def get_discounted_price(self, discount):
        if discount < 0 or discount > 100:
            raise  ValueError("Не корректно задан процент")
        return self.price - self.price / 100 * discount

class StoreProduct(Product, PriceMixin):
    pass


p = StoreProduct("Mouse", 250)

print(p.get_discounted_price(10))