__VERSION__ = 1.0.0
__AUTHORS__ = "Ex4c && NICEA"

"""
CREATED TO INSULT PEOPLE, DON'T BE SHY, GET INSULT LIKE A MAN
 \%\     {PEW PEW}
 (0-0) /                           [---------------]
 \_ _==={}  ->     ->       ->     [---------------]
 / \                               [------YOU------]
                                   [---------------]


"""



import requests
import json


#===============| Basic Vars |===============#
url = "https://insult.mattbas.org/api/"
key = ""
token_ssl = False
user = ""
pass = ""


#===============| Front End |===============#
def create_menu():
  print('------------------')
  print('|INSULT GENERATOR|')
  print('------------------')
  print('Choose Option:')
  print('1. INSULT ME.\n2. INSULT ME LIKE BIATCH\n3. Exit:')
  user_menu_input = input('\n\m:>')
  if user_menu_input < 3:
    user = input("Provide username(default:NONE")
    pass = input("Provide password(default:NONE")
  level_of_insult = 1
  return user_menu_input, level_of_insult*3;

#===============| BACK END |===============#
def obtain_request(url,key,token_ssl):
  requests.get(url,auth=(user, pass) token_ssl)

def generate_insult(user_input,level_of_insult):
  level_of_insult = level_of_insult*user_input
  insults_output = []
  for x in level_of_insult:
    api_request_reponse = obtain_request(url,key,token_ssl)
    json_output = json.load(api_requests_response.json())
    insult = json_output.get('insult')
    insults_output.add(insult)
    print(insult)
  return insults_output



#>>>>>===============| MAIN |===============<<<<<#

user_input, level_of_insult = create_menu()
if user_input < 3:
  generate_insult(user_input,level_of_insult)


