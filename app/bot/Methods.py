import requests

API = 'http://127.0.0.1:8080'

def get_model_answer(prompt: str) -> str:
    try:
        ans = requests.post(API+'/predict', json={'text': prompt}).json()['answer']
        print('Answer:', ans)
        return ans
    except requests.exceptions.ConnectionError:
        return 'Я бы очень хотел поболтать, но сервер немного приболел\U0001F912'
    except requests.exceptions.RequestException:
        return 'Ой, кажется с сервером что-то не так\U0001F61F'
