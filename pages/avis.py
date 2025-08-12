from fasthtml.common import (
    H1,
    H2,
    A,
    Body,
    Button,
    Div,
    Form,
    Head,
    Html,
    Input,
    Label,
    Link,
    Meta,
    P,
    Script,
    Section,
    Span,
    Style,
    Textarea,
    Title,
)


class Avis:

    def __init__(self):

        super().__init__()

    def page(self):
        return Html(
            Head(
                Meta(charset="UTF-8"),
                Meta(name="viewport", content="width=device-width, initial-scale=1"),
                Title("TANGA GROUP, Bâtir un technopole africain"),
                Link(
                    href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap",
                    rel="stylesheet",
                ),
                Style(
                    ':root {\r\n      --primary: #050505;\r\n      --primary-dark: #6D6D6D;\r\n      --secondary: #8888;\r\n      --contour-colour: #4F4F4F;\r\n      --accent: #B0B0B0;\r\n      --bg: #D1D1D1;\r\n      --text: #1a1a1a;\r\n    }\r\n\r\n    body.dark-mode {\r\n      --primary: #ffffff;\r\n      --primary-dark: #bbbbbb;\r\n      --secondary: #4444;\r\n      --contour-colour: #888;\r\n      --accent: #f1f1f1;\r\n      --bg: #121212;\r\n      --text: #f5f5f5;\r\n    }\r\n\r\n    * {\r\n      margin: 0;\r\n      padding: 0;\r\n      box-sizing: border-box;\r\n      font-family: \'Poppins\', sans-serif;\r\n    }\r\n\r\n    body {\r\n      background-color: var(--bg);\r\n      color: var(--text);\r\n      transition: background-color 0.4s, color 0.4s;\r\n      line-height: 1.6;\r\n    }\r\n\r\n    header {\r\n      background: linear-gradient(90deg, var(--primary), var(--secondary));\r\n      padding: 20px 40px;\r\n      text-align: center;\r\n      color: white;\r\n      position: sticky;\r\n      top: 0;\r\n      z-index: 1000;\r\n      display: flex;\r\n      justify-content: space-between;\r\n      align-items: center;\r\n    }\r\n\r\n    .logo-container {\r\n      display: flex;\r\n      align-items: center;\r\n      gap: 20px;\r\n      flex-wrap: wrap;\r\n    }\r\n\r\n    .logo-container .logo {\r\n      height: 60px;\r\n      width: auto;\r\n      object-fit: contain;\r\n    }\r\n\r\n    .mode-toggle {\r\n      background-color: var(--contour-colour);\r\n      color: white;\r\n      border: none;\r\n      padding: 10px 20px;\r\n      border-radius: 20px;\r\n      font-size: 14px;\r\n      cursor: pointer;\r\n      margin-left: auto;\r\n      transition: transform 0.4s ease;\r\n      user-select: none;\r\n    }\r\n\r\n    .mode-toggle.clicked {\r\n      transform: rotate(180deg) scale(1.1);\r\n    }\r\n\r\n    nav {\r\n      display: flex;\r\n      justify-content: center;\r\n      flex-wrap: wrap;\r\n      gap: 15px;\r\n      padding: 20px;\r\n      background-color: white;\r\n      position: sticky;\r\n      top: 72px;\r\n      z-index: 999;\r\n    }\r\n\r\n    nav button {\r\n      background-color: var(--contour-colour);\r\n      color: white;\r\n      border: none;\r\n      padding: 15px 25px;\r\n      border-radius: 25px;\r\n      font-size: 16px;\r\n      cursor: pointer;\r\n      transition: transform 0.3s, background-color 0.3s;\r\n    }\r\n\r\n    nav button:hover {\r\n      background-color: var(--primary-dark);\r\n      transform: scale(1.05);\r\n    }\r\n\r\n    section {\r\n      padding: 60px 40px;\r\n      margin: 40px auto;\r\n      max-width: 1000px;\r\n      min-height: 500px;\r\n      text-align: center;\r\n      background: white;\r\n      border-radius: 20px;\r\n      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);\r\n      transition: opacity 0.6s ease-out, transform 0.6s ease-out;\r\n    }\r\n\r\n    body.dark-mode section {\r\n      background: #1e1e1e;\r\n    }\r\n\r\n\r\n    section h2 {\r\n      margin-bottom: 20px;\r\n      color: var(--primary);\r\n    }\r\n\r\n    .emoji {\r\n      font-size: 50px;\r\n      display: block;\r\n      margin-bottom: 20px;\r\n      transition: transform 0.3s;\r\n    }\r\n\r\n    .emoji:hover {\r\n      animation: bounce 0.6s ease-in-out infinite alternate;\r\n    }\r\n\r\n    button.demo-btn {\r\n      background-color: var(--primary);\r\n      color: white;\r\n      border: none;\r\n      padding: 12px 30px;\r\n      border-radius: 30px;\r\n      font-size: 18px;\r\n      cursor: pointer;\r\n      margin-top: 20px;\r\n      transition: background-color 0.3s ease;\r\n    }\r\n\r\n    button.demo-btn:hover {\r\n      background-color: var(--primary-dark);\r\n    }\r\n\r\n\r\n    /* ----- Formulaire d\'avis ----- */\r\n    .feedback-form {\r\n      max-width: 500px;\r\n      margin: 20px auto;\r\n      text-align: left;\r\n    }\r\n\r\n    .feedback-form label {\r\n      display: block;\r\n      margin-bottom: 8px;\r\n      font-weight: 600;\r\n      color: var(--primary);\r\n    }\r\n\r\n    .feedback-form input[type="text"],\r\n    .feedback-form textarea {\r\n      width: 100%;\r\n      padding: 12px;\r\n      margin-bottom: 20px;\r\n      border-radius: 10px;\r\n      border: 1px solid var(--contour-colour);\r\n      background-color: var(--accent);\r\n      color: var(--text);\r\n      font-family: \'Poppins\', sans-serif;\r\n      font-size: 16px;\r\n      transition: border-color 0.3s ease, background-color 0.3s ease;\r\n      resize: vertical;\r\n    }\r\n\r\n    .feedback-form input[type="text"]:focus,\r\n    .feedback-form textarea:focus {\r\n      outline: none;\r\n      border-color: var(--primary);\r\n      background-color: var(--bg);\r\n    }\r\n\r\n    .feedback-form button[type="submit"] {\r\n      width: 100%;\r\n      cursor: pointer;\r\n      font-size: 18px;\r\n      border-radius: 30px;\r\n      padding: 12px 0;\r\n      transition: background-color 0.3s ease;\r\n    }\r\n\r\n    .feedback-form button[type="submit"]:hover {\r\n      background-color: var(--primary-dark);\r\n    }\r\n\r\n    #formMessage {\r\n      text-align: center;\r\n      margin-top: 15px;\r\n      font-weight: 600;\r\n      color: var(--primary-dark);\r\n    }\r\n\r\n    @keyframes bounce {\r\n      0% {\r\n        transform: translateY(0);\r\n      }\r\n      100% {\r\n        transform: translateY(-10px);\r\n      }\r\n    }\r\n\r\n    @media (max-width: 600px) {\r\n      header {\r\n        flex-direction: column;\r\n        align-items: center;\r\n        padding: 15px 20px;\r\n      }\r\n\r\n      .logo-container {\r\n        gap: 10px;\r\n        justify-content: center;\r\n        text-align: center;\r\n      }\r\n\r\n      .logo-container .logo {\r\n        height: 40px;\r\n      }\r\n\r\n      .logo-container .text h1 {\r\n        font-size: 18px;\r\n      }\r\n\r\n      .logo-container .text p {\r\n        font-size: 12px;\r\n      }\r\n\r\n      .mode-toggle {\r\n        margin-left: 0;\r\n        margin-top: 10px;\r\n        padding: 8px 15px;\r\n        font-size: 12px;\r\n        border-radius: 15px;\r\n      }\r\n\r\n      nav {\r\n        flex-wrap: wrap;\r\n        gap: 10px;\r\n        padding: 10px 15px;\r\n        position: static;\r\n      }\r\n\r\n      nav button {\r\n        flex: 1 1 45%;\r\n        padding: 10px 15px;\r\n        font-size: 14px;\r\n        border-radius: 20px;\r\n      }\r\n\r\n      section {\r\n        padding: 30px 20px;\r\n        margin: 20px 15px;\r\n        max-width: 100%;\r\n        border-radius: 15px;\r\n      }\r\n\r\n      section h2 {\r\n        font-size: 20px;\r\n      }\r\n\r\n      .emoji {\r\n        font-size: 40px;\r\n      }\r\n\r\n      button.demo-btn {\r\n        padding: 10px 25px;\r\n        font-size: 16px;\r\n      }\r\n\r\n      footer {\r\n        padding: 20px 10px;\r\n        font-size: 14px;\r\n      }\r\n    }'
                ),
            ),
            Body(
                Section(
                    Span("📝", cls="emoji"),
                    H2("Donnez-nous votre avis"),
                    P("Vos retours nous aident à améliorer nos solutions."),
                    Form(
                        Label("Plaque d'immarticulation", fr="identite"),
                        Input(
                            type="text",
                            id="identite",
                            name="identite",
                            placeholder="Nom ou entreprise",
                            required=True,
                        ),
                        Label("Votre avis", fr="avis"),
                        Textarea(
                            id="avis",
                            name="avis",
                            placeholder="Partagez votre expérience...",
                            rows="5",
                            required=True,
                        ),
                        Button("📨 Envoyer", type="submit", cls="demo-btn"),
                        id="feedbackForm",
                        cls="feedback-form",
                        method="post",
                    ),
                    P(id="formMessage"),
                ),
            ),
            lang="fr",
        )

    def afterSubmit(
        self,
    ):
        return Html(
            Head(
                Meta(charset="UTF-8"),
                Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
                Title("Merci pour votre Avis"),
                Style(
                    "body {\r\n            font-family: Arial, sans-serif;\r\n            margin: 0;\r\n            padding: 0;\r\n            background-color: #f4f4f4;\r\n            display: flex;\r\n            justify-content: center;\r\n            align-items: center;\r\n            height: 100vh;\r\n        }\r\n        .container {\r\n            max-width: 600px;\r\n            width: 100%;\r\n            background: white;\r\n            padding: 20px;\r\n            border-radius: 8px;\r\n            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);\r\n            text-align: center;\r\n        }\r\n        h1 {\r\n            color: #333;\r\n        }\r\n        p {\r\n            color: #555;\r\n        }\r\n        a {\r\n            display: inline-block;\r\n            margin-top: 20px;\r\n            padding: 10px 20px;\r\n            background-color: #007BFF;\r\n            color: white;\r\n            text-decoration: none;\r\n            border-radius: 4px;\r\n        }\r\n        a:hover {\r\n            background-color: #0056b3;\r\n        }"
                ),
            ),
            Body(
                Div(
                    H1("Merci pour votre Avis !"),
                    P(
                        "Nous apprécions vos retours et nous nous engageons à améliorer nos services."
                    ),
                    A(
                        "Retour à notre site",
                        href="https://app.tangagroup.com",
                        target="_blank",
                    ),
                    cls="container",
                )
            ),
            lang="fr",
        )

    def notFound(self):
        return Html(
            Head(
                Meta(charset="UTF-8"),
                Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
                Title("Page Non Trouvée - 404"),
                Style(
                    "body {\r\n            font-family: Arial, sans-serif;\r\n            margin: 0;\r\n            padding: 0;\r\n            background-color: #f4f4f4;\r\n            display: flex;\r\n            justify-content: center;\r\n            align-items: center;\r\n            height: 100vh;\r\n            text-align: center;\r\n        }\r\n        .container {\r\n            max-width: 600px;\r\n            width: 100%;\r\n            background: white;\r\n            padding: 20px;\r\n            border-radius: 8px;\r\n            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);\r\n        }\r\n        h1 {\r\n            color: #333;\r\n            font-size: 2.5em;\r\n        }\r\n        p {\r\n            color: #555;\r\n            font-size: 1.2em;\r\n        }\r\n        a {\r\n            display: inline-block;\r\n            margin-top: 20px;\r\n            padding: 10px 20px;\r\n            background-color: #007BFF;\r\n            color: white;\r\n            text-decoration: none;\r\n            border-radius: 4px;\r\n        }\r\n        a:hover {\r\n            background-color: #0056b3;\r\n        }"
                ),
            ),
            Body(
                Div(
                    H1("404 - Page Non Trouvée"),
                    P(
                        "Désolé, le point de feedback que vous recherchez n'a pas été trouvé."
                    ),
                    P(
                        "Il se peut que le lien soit brisé ou que la page ait été déplacée."
                    ),
                    P("Veuillez vérifier l'URL ou retourner à notre page d'accueil."),
                    A("Retour à l'Accueil", href="https://app.tangagroup.com"),
                    cls="container",
                )
            ),
            lang="fr",
        )

    def listAvis(self):

        return Html(
            Head(
                Meta(charset="UTF-8"),
                Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
                Title("Avis des Utilisateurs"),
                Style(
                    'body {\r\n            font-family: Arial, sans-serif;\r\n            margin: 0;\r\n            display: flex;\r\n            background-color: #f4f4f4;\r\n        }\r\n        .sidebar {\r\n            width: 200px;\r\n            background: #2c333a;\r\n            color: white;\r\n            padding: 20px;\r\n            height: 100vh;\r\n        }\r\n        .sidebar h2 {\r\n            color: white;\r\n        }\r\n        .sidebar a {\r\n            color: white;\r\n            text-decoration: none;\r\n            display: block;\r\n            margin: 10px 0;\r\n        }\r\n        .sidebar a:hover {\r\n            text-decoration: underline;\r\n        }\r\n        .container {\r\n            flex: 1;\r\n            padding: 20px;\r\n            background: white;\r\n            border-radius: 8px;\r\n            margin-left: 20px;\r\n        }\r\n        h1 {\r\n            text-align: center;\r\n            color: #333;\r\n        }\r\n        .section {\r\n            margin: 20px 0;\r\n            border: 1px solid #ddd;\r\n            border-radius: 4px;\r\n            padding: 10px;\r\n        }\r\n        .review {\r\n            border-bottom: 1px solid #ddd;\r\n            padding: 10px 0;\r\n        }\r\n        .review:last-child {\r\n            border-bottom: none;\r\n        }\r\n        .review p {\r\n            margin: 5px 0;\r\n            color: #555;\r\n        }\r\n        .form-group {\r\n            margin: 20px 0;\r\n        }\r\n        input[type="text"],\r\n        textarea {\r\n            width: 100%;\r\n            padding: 10px;\r\n            margin-top: 5px;\r\n            border: 1px solid #ccc;\r\n            border-radius: 4px;\r\n        }\r\n        button {\r\n            width: 100%;\r\n            padding: 10px;\r\n            background-color: #007BFF;\r\n            color: white;\r\n            border: none;\r\n            border-radius: 4px;\r\n            cursor: pointer;\r\n        }\r\n        button:hover {\r\n            background-color: #0056b3;\r\n        }'
                ),
            ),
            Body(
                Div(H2("Feelbacks"), Div(id="section-links"), cls="sidebar"),
                Div(
                    H1("Avis des Utilisateurs de votre service"),
                    Div(id="review-sections"),
                    cls="container",
                ),
                Script(
                    "// Exemple de données d'avis\r\n    async function fetchData() {\r\n        const response = await fetch('avisList');\r\n        return await response.json();\r\n    }\r\n\r\n    let data;\r\n\r\n    // Fonction pour générer dynamiquement les liens des sections\r\n    function generateSectionLinks() {\r\n        const sectionLinks = document.getElementById('section-links');\r\n        sectionLinks.innerHTML = ''; // Réinitialiser le contenu\r\n\r\n        for (const section in data) {\r\n            const link = document.createElement('a');\r\n            link.href = `#${section}`;\r\n            link.innerText = section.charAt(0).toUpperCase() + section.slice(1);\r\n            link.onclick = () => showSection(section);\r\n            sectionLinks.appendChild(link);\r\n        }\r\n    }\r\n\r\n    // Fonction pour afficher les avis d'une section\r\n    function displayReviews(section) {\r\n        const reviewSections = document.getElementById('review-sections');\r\n        reviewSections.innerHTML = ''; // Réinitialiser le contenu\r\n\r\n        const sectionDiv = document.createElement('div');\r\n        sectionDiv.classList.add('section');\r\n        sectionDiv.innerHTML = `<h3>${section.charAt(0).toUpperCase() + section.slice(1)}</h3>`; // Titre de la section\r\n\r\n        data[section].forEach(review => {\r\n            const reviewDiv = document.createElement('div');\r\n            reviewDiv.classList.add('review');\r\n            reviewDiv.innerHTML = `<strong>${review.name}</strong><p>${review.text}</p>`;\r\n            sectionDiv.appendChild(reviewDiv);\r\n        });\r\n\r\n        reviewSections.appendChild(sectionDiv);\r\n    }\r\n\r\n    // Afficher la première section par défaut\r\n    function showSection(section) {\r\n        displayReviews(section);\r\n    }\r\n\r\n    // Appel de la fonction pour générer les liens et afficher la première section\r\n    window.onload = async () => {\r\n        data = await fetchData();\r\n        generateSectionLinks();\r\n        showSection(Object.keys(data)[0]); // Afficher la première section\r\n    };\r\n\r\n    // Gestion de la soumission de l'avis\r\n    document.getElementById('submit-review').addEventListener('click', function() {\r\n        const name = document.getElementById('name').value;\r\n        const reviewText = document.getElementById('review').value;\r\n        const section = document.querySelector('.sidebar a.active')?.getAttribute('href').substring(1) || Object.keys(data)[0];\r\n\r\n        if (name && reviewText) {\r\n            // Ajouter l'avis à la section appropriée\r\n            data[section].push({ name, text: reviewText });\r\n            displayReviews(section); // Mettre à jour l'affichage\r\n            document.getElementById('name').value = '';\r\n            document.getElementById('review').value = '';\r\n        } else {\r\n            alert('Veuillez remplir tous les champs.');\r\n        }\r\n    });"
                ),
            ),
            lang="fr",
        )


avisPage = Avis()
