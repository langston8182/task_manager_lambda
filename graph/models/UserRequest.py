from pydantic.v1 import BaseModel, Field


class UserRequest(BaseModel):
    """
    Récupère la personne a qui la tâche est confiée et quelle est le type d'action à réaliser.
    Spécifie si la requête de l'utilisateur correspond à une tâche ou non.
    """

    responsable: str = Field(
        description="""
        Vous recevez une requête utilisateur décrivant une tâche.
        Règles d'extraction :

        Si la phrase est formulée à la première personne (commence par 'je' ou 'j''), le responsable de la tâche est l'utilisateur connecté.
        Sinon, identifiez la personne mentionnée après le mot 'pour'.
        Exemple :
        'Je dois aller chez le dentiste pour Aurore' → responsable = utilisateur connecté
        'Créer une tâche intitulée "Faire les devoirs de Lissandro" pour Cyril' → responsable = Cyril
        'Il faut préparer le dossier pour Lissandro' → responsable = pas de responsable, donc utilisateur connecté par défaut
        Donnez uniquement le nom du responsable.
        """
    )
    type: str = Field(
        description="Type d'action à effectuer : ajouter, modifier, supprimer, consulter"
    )
    is_task: bool = Field(
        description="""
    Indique si la requête utilisateur correspond à une action liée aux tâches (ajout, suppression, consultation, modification).
    Répondre `true` pour toute requête en rapport avec des tâches, même sous forme de question comme "Quelles sont mes tâches ?".
    Répondre `false` si la requête ne concerne pas les tâches (ex: météo, cuisine, ou hors-sujet).
    exemple : Quelles sont mes tâches ? → is_task = true
    exemple : Quel temps fait-il aujourd'hui ? → is_task = false
    """
    )
