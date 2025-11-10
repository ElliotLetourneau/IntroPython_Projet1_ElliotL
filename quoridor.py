#________________________________________interpréter_la_ligne_de_commande________________________________________

import argparse


def interpréter_la_ligne_de_commande():
    """Génère un interpréteur de ligne de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par parser.parse_args().
                   Cet objet aura l'attribut «idul» représentant l'idul du joueur.
    """
    # Création du parseur avec une description
    parser = argparse.ArgumentParser(
        description="Quoridor"
    )

    # Ajout de l'argument positionnel « idul »
    parser.add_argument(
        "idul",
        help="IDUL du joueur"
    )

    # Retourne le résultat de l'analyse de la ligne de commande
    return parser.parse_args()

#________________________________________formater_entête________________________________________

def formater_entête(joueurs):
    # Trouver la longueur maximale du nom pour aligner "murs="
    longueur_max_nom = max(len(joueur["nom"]) for joueur in joueurs)

    # Construire la légende ligne par ligne
    lignes = ["Légende:"]
    for i, joueur in enumerate(joueurs, start=1):
        nom = joueur["nom"]
        murs = "|" * joueur["murs"]
        # Ajuster les espaces pour aligner le mot "murs"
        espaces = " " * (longueur_max_nom - len(nom))
        lignes.append(f"   {i}={nom},{espaces} murs={murs}")

    # Joindre toutes les lignes avec des retours à la ligne
    return "\n".join(lignes)

#________________________________________formater_le_damier________________________________________

def formater_le_damier(joueurs, murs):
    """Formater la représentation graphique du damier.

    Args:
        joueurs (list): Liste de dictionnaires représentant les joueurs.
        murs (dict): Dictionnaire représentant l'emplacement des murs.

    Returns:
        str: Chaîne de caractères représentant le damier.
    """
    pass

#________________________________________formater_le_jeu________________________________________

def formater_le_jeu(état):
    """Formater la représentation graphique d'un jeu.

    Doit faire usage des fonctions formater_entête et formater_le_damier.

    Args:
        état (dict): Dictionnaire représentant l'état du jeu.

    Returns:
        str: Chaîne de caractères représentant le jeu.
    """
    pass

#________________________________________sélectionner_un_coup________________________________________

def sélectionner_un_coup():
    """Sélectionner un coup

    Returns:
        tuple: Un tuple composé d'un type de coup et de la position.
               Le type de coup est une chaîne de caractères.
               La position est une liste de 2 entiers [x, y].
    Examples:
        Quel coup voulez-vous jouer? ('D', 'MH', 'MV') : D
        Donnez la position du coup à jouer ('x, y') : 2, 6
    """
    pass