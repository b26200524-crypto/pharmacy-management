"""
Module de gestion du stock de médicaments.
Gère la lecture et l'écriture dans le fichier CSV.
"""

import csv
import os
from models.medicament import Medicament


# Constante : chemin du fichier de données
FICHIER_STOCK: str = "data/medicaments.csv"


def charger_stock() -> list:
    """
    Charge les médicaments depuis le fichier CSV.

    Returns:
        Liste d'objets Medicament.
    """
    medicaments = []

    # Crée le fichier s'il n'existe pas encore
    if not os.path.exists(FICHIER_STOCK):
        return medicaments

    with open(FICHIER_STOCK, "r", encoding="utf-8") as fichier:
        lecteur = csv.reader(fichier)
        for ligne in lecteur:
            if len(ligne) == 5:  # nom, prix, quantite, date_exp, categorie
                nom, prix, quantite, date_exp, categorie = ligne
                med = Medicament(nom, float(prix), int(quantite), date_exp, categorie)
                medicaments.append(med)

    return medicaments


def sauvegarder_stock(medicaments: list) -> None:
    """
    Sauvegarde la liste des médicaments dans le fichier CSV.

    Args:
        medicaments: Liste d'objets Medicament à sauvegarder.
    """
    with open(FICHIER_STOCK, "w", encoding="utf-8", newline="") as fichier:
        for med in medicaments:
            fichier.write(med.vers_csv() + "\n")


def afficher_stock(medicaments: list) -> None:
    """
    Affiche tous les médicaments du stock.

    Args:
        medicaments: Liste des médicaments à afficher.
    """
    if not medicaments:
        print("⚠️  Stock is empty.")
        return

    print("\n" + "=" * 45)
    print("         📦 Medecine stock")
    print("=" * 45)

    for med in medicaments:
        med.afficher()

    print("=" * 45)


def afficher_alertes(medicaments: list) -> None:
    """
    Affiche les alertes de stock bas et de médicaments expirés.

    Args:
        medicaments: Liste des médicaments à vérifier.
    """
    alertes = False

    print("\n🔔 ALERTS :")
    for med in medicaments:
        if med.est_expire():
            print(f"  ⚠️  {med.nom} est EXPIRÉ !")
            alertes = True
        elif med.stock_bas():
            print(f"  🔴 {med.nom} : stock bas ({med.get_quantite()} unités restantes)")
            alertes = True

    if not alertes:
        print("  ✅ No alets. Everything is fine.")


def rechercher_medicament(medicaments: list, nom: str):
    """
    Recherche un médicament par son nom.

    Args:
        medicaments: Liste des médicaments.
        nom: Nom à rechercher.

    Returns:
        L'objet Medicament trouvé ou None.
    """
    for med in medicaments:
        if med.nom.lower() == nom.lower():
            return med
    return None
