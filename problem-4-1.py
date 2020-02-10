from bs4 import BeautifulSoup
import requests


def scrapeLogo():
    page = requests.get("https://theinternship.io/")
    logo_list = []
    soup = BeautifulSoup(page.content, 'html.parser')
    all_partner = soup.find_all(class_='partner')
    data = []
    for partner in all_partner:
        description = partner.find(class_='list-company').text
        logo = partner.find('img', class_='center-logos')
        logo_name = logo['src']
        logo_list.append( (len(description), logo_name, description) )
    return logo_list

logo_list = scrapeLogo()
logo_list.sort()
new_logo_list = []
for i in range( len(logo_list) ):
    new_logo_list.append( logo_list[i][1] )
    print(logo_list[i][1])
