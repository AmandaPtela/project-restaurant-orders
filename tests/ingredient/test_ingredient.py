from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ovo_cozido = Ingredient('ovo')
    ovo_frito = Ingredient('ovo')
    salmao = Ingredient('salmão')
    bacon = Ingredient('bacon')

    # print(ovo.__hash__)

    assert ovo_cozido.__hash__() == ovo_frito.__hash__()
    assert ovo_cozido == salmao
    assert ovo_cozido.__hash__() != bacon.__hash__()

    assert salmao.__repr__() == "Ingredient('salmão')"

    assert bacon.name == 'bacon'
    assert bacon.restrictions == {
        Restriction.ANIMAL_DERIVED, Restriction.ANIMAL_MEAT
        }
