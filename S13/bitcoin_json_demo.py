import pprint
data = {
    {'time': {'updated': 'Oct 9, 2024 15:03:58 UTC', 'updatedISO': '2024-10-09T15:03:58+00:00', 'updateduk': 'Oct 9, 2024 at 16:03 BST'}, 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org', 'chartName': 'Bitcoin', 'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '61,832.807', 'description': 'United States Dollar', 'rate_float': 61832.8067}, 'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '47,292.266', 'description': 'British Pound Sterling', 'rate_float': 47292.2657}, 'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '56,450.323', 'description': 'Euro', 'rate_float': 56450.3227}}}
}

# Find the current bitcoin price in USD
# pprint.pprint

# print(type(data))
# print(data.keys())
# pprint.pprint(data["bpi"])

bpi = data["bpi"]
# print(type(bpi))
# print(bpi.keys())

pprint.pprint(bpi["USD"])

print(data["bpi"]["USD"]["rate"])