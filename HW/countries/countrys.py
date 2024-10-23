import json
import urllib.request
import random

#URL = "https://restcountries.com/v3.1/name/{country_name}"


def get_country_info(country_name):
    """
    Gets information from website from REST Countries
    """
    URL = f"https://restcountries.com/v3.1/name/{country_name}" 

    try:
        with urllib.request.urlopen(URL) as response: 
            data = response.read()
            json_data = json.loads(data)
            
           
        if len(json_data) > 0:
            country_data = json_data[0]

            country_info = {
                "Name" : country_data.get("name", {}).get("common", "N/A"),
                'Capital' : country_data.get("capital", ["N/A"])[0],
                "Population": country_data.get("population", "N/A"),
                "Area": country_data.get("area", "N/A")
            }
            return country_info
        
        else:
            print("COuntry not found :(")
            return None
    
    except urllib.error.URLError as e:
        print(f"Error fetching data from URL: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing Json data: {e}")

def get_random_country_info():
    """
    Picks a random REST country and returns facts about said country
    """

    URL = f"https://restcountries.com/v3.1/all"

    try:
        with urllib.request.urlopen(URL) as response: 
            data = response.read()
            json_data = json.loads(data)
            random_country = random.choice(json_data)
           
            country_info = {
                "Name" : random_country.get("name", {}).get("common", "N/A"),
                'Capital' : random_country.get("capital", ["N/A"])[0],
                "Population": random_country.get("population", "N/A"),
                "Area": random_country.get("area", "N/A")
            }
            return country_info
        
    except urllib.error.URLError as e:
        print(f"Error fetching data from URL: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing Json data: {e}")



# def main():
#     country_name = input("Enter Country Name: ")

#     if country_name.lower() == "random":
#         country_info = get_random_country_info()
#     else:
#         country_info = get_country_info(country_name)

#     print(country_info)

def main():
    country_name = input("Enter Country Name: ")

    if country_name.lower() == "random":
        country_info = get_random_country_info()
    else:
        country_info = get_country_info(country_name)

    print(country_info)


main()
        



   
