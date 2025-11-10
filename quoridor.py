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
    murs_h = murs["horizontaux"]
    murs_v = murs["verticaux"]

    # Entête du damier
    damier = "   -----------------------------------\n"

    # Création de la grille de base
    grille = [["." for _ in range(9)] for _ in range(9)]

    # Placement des joueurs
    for i, joueur in enumerate(joueurs, start=1):
        x, y = joueur["position"]
        grille[9 - y][x - 1] = str(i)

    # Construction du damier ligne par ligne
    for y in range(9, 0, -1):
        # Ligne avec les points (joueurs inclus)
        damier += f"{y} | " + "   ".join(grille[9 - y]) + " |\n"

        # Ligne avec les murs horizontaux ou verticaux
        if y > 1:
            ligne_mur = "  |"
            for x in range(1, 10):
                # Mur horizontal
                ligne_mur += "-------" if [x, y - 1] in murs_h else "   "
                # Mur vertical
                if [x, y - 1] in murs_v:
                    ligne_mur = ligne_mur[:-3] + "|"
            ligne_mur += "\n"
            damier += ligne_mur

    # Pied du damier
    damier += "--|-----------------------------------\n"
    damier += "  | 1   2   3   4   5   6   7   8   9"

    return damier

#________________________________________formater_le_jeu________________________________________

def formater_le_jeu(état):
    # Récupérer les informations de base
    joueurs = état["joueurs"]
    murs_h = état["murs"]["horizontaux"]
    murs_v = état["murs"]["verticaux"]

    # Construire la légende
    res = "Légende:\n"
    res += f"   1={joueurs[0]['nom']},  murs={'|' * joueurs[0]['murs']}\n"
    res += f"   2={joueurs[1]['nom']}, murs={'|' * joueurs[1]['murs']}\n"
    res += "   -----------------------------------\n"

    # Grille vide initiale : 9x9
    grille = [["." for _ in range(9)] for _ in range(9)]

    # Placer les joueurs
    for i, j in enumerate(joueurs, start=1):
        x, y = j["position"]
        grille[9 - y][x - 1] = str(i)

    # Construire les lignes du damier
    lignes = []
    for y in range(9, 0, -1):
        # Ligne de points
        ligne = f"{y} | " + "   ".join(grille[9 - y]) + " |\n"
        lignes.append(ligne)

        # Ligne d'espacement ou de murs horizontaux
        if y > 1:
            sep = "  |"
            for x in range(1, 10):
                # Mur horizontal
                if [x, y - 1] in murs_h:
                    sep += "-------"
                else:
                    sep += "   "
                # Mur vertical
                if [x, y - 1] in murs_v:
                    sep = sep[:-3] + "|"
            sep += "\n"
            lignes.append(sep)

    # Ligne du bas
    lignes.append("--|-----------------------------------\n")
    lignes.append("  | 1   2   3   4   5   6   7   8   9")

    return res + "".join(lignes)

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