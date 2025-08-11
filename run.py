import deps
from fasthtml.common import Request

from .cruds.feelback import CrudFeelback
from .pages.avis import avisPage
from .pages.home import feelBackHome
from .schemas import AddAvis, AddFeelback, DeleteFeelback, Feelback, UserId
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
    @deps.user_validation
    def run(session, request: Request):
        return feelBackHome.page()

    @router("/refresh", methods=["GET"])
    @deps.user_validation
    def refrech(session, request: Request):
        response = OPTIONS.CRUD.get_all_(feelback=UserId(user_id=session["user_id"]))

        return {
            "table": {
                "bad": [1, 2, 34, 45, 23, 9, 50, 0, 23, 90, 40, 13],
                "midle": [1, 2, 34, 45, 29, 3, 40, 4, 30, 92, 30, 23],
                "good": [1, 2, 34, 45, 25, 2, 0, 3, 20, 2, 34, 3],
            },
            "donute": OPTIONS.CRUD.donute(feelback=UserId(user_id=session["user_id"])),
            "cards": response,
        }

    @router("/add", methods=["POST"])
    @deps.user_validation
    def add_topic(session, request: Request, nom: str, localite: str):
        OPTIONS.CRUD.add(
            feelback=AddFeelback(
                user_id=session["user_id"], topic=nom, localite=localite
            )
        )
        clientMq.publish(topic=f"{nom}/{session['user_id']}")
        return {"success": True}

    @router("/delete/{id}", methods=["GET"])
    @deps.user_validation
    def remove(session, request: Request, id: str):
        try:
            OPTIONS.CRUD.remove(
                feelback=DeleteFeelback(user_id=session["user_id"], feelback_id=id)
            )
            return
        except Exception:
            pass

    @router("/avis/{fellback_id}", methods=["GET", "POST"])
    def feelback_avis(
        session, request: Request, fellback_id: str, avis: str = "", identite: str = ""
    ):
        if response := OPTIONS.CRUD.get_user_with_feelback(
            feelback=Feelback(feelback_id=fellback_id, user_id=session["user_id"])
        ):
            if request.method == "GET":
                return avisPage.page()
            elif request.method == "POST":
                OPTIONS.CRUD.addAvis(
                    avis=AddAvis(
                        identite=identite,
                        avis=avis,
                        feelback_id=fellback_id,
                        user_id=response,
                    )
                )
                return avisPage.afterSubmit()

        else:
            return avisPage.notFound()

        return {"success": True}
