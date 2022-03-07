import requests

url = ""
key = ""
token_ssl = False

def obtain_request(url,key,token_ssl):
user = input("Provide username(default:NONE")
pass = input("Provide password(default:NONE")
requests.get(url,auth=('user', 'pass') token_ssl)

api_request_reponse = obtain_request(url,key,token_ssl)
