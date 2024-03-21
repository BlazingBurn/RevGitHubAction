# a = 2
# print("coucou", a)

from mon_module import calculer_moyenne

def main():
    # Exemple d'utilisation de la fonction calculer_moyenne
    liste = [1, 2, 3, 4, 5]
    moyenne = calculer_moyenne(liste)
    print("La moyenne de la liste est:", moyenne)

if __name__ == "__main__":
    main()
