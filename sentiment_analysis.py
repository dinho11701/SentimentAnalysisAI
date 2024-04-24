import requests


def sentiment_analyzer(text_to_analyze, api_key):
    url = "https://api.meaningcloud.com/sentiment-2.1"
    payload = {
        'key': api_key,
        'txt': text_to_analyze,
        'lang': 'en',  # or 'es' for Spanish, 'fr' for French, etc.
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error {response.status_code}: {response.text}"


# Remplacez 'your_api_key_here' par votre clé API MeaningCloud.
api_key = '43efd8951e9ad19aa37a57deedc1bd4a'

# Test de la fonction
result = sentiment_analyzer("I love this new technology!", api_key)
print(result)
