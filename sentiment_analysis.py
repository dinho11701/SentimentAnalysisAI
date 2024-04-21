import requests


def sentiment_analyzer(text_to_analyse):
    """
    Analyse le sentiment d'une chaîne de caractères en utilisant un service d'API externe.

    Cette fonction envoie le texte donné à une API de traitement du langage naturel, qui utilise
    un modèle BERT pour prédire le sentiment. Elle nécessite un accès à internet pour envoyer la
    requête au service d'API distant.

    Args:
        text_to_analyse (str): Le texte à analyser pour le sentiment.

    Returns:
        str: La réponse du service d'API sous forme de chaîne de caractères. La réponse est typiquement
             une structure de données JSON sous forme de texte qui décrit le sentiment du texte analysé.
             Le format précis de cette réponse dépend de l'API spécifique utilisée.

    Raises:
        requests.exceptions.HTTPError: Une erreur est levée si la requête HTTP vers l'API échoue.
        requests.exceptions.ConnectionError: Une erreur est levée si la connexion au service d'API échoue.
        requests.exceptions.Timeout: Une erreur est levée si la requête dépasse le délai maximum autorisé.

    Exemple:
        >>> result = sentiment_analyzer("J'adore utiliser cette nouvelle technologie!")
        >>> print(result)
        '{"sentiment_analysis": {"score":0.95, "label":"positive"}}'
    """

    # URL de l'API d'analyse de sentiment basée sur le modèle BERT
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Données à envoyer à l'API encapsulées dans un dictionnaire
    myobj = {"raw_document": {"text": text_to_analyse}}

    # En-têtes HTTP requis par l'API
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Envoi de la requête POST et récupération de la réponse
    response = requests.post(url, json=myobj, headers=header)

    # Retourne le contenu de la réponse
    return response.text
