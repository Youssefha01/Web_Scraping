import re
import requests
from bs4 import BeautifulSoup
import csv


def get_page():
    url=[]
    nbr=1
    for i in range(194):
        i=f"https://www.wandaloo.com/occasion/?pg={nbr}"
        nbr+=1
        url.append(i)
    return url

def parse_cars(urls, writer):
    r = requests.get(urls)
    soup = BeautifulSoup(r.content, "html.parser")
    cars = soup.find_all('li', class_=lambda x: x in ('odd', 'even'))

    for car in cars:
        nom = car.find('p', class_="titre").text.strip()
        prix = car.find('p', class_="prix").text.strip()
        ul_tag = car.find("ul", class_="detail")
        if ul_tag:
            carburant = ul_tag.find_all("li")[0].text.strip()
            Model = ul_tag.find_all("li")[1].text.strip()
            CV = ul_tag.find_all("li")[2].text.strip()
            KM = ul_tag.find_all("li")[3].text.strip()
        ville = car.find("span", class_="city").text.strip()
        
        writer.writerow({'Nom': nom, 'Prix': prix, 'Carburant': carburant, 'Modèle': Model, 'CV': CV, 'KM': KM, 'Ville': ville})

def parse_all():
    with open('cars_data.csv', mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Nom', 'Prix', 'Carburant', 'Modèle', 'CV', 'KM', 'Ville']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        pages = get_page()
        for page in pages:
            parse_cars(page, writer)
            print(f"Scraping {page}")

parse_all()
