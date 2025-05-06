from typing import Any, Dict

from graph.chains.rag_retrieval import retrieval_chain
from graph.models.GraphState import GraphState
from tools.get_retriever import retriever


def get_all_tasks(state: GraphState) -> Dict[str, Any]:
    """
    Récupère toutes les tâches assignées à un responsable spécifique à l'aide d'une chaîne de récupération.

    :param state: Un GraphState contenant un champ 'task' avec un attribut 'responsable'.
    :return: Un dictionnaire contenant la réponse du système (ui_response).
    """
    task = state.get("task")
    if not task or not hasattr(task, "responsable"):
        return {"ui_response": "Aucun responsable spécifié."}

    responsable = task.responsable
    question = f"Quelles sont toutes les taches de {responsable} ?"
    result = retrieval_chain.invoke(input={"input": question})
    if not result['context']:
        return {"ui_response": "Vous n’avez pas de tâches enregistrées pour le moment."}

    return {"ui_response": result.get("answer", "Aucune réponse trouvée.")}
