__VERSION__ = 1.0.0
__AUTHORS__ = "Ex4c && NICEA"

import requests

url = "https://insult.mattbas.org/api/"
key = ""
token_ssl = False

def obtain_request(url,key,token_ssl):
  user = input("Provide username(default:NONE")
  pass = input("Provide password(default:NONE")
  requests.get(url,auth=($user, $pass) token_ssl)

api_request_reponse = obtain_request(url,key,token_ssl)

def create_menu():
  print('------------------')
  print('|INSULT GENERATOR|')
  print('------------------')
  print('Choose Option:')
  print('1. INSULT ME.\n2. INSULT ME LIKE BIATCH\n3. Exit:')
  
  
