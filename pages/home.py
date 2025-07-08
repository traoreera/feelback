from core.composants import *
from fasthtml.common import *
from deps import AllPage


class FeelBackHome:
    def __init__(self):

        self.html = AllPage(
            head=[
                Script(src="../../js/feelback.js"),
                Script(src="../../js/userBord.js"),
                Link(rel="stylesheet", href="../../css/style.css"),
                Link(rel="stylesheet", href="../../css/feelback.css"),
                Meta(charset="UTF-8"),
                Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
                Title("FeelBack Dashboard"),
                Link(
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css",
                    rel="stylesheet",
                ),
                Link(
                    rel="stylesheet",
                    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css",
                ),
                Script(
                    src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"
                ),
            ],
            plugins=[
                {
                    "name": "FeelBack",
                    "url": "/app/feelback",
                },
                {
                    "name": "Home Lock",
                    "url": "/app/locket",
                }
            ],
            content=[
                Div(
                    Div(
                        H2("Tableau par 12 mois"),
                        Canvas(
                            id="lignegraph",
                            #height="400",
                            #style="""display: block; box-sizing: border-box; height: 400px; width: 992px;""",
                        ),
                        id="bare",
                        cls="chart",
                    ),
                    Div(
                        H2("Taux Journalier"),
                        Canvas(id="cercle"),
                        id="doughnut-chart",
                        cls="chart",
                    ),
                    cls="charts",
                ),
                Section(
                    Div(
                        H2("Points de feedback"),
                        Button(I(cls="fas fa-plus"), id="AjoutTopic", cls="add-btn"),
                        cls="DivTitre",
                    ),
                    Div(id="Div_Feedback", cls="DivFeedback"),
                ),
                Div(
                    Div(
                        Div(
                            H3("Ajouter un point de feedback", cls="titreModal"),
                            Button("×", id="btnFermerModal", cls="FermerModal"),
                            cls="enteteModal",
                        ),
                        Form(
                            Div(
                                Label("Nom du point", fr="nom"),
                                Input(
                                    type="text",
                                    id="nom",
                                    name="nom",
                                    placeholder="Ex: Caisse 1",
                                    required="",
                                    cls="form-control",
                                ),
                                cls="form-group",
                            ),
                            Div(
                                Label("Emplacement", fr="pointLocation"),
                                Input(
                                    type="text",
                                    id="pointLocation",
                                    name="localite",
                                    placeholder="Ex: Entrée principale",
                                    cls="form-control",
                                ),
                                cls="form-group",
                            ),
                            Button("Ajouter le point", type="submit", cls="submit-btn"),
                            id="formModal",
                        ),
                        cls="contenuModal",
                    ),
                    id="voirModal",
                    cls="modal",
                ),
            ],
        )

    def page(self):
        return self.html.page()


home_pages = FeelBackHome()
