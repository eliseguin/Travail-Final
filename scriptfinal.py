#coding:utf-8

#on importe les modules nécessaires pour faire le travail, dont le beautiful soup

import csv
import requests
from bs4 import BeautifulSoup

url="http://www.gatineau.ca/upload/donneesouvertes/travaux_routiers.xml"

# J'ai pris le site web des données ouvertes de la Ville de Gatineau qui présente les travaux routiers

#Je donne mon identité
entetes={
    "User-Agent":"Elizabeth Seguin",
    "From":"eliseguin@sympatico.ca"
}
#importation des derniers modules
contenu=requests.get(url, headers=entetes)

page=BeautifulSoup(contenu.text,"html.parser")

# print(page) 
# ça fonctionne, j'ai importé correctement mes modules et je peux lire le html de mon lien url.

# Ici, je peux trouver le contenu en cherchant tout ce qui correspond à "item", qui contient en fait toutes les informations que je cherche.

# print(page.find_all("item"))

# Je crée une première boucle

# for ligne in page.find_all("item"):
    # print(ligne.titre_frca)
    
    #ça, c'était pour si je voulais avoir que le titre du travail en cours sur les routes. Je n'ai pas la position de ces travaux. 
    # allons donc trouver ces positions. Voici pour les longitudes : 

# for ligne in page.find_all("item"):
    # print(ligne.longitude)
    
# Voici pour les latitudes :

# for ligne in page.find_all("item"):
    # print(ligne.latitude)
    
# Dans le fond, ce que j'aimerais, c'est créer une boucle qui me donne la position de l'endroit où il y a des travaux et la description 
# qui explique ce qui se passe à cette position précise. 


for ligne in page.find_all("item"):
    print(ligne.titre_frca)
    print(ligne.longitude)
    print(ligne.latitude)
    print(ligne.date_de_debut_des_travaux)
    print(ligne.date_de_fin_des_travaux)
