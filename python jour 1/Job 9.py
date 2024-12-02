# créer l'inventaire
nom="sucre"
prix_sucre=1
quantité_sucre=5
nom2="sel"
prix_sel=1.20
quantité_sel=3
nom3="poivre"
prix_poivre=0.90
quantité_poivre=9

print("Aujourd'hui nous avons : du",nom,"à",prix_sucre,"euros l'unité et il nous en reste",quantité_sucre,";du",nom2,"à",prix_sel,"euros l'unité et il nous en reste",quantité_sel,";du",nom3,"à",prix_poivre,"euros l'unité et il nous en reste",quantité_poivre,",que vous faut-il ?")
# demande de produit sucre
demande=input("quel type de demande ?")
if demande == nom :
    nombre=int(input("quelle nombre ?"))
    if nombre > quantité_sucre :
        print("désolé on en a pas assez")
    elif nombre <= 0 :
        print("soyer sérieux")
    else : 
        print("très bien cela fera ",nombre*prix_sucre,"il ne nous reste plus que",quantité_sucre -nombre)
# demande de produit sel
demande=input("quel type de demande ?")
if demande == nom2 :
    nombre2=int(input("quelle nombre ?"))
    if nombre > quantité_sel :
        print("désolé on en a pas assez")
    elif nombre <= 0 :
        print("soyer sérieux")
    else : 
        print("très bien cela fera ",nombre2*prix_sel,"il ne nous reste plus que",quantité_sel -nombre2)
# demande de produit poivre
demande=input("quel type de demande ?")
if demande == nom3 :
    nombre3=int(input("quelle nombre ?"))
    if nombre > quantité_poivre :
        print("désolé on en a pas assez")
    elif nombre <= 0 :
        print("soyer sérieux")
    else : 
        print("très bien cela fera",nombre3*prix_poivre,"il ne nous reste plus que",quantité_poivre-nombre3)
