import urllib.parse
import requests

main_api = "http://www.mapquestapi.com/directions/v2/route?";
#orig = "Bogotá, Colombia";
#dest = "Arauca, Colombia";
key = "pAXPZMssSGEm4bvGQaSUOTPMjBeWh6W5";

while True:
    orig = input("Starting Location: ");
    if orig == "quit" or orig == "q":
        break;
    if dest == "quit" or dest == "q":
        break;

    dest = input("Destination: ");
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest});
    print("URL: " + (url));
    json_data = requests.get(url).json();
    json_status = json_data["info"]["statuscode"];
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n");
