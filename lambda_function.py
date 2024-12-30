import json
from core import run_llm

def lambda_handler(event, context):
    """
    AWS Lambda démarre ici.
    La variable event contient les données entrantes (par ex. la question de l'utilisateur).
    """
    # Vérifiez que le corps de la requête est présent et tentez de le décoder
    try:
        body = json.loads(event.get("body", "{}"))  # Extraire et analyser le corps JSON
        question = body.get("question", "Bonjour, y a-t-il une question ?")
        username = body.get("username", "Virginie")
    except json.JSONDecodeError:
        question = "Bonjour, y a-t-il une question ?"  # Valeur par défaut en cas d'erreur

    # On appelle notre logique LLM
    answer = run_llm(question, username)

    # On retourne la réponse avec l'en-tête Content-Type approprié
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"answer": answer})
    }
