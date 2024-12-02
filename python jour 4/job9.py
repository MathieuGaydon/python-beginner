def moyenne(num1,num2,num3) :
    x=(num1+num2+num3)/3 
    if 15<=x<20 :
        print("Très bon élève")
    elif 11<=x<14 :
        print("Bon élève")
    elif 8<=x<10 :
        print("Élève moyen")
    else :
        print("Élève devant faire des efforts")
num1=int(input("saisir la première note"))
num2=int(input("saisir la deuxième note"))
num3=int(input("saisir la troisième note"))
moyenne(num1,num2,num3)
