import json
import urllib.request

URL = "https://restcountries.com/v3.1/all"


def get_country_info(country_name):
    """
    Gets information from website from REST Countries
    """

    try:
        with urllib.request.urlopen(URL + country_name) as response:
            data = response.read()
            json_data = json.loads(data)
            country_data = json_data[0] # Got help for this specific part
            country_info = {
                "Name" : country_data.get("name", {}).get("common", "N/A"),
                'Capital' : country_data.get("capital", ["N/A"])[0],
                "Population": country_data.get("population", "N/A"),
                "Area": country_data.get("area", "N/A")

            }
            return country_info
    except urllib.error.URLError as e:
        print(f"Error fetching data from URL: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing Json data: {e}")

