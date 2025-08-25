from fasthtml.common import *

import deps

dash = APIRouter("/admins/feelback")


class Dash:

    def __init__(self):
        pass

    @dash("/", ["GET"])
    @deps.admin_validation
    def run(session):

        html = deps.DashBase(
            head=[],
            content=[
                Div(
                    Div(
                        Div(I(cls="fas fa-users"), cls="icon users"),
                        Div(
                            H3("1,245"),
                            P("Utilisateurs"),
                            Span(I(cls="fas fa-arrow-up"), "12%", cls="trend up"),
                            cls="info",
                        ),
                        cls="stat-card",
                    ),
                    Div(
                        Div(I(cls="fas fa-exclamation-circle"), cls="icon errors"),
                        Div(
                            H3("42"),
                            P("Erreurs (24h)"),
                            Span(I(cls="fas fa-arrow-up"), "5%", cls="trend up"),
                            cls="info",
                        ),
                        cls="stat-card",
                    ),
                    Div(
                        Div(I(cls="fas fa-exclamation-triangle"), cls="icon risks"),
                        Div(
                            H3("8"),
                            P("Risques"),
                            Span(I(cls="fas fa-minus"), "Stable", cls="trend neutral"),
                            cls="info",
                        ),
                        cls="stat-card",
                    ),
                    Div(
                        Div(I(cls="fas fa-envelope"), cls="icon messages"),
                        Div(
                            H3("3"),
                            P("Messages non lus"),
                            Span(I(cls="fas fa-arrow-down"), "2", cls="trend down"),
                            cls="info",
                        ),
                        cls="stat-card",
                    ),
                    cls="stats-container",
                ),
                Div(
                    Div(
                        H2("Activité des utilisateurs"),
                        Canvas(id="userActivityChart"),
                        cls="chart-container",
                    ),
                    Div(
                        H2("Erreurs récentes"),
                        Div(
                            Div(
                                Div(
                                    I(cls="fas fa-exclamation-circle"), cls="error-icon"
                                ),
                                Div(
                                    P(
                                        "Échec de connexion - Tentative de brute force",
                                        cls="error-message",
                                    ),
                                    P(
                                        "Il y a 12 minutes · IP: 192.168.1.45",
                                        cls="error-time",
                                    ),
                                    cls="error-details",
                                ),
                                cls="error-item",
                            ),
                            Div(
                                Div(
                                    I(cls="fas fa-exclamation-circle"), cls="error-icon"
                                ),
                                Div(
                                    P(
                                        "Session expirée - Utilisateur: jdupont",
                                        cls="error-message",
                                    ),
                                    P(
                                        "Il y a 34 minutes · IP: 192.168.1.102",
                                        cls="error-time",
                                    ),
                                    cls="error-details",
                                ),
                                cls="error-item",
                            ),
                            Div(
                                Div(
                                    I(cls="fas fa-exclamation-circle"), cls="error-icon"
                                ),
                                Div(
                                    P(
                                        "Tentative d'accès non autorisé",
                                        cls="error-message",
                                    ),
                                    P(
                                        "Il y a 1 heure · IP: 192.168.1.78",
                                        cls="error-time",
                                    ),
                                    cls="error-details",
                                ),
                                cls="error-item",
                            ),
                            cls="error-list",
                        ),
                        Button("Voir toutes les erreurs", cls="view-all"),
                        cls="recent-errors",
                    ),
                    cls="content-row",
                ),
                Div(
                    Div(
                        H2("Derniers utilisateurs"),
                        Button(
                            I(cls="fas fa-plus"),
                            "Ajouter un utilisateur",
                            cls="add-user",
                        ),
                        cls="table-header",
                    ),
                    Table(
                        Thead(
                            Tr(
                                Th("ID"),
                                Th("Nom"),
                                Th("Email"),
                                Th("Rôle"),
                                Th("Statut"),
                                Th("Actions"),
                            )
                        ),
                        Tbody(
                            Tr(
                                Td("#001"),
                                Td(
                                    Img(
                                        src="https://via.placeholder.com/30", alt="User"
                                    ),
                                    "Jean Dupont",
                                ),
                                Td("j.dupont@example.com"),
                                Td("Administrateur"),
                                Td(Span("Actif", cls="status active")),
                                Td(
                                    Button(I(cls="fas fa-edit"), cls="action-btn edit"),
                                    Button(
                                        I(cls="fas fa-trash"), cls="action-btn delete"
                                    ),
                                ),
                            ),
                            Tr(
                                Td("#002"),
                                Td(
                                    Img(
                                        src="https://via.placeholder.com/30", alt="User"
                                    ),
                                    "Marie Martin",
                                ),
                                Td("m.martin@example.com"),
                                Td("Modérateur"),
                                Td(Span("Actif", cls="status active")),
                                Td(
                                    Button(I(cls="fas fa-edit"), cls="action-btn edit"),
                                    Button(
                                        I(cls="fas fa-trash"), cls="action-btn delete"
                                    ),
                                ),
                            ),
                            Tr(
                                Td("#003"),
                                Td(
                                    Img(
                                        src="https://via.placeholder.com/30", alt="User"
                                    ),
                                    "Pierre Durand",
                                ),
                                Td("p.durand@example.com"),
                                Td("Utilisateur"),
                                Td(Span("Inactif", cls="status inactive")),
                                Td(
                                    Button(I(cls="fas fa-edit"), cls="action-btn edit"),
                                    Button(
                                        I(cls="fas fa-trash"), cls="action-btn delete"
                                    ),
                                ),
                            ),
                        ),
                    ),
                    cls="users-table",
                ),
            ],
            style=[Link(rel="stylesheet", href="../../css/Adminscss.css")],
            script=[],
        )

        return html.page()
