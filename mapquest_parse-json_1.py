import urllib.parse
import requests

main_api = "http://www.mapquestapi.com/directions/v2/route?";
orig = "Bogotá, Colombia";
dest = "Arauca, Colombia";
key = "pAXPZMssSGEm4bvGQaSUOTPMjBeWh6W5";

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest});

json_data = requests.get(url).json();
print(json_data);