"""
Module de gestion des ventes de la pharmacie.
"""

from datetime import datetime
from models.medicament import Medicament
from models.client import Client
from models.pharmacien import Pharmacien


# Constante : chemin du fichier historique
FICHIER_HISTORIQUE: str = "data/historique.txt"


def enregistrer_vente(medicament: Medicament, client: Client,
                      pharmacien: Pharmacien, quantite: int) -> bool:
    """
    Enregistre une vente dans le fichier historique.

    Args:
        medicament: Le médicament vendu.
        client: Le client acheteur.
        pharmacien: Le pharmacien qui effectue la vente.
        quantite: La quantité vendue.

    Returns:
        True si la vente est réussie, False sinon.
    """
    # Vérifier si la vente est possible
    if not medicament.reduire_stock(quantite):
        print(f"❌ Stock insuffisant pour {medicament.nom}.")
        return False

    # Calculer le total
    total: float = medicament.get_prix() * quantite
    date_vente: str = datetime.now().strftime("%d/%m/%Y %H:%M")

    # Dictionnaire utile : résumé de la vente
    achat: dict = {
        "medicament": medicament.nom,
        "quantite": quantite,
        "total": total,
        "date": date_vente
    }

    # Ajouter à l'historique du client
    client.ajouter_achat(achat)

    # Incrémenter le compteur du pharmacien
    pharmacien.enregistrer_vente()

    # Écriture dans le fichier historique
    with open(FICHIER_HISTORIQUE, "a", encoding="utf-8") as fichier:
        ligne = (f"[{date_vente}] | Client : {client} | "
                 f"Médicament : {medicament.nom} | "
                 f"Qté : {quantite} | Total : {total} FCFA | "
                 f"Pharmacien : {pharmacien}\n")
        fichier.write(ligne)

    print(f"\n✅ Vente enregistrée !")
    print(f"   Médicament : {medicament.nom}")
    print(f"   Quantité   : {quantite}")
    print(f"   Total      : {total} FCFA")

    return True


def afficher_historique() -> None:
    """Lit et affiche l'historique complet des ventes depuis le fichier."""
    try:
        with open(FICHIER_HISTORIQUE, "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()

        if not lignes:
            print("Aucune vente enregistrée.")
            return

        print("\n" + "=" * 55)
        print("           📜 HISTORIQUE DES VENTES")
        print("=" * 55)

        for ligne in lignes:
            print(f"  {ligne.strip()}")

        print("=" * 55)
        print(f"  Total : {len(lignes)} vente(s) enregistrée(s).")

    except FileNotFoundError:
        print("Aucun historique disponible.")
