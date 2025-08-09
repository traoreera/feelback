import deps
from fasthtml.common import Request

from .cruds.feelback import CrudFeelback
from .pages.home import feelBackHome
from .schemas import AddFeelback, DeleteFeelback, Feelback
from .task.feelback import clientMq

PLUGIN_INFO = {
    "name": "Feelback",
    "version": "1.0.0",
    "author": "traore Eliezer B.",
    "Api_prefix": "/app/feelback",
    "tag_for_identified": ["Plugin", "feelback"],
    "trigger": 1,
    "description": "Feelback plugin for user feedback and interaction.",
    "author_url": "git:traoreera",
}

router = deps.APIRouter(
    prefix=PLUGIN_INFO["Api_prefix"],
)


class OPTIONS:
    CRUD = CrudFeelback()


class Plugin:
    def __init__(self):
        pass

    @router("/", methods=["GET"])
    # @deps.user_validation
    def run(session, request: Request):
        return feelBackHome.page()

    @router("/refresh", methods=["GET"])
    # @deps.user_validation
    def refrech(session, request: Request):
        response = OPTIONS.CRUD.donute(
            feelback=Feelback(user_id=session["user_id"], feelback_id=1)
        )
        return response

    @router("/add", methods=["POST"])
    # @deps.user_validation
    def add_topic(session, request: Request, nom: str, localite: str):
        OPTIONS.CRUD.add(
            feelback=AddFeelback(
                user_id=session["user_id"], topic=nom, localite=localite
            )
        )
        clientMq.publish(topic=f"{nom}/{session['user_id']}")
        return {"success": True}

    @router("/delete/{id}", methods=["GET"])
    # #@deps.user_validation
    def remove(session, request: Request, id: str):
        try:
            OPTIONS.CRUD.remove(
                feelback=DeleteFeelback(user_id=session["user_id"], feelback_id=id)
            )
            return
        except Exception:
            pass

    @router("/avis/{fellback_id}", methods=["GET"])
    def feelback_avis(session, request: Request, fellback_id: str):

        if response := True:

            return f"""
            <form action="/app/feelback/avis/{response}" method="POST">
            <input type="text" name="avis" placeholder="Votre avis" id="avis", required>
            <input type="submit" value="Envoyer">
            </form>
            """

        else:
            return f""" 404 Not Found: {fellback_id} not found in database"""

    @router("/avis/{feelback_id}", methods=["POST"])
    def feelback_avis_posting(session, request: Request, feelback_id: str, avis: str):
        print(avis, feelback_id)
