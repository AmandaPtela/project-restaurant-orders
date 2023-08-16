# Req 3 - menu builder
# source_path = caminho do arquivo menu_data
from models.dish import Dish
from models.ingredient import Ingredient
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.path = source_path
        self.dishes = self.dishes(source_path)

    def dishes(self, path):
        dishes = dict()
        with open(path, 'r') as csvv:
            arquivo = csv.DictReader(csvv)  # lê

            for linha in arquivo:
                name = linha["dish"]
                price = linha["price"]
                ing = linha["ingredient"]
                amount = linha["recipe_amount"]

                price_numb = float(price)
                ingredient = Ingredient(ing)

                if name not in dishes:
                    # cria o prato
                    dishes[name] = Dish(name, price_numb)
                # adiciona os ingredientes
                dishes[name].add_ingredient_dependency(
                    ingredient, int(amount))
                # retorna valores do dicionário
                print(dishes.keys())
        return set(dishes.values())
    """
new = MenuData("data/menu_base_data.csv")
print(new) """
