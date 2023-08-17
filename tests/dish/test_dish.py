import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 2
def test_dish():
    # PAREI AQUI ---- CONTINUAR AQUI
    lasanha = Dish('lasanha', 20.00)
    lasanha.add_ingredient_dependency(
            ingredient=Ingredient("lasanha"),
            amount=100)
    lasanha.get_restrictions()
    miojo = Dish('miojo', 2.00)
    lasanha.recipe = {}
    lasanha.ingredients = None

    # 2.1 - o atributo name de um prato diferente que o passado ao construtor.
    assert lasanha.name == 'lasanha'
    assert lasanha.recipe == {}

    assert lasanha.__hash__() == lasanha.__hash__()

    assert lasanha.__hash__() != miojo.__hash__()

    assert lasanha.__eq__(lasanha)

    assert repr(lasanha) == "Dish('lasanha', R$20.00)"

    lasanha.add_ingredient_dependency(
            ingredient=Ingredient("lasanha"),
            amount=100)

    assert lasanha.get_ingredients() == {Ingredient('lasanha')}
    assert len(lasanha.get_ingredients()) == len(lasanha.get_ingredients())

    assert lasanha.get_restrictions() == set()

    message = "Dish price must be float."
    with pytest.raises(TypeError, match=message):
        Dish("Nome do Prato", "20.00")

    message = "Dish price must be greater then zero."
    with pytest.raises(ValueError, match=message):
        Dish("Arroz doce", -10)

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Nome do Prato", "20.00")

    message = "Dish price must be greater then zero."
    with pytest.raises(ValueError, match=message):
        Dish("Beiju", 0)

    print('HASH LASANHA', lasanha.add_ingredient_dependency(
            ingredient=Ingredient("lasanha"),
            amount=100))
    print('INGREDIENT ADD', lasanha.get_ingredients())
