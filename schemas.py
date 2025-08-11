import deps


class AddFeelback(deps.BaseModel):
    user_id: str
    topic: str
    localite: str
    bad: int = 0
    good: int = 0
    middle: int = 0


class UserId(deps.BaseModel):
    user_id: str


class Feelback(deps.BaseModel):
    feelback_id: str
    user_id: str


class DeleteFeelback(UserId):
    feelback_id: str


class UpdateFeelback(deps.BaseModel):
    topic: str
    user_id: str
    message: str


class GetFeelback(deps.BaseModel):
    user_id: str


class AddAvis(deps.BaseModel):
    identite: str
    avis: str
    feelback_id: str


class FeelbackAvis(deps.BaseModel):
    user_id: str
    identite: str
    avis: str
    feelback_id: str
