# Initialisation des variables
montant_initial = 10000  # Montant initial de l'investissement en euros
taux_rendement = 5      # Taux de rendement annuel en pourcentage

# Fonction pour calculer le gain annuel
def calcul_gain(montant, taux):
    return montant * taux / 100

# Affichage du gain annuel initial
gain_annuel = calcul_gain(montant_initial, taux_rendement)
print(f"Gain annuel initial: {gain_annuel} euros")

# Augmenter le capital de 5 000 euros et augmenter le taux de 2%
montant_initial += 5000
taux_rendement += 2

# Calcul du gain annuel après augmentation du capital
gain_annuel_ajuste = calcul_gain(montant_initial, taux_rendement)
print(f"Gain annuel après augmentation du capital: {gain_annuel_ajuste} euros")

# L'investisseur retire 10% du montant total
montant_initial -= montant_initial * 0.10

# Le taux de rendement diminue de 1% suite au retrait
taux_rendement -= 1

# Calcul du gain annuel après retrait et réduction du taux
gain_annuel_final = calcul_gain(montant_initial, taux_rendement)
print(f"Gain annuel après retrait de 10% et réduction du taux de rendement: {gain_annuel_final} euros")
