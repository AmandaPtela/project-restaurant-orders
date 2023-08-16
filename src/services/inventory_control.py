from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe) -> bool:
        inventory = self.inventory

        # print(inventory)
        for ingredient, amount in recipe.items():

            if ingredient not in inventory:
                # Print('INGREDIENTE', ingredient)
                # Print('INVENTORY', inventory)
                return False

            if amount > inventory[ingredient]:
                # Print(amount)
                return False

        return True

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        avl = self.check_recipe_availability(recipe)
        recipes = recipe.keys()
        inventory = self.inventory

        # Print(avl)
        if avl:

            for ingredient in recipes:
                # Print(inventory[ingredient], recipe[ingredient])
                inventory[ingredient] -= recipe[ingredient]
                # Print(inventory[ingredient], recipe[ingredient])
        else:
            raise ValueError("Receita indisponível")
