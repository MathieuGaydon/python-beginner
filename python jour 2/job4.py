N = int(input('Entrer un nombre entier supérieur à 0: '))
if N <= 0:
    print("Le nombre doit être supérieur à 0.")
else:
    for i in range(1, N + 1):
        print(f"Table de multiplication de {i}:")
        for count in range(1, 11):
            product = i * count
            print(f"{i} * {count} = {product}")
        print()
