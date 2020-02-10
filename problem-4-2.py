from bs4 import BeautifulSoup
from flask import Flask
from flask_restful import Resource, Api
import requests

# SCPARPING PART

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

logo_list = new_logo_list

#EDIT logo TO "https://theinternship.io/....."
#AND CREATE DICT OF COMPANIES

for i in range( len(logo_list) ):
    logo_list[i] = "https://theinternship.io/" + logo_list[i]
logo_map_list = []
for i in range( len(logo_list) ):
    logo_map = {"logo" : logo_list[i]}
    logo_map_list.append(logo_map)
companies = {"companies" : logo_map_list}

# BUILD API PART
app = Flask(__name__)
api = Api(app)

class MyApi(Resource):
    
    def __init__(self):
        pass

    def get(self):
        return companies 

api.add_resource(MyApi, '/companies')

if __name__ == "__main__":
    app.run(debug=True)
