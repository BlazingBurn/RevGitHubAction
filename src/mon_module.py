def calculer_moyenne(liste):
    if not liste:
        return 0  # Retourne 0 si la liste est vide pour éviter une division par zéro
    return sum(liste) / len(liste)