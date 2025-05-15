# import json, csv
# 
# def getData():
#     with open("33_country_codes.json", "r") as file:
#         data = json.load(file)
#         print(data)
#         
# getData()
# 
# def saveCSV():
#     pass


codes = {"country": [
          {
              "countryCode": "AD",
              "countryName": "Andorra",
              "continentName": "Europe"
          },
          {
              "countryCode": "AE",
              "countryName": "United Arab Emirates",
              "continentName": "Asia"
          },
          {
              "countryCode": "AF",
              "countryName": "Afghanistan",
              "continentName": "Asia"
          }
          ]
         }

codes_list = []
countries = []
continents = []

print(codes["country"][0]["countryName"])

for country in codes["country"]:
    codes_list.append(country["countryCode"])
    countries.append(country["countryName"])
    continents.append(country["continentName"])

print("Country Codes:", codes_list)
print("Countries:", countries)
print("Continents:", continents)