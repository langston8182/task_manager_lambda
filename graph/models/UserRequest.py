from pydantic.v1 import BaseModel, Field


class UserRequest(BaseModel):
    """
    Récupère la personne a qui la tâche est confiée et quelle est le type d'action à réaliser.
    Spécifie si la requête de l'utilisateur correspond à une tâche ou non.
    """

    responsable: str = Field(
        description="""
        Responsable de la tâche. Identifie dans la requête à qui la tâche est confiée.
        1. Soit tu arrives à identifier la personne à qui la tâche est confiée.
        2. Soit si tu n'y arrive pas utilise l'utilisateur connecté.
        Exemple : "Je dois aller chez le dentiste pour Aurore"
        Le responsable est "Je" donc l'utilisateur connecté
        """
    )
    type: str = Field(
        description="Type d'action à effectuer : ajouter, modifier, supprimer, consulter"
    )
    is_task: bool = Field(
        description="Indique si la requête de l'utilisateur correspond à une tâche ou non, true si ca correspond à une tâche, false sinon"
    )
