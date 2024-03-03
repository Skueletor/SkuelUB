import json

def load_messages(language):
    try:
        with open(f'langs/{language}.json', 'r', encoding='utf-8') as file:
            messages = json.load(file)
    except FileNotFoundError:
        with open('langs/en.json', 'r', encoding='utf-8') as file:
            messages = json.load(file)
    return messages
