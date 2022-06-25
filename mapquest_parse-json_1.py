import urllib.parse
import requests

main_api = "http://www.mapquestapi.com/directions/v2/route?";
orig = "Washington, D.C.";
dest = "Baltimore, Md";
key = "pAXPZMssSGEm4bvGQaSUOTPMjBeWh6W5";

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest});
