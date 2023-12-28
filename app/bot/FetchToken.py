import json

def fetch_tg_api():
    with open('./secret.json', 'r') as json_file:
        return json.load(json_file)['telegram_api'] 
    
