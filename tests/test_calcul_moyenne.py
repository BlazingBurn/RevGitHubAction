from .. import mon_module
# from mon_module import calculer_moyenne

def test_calcul_moyenne():
    assert calculer_moyenne([1, 2, 3, 4, 5]) == 3
    assert calculer_moyenne([10, 20, 30, 40, 50]) == 30
    assert calculer_moyenne([]) == 0  # Cas où la liste est vide
    assert calculer_moyenne([5]) == 5  # Cas où il y a une seule valeur dans la liste
