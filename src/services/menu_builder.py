from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        dishes = self.menu_data.dishes
        rest = restriction
        complete_menu = []
        # print(dishes.get_restrictions())

        for dish in dishes:
            avl = self.inventory.check_recipe_availability(dish.recipe)
            if rest not in dish.get_restrictions() and avl == "True":
                complete_menu.append(
                    {
                        "dish_name": dish.name,
                        "ingredients": dish.recipe.keys(),
                        "price": dish.price,
                        "restrictions": dish.get_restrictions()
                    }
                )
            return complete_menu

        return dishes
        # lista de dicionários que contenham as chaves dish_name,
        # ingredients, price e restrictions.
