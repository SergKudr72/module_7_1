from pprint import pprint

class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop(Product):

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        list_products = file.read()
        file.close()
        return list_products

    def add(self, *products):
        list_products = self.get_products()
        print(f'{list_products}')
        for product in products:
            # if str(product) in list_products:
            #     print (f'Продукт {product} уже есть в магазине')
            # else:
            #     file = open(self.__file_name, 'a')
            #     file.write(f'{product}\n')
            #     file.close()
    # Проверка преподавателя и рекомендации:
# Сделали хорошо, но только в add открытие файла переместите до цикла, а закрытие - после.
# Не слишком эффективно по операциям на каждой итерации открывать-закрывать файл. Это недешевое дело,
# если масштабировать.
    # Работа над ошибками:
            if str(product) not in list_products:
                file = open(self.__file_name, 'a')
                file.write(f'{product}\n')
                file.close()
            else:
                print (f'Продукт {product} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
