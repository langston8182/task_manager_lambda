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
        'Il faut préparer le dossier pour Lissandro' → responsable = 'Lissandro'
        Donnez uniquement le nom du responsable.
        """
    )
    type: str = Field(
        description="Type d'action à effectuer : ajouter, modifier, supprimer, consulter"
    )
    is_task: bool = Field(
        description="Indique si la requête de l'utilisateur correspond à une tâche ou non, true si ca correspond à une tâche, false sinon"
    )
