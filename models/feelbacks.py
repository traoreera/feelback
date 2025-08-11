import deps  # core dependance for application

from ..schemas import AddFeelback


class Feelbacks(deps.Base):

    __tablename__ = "feelbacks"

    __table_args__ = (deps.UniqueConstraint("user_id", "topic", name="uq_user_topic"),)

    # for iditification
    id = deps.Column(deps.String, primary_key=True, index=True)
    user_id = deps.Column(deps.String, nullable=False, index=True)

    # for data
    topic = deps.Column(deps.String, nullable=False)
    bad = deps.Column(deps.Integer, nullable=False, default=0)
    good = deps.Column(deps.Integer, nullable=False, default=0)
    middle = deps.Column(deps.Integer, nullable=False, default=0)

    # description
    localite = deps.Column(
        deps.Text,
        nullable=True,
    )

    # for time
    created_at = deps.Column(deps.TIMESTAMP, server_default=deps.func.now())
    updated_at = deps.Column(
        deps.TIMESTAMP, server_default=deps.func.now(), onupdate=deps.func.now()
    )

    def __init__(
        self,
        feelback: AddFeelback,
    ):
        self.user_id = feelback.user_id
        self.topic = feelback.topic
        self.bad = feelback.bad
        self.good = feelback.good
        self.middle = feelback.middle
        self.localite = feelback.localite
        self.id = deps.make_ids()

    def responseModel(self):
        return {
            "id": self.id,
            "name": self.topic,
            "happy": self.good,
            "neutral": self.middle,
            "unhappy": self.bad,
        }


class Avis(deps.Base):
    __tablename__ = "avis"

    # for iditification
    id = deps.Column(deps.String, primary_key=True, index=True, unique=True)
    feelback_id = deps.Column(deps.String, nullable=False, index=True)
    user_id = deps.Column(deps.String, nullable=False, index=True)
    # for data
    identite = deps.Column(deps.String, nullable=False)

    avis = deps.Column(deps.Text, nullable=False)

    def __init__(self, identite: str, avis: str, feelback_id: str, user_id: str):
        self.identite = identite
        self.feelback_id = feelback_id
        self.user_id = user_id
        self.avis = avis
        self.id = deps.make_ids()

    def responseModel(self):
        return {
            "id": self.id,
            "identite": self.identite,
            "avis": self.avis,
        }
        # Add any other fields you want to return in the response
