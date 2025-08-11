import deps

from ..models.feelbacks import Avis, Feelbacks
from ..schemas import (
    AddAvis,
    AddFeelback,
    DeleteFeelback,
    Feelback,
    UpdateFeelback,
    UserId,
)


class CrudFeelback:
    def __init__(self):
        self.model = Feelbacks
        self.db: deps.Session = deps.db

    def for_refresh(self, feelback: AddFeelback):
        try:
            self.db.refresh(feelback)
            return True
        except Exception:
            self.for_rollback()
            return False

    def for_rollback(self):
        return self.db.rollback()

    def add(self, feelback: AddFeelback):
        try:
            self.db.add(Feelbacks(feelback=feelback))
            return self._extracted_from_update_4(feelback)
        except Exception:
            self.for_rollback()
            return False

    def remove(self, feelback: DeleteFeelback):
        if (
            self.db.query(Feelbacks)
            .filter(Feelbacks.id == feelback.feelback_id)
            .filter(Feelbacks.user_id == feelback.user_id)
            .delete()
        ):
            self.db.commit()
            return True

        else:
            self.for_rollback()
            return False

    def update(self, feelback: UpdateFeelback):
        response = (
            self.db.query(Feelbacks)
            .filter(Feelbacks.user_id == feelback.user_id)
            .first()
        )
        if response:
            if feelback.message == "bad":
                response.bad += 1
            if feelback.message == "good":
                response.good += 1
            if feelback.message == "midle":
                response.middle += 1
            self.db.commit()

    # TODO Rename this here and in `add` and `update`
    def _extracted_from_update_4(self, feelback):
        return self._extracted_from__extracted_from_update_4_15(feelback)

    # TODO Rename this here and in `update` and `_extracted_from_update_4`
    def _extracted_from__extracted_from_update_4_15(self, arg0):
        self.db.commit()
        self.for_refresh(arg0)
        return True

    def get_all_(self, feelback: UserId):
        response = [
            i.responseModel()
            for i in (
                self.db.query(Feelbacks)
                .filter(Feelbacks.user_id == feelback.user_id)
                .all()
            )
        ]

        # sourcery skip: or-if-exp-identity
        return response if response else None

    def get_element_by_id(self, feelback: Feelback):
        response = (
            self.db.query(Feelbacks)
            .filter(Feelbacks.user_id == feelback.user_id)
            .filter(Feelbacks.id == feelback.feelback_id)
            .first()
        )
        return response.responseModel() if response else None

    def get_feelback_for_avis_with_id(self, feelback: Feelback):
        response = (
            self.db.query(Feelbacks)
            .filter(Feelbacks.user_id == feelback.user_id)
            .first()
        )

        return response.user_id if response else None

        # sourcery skip: or-if-exp-identity

    def donute(self, feelback: UserId):
        # return total of bad good midle vote filter by user_id
        if response := (
            self.db.query(Feelbacks).filter(Feelbacks.user_id == feelback.user_id).all()
        ):
            midle = [i.middle for i in response]
            bad = [i.bad for i in response]
            good = [i.good for i in response]
            return [sum(midle), sum(bad), sum(good)]
        else:
            return [0, 0, 0]

    def get_user_with_feelback(self, feelback: Feelback):
        response = (
            self.db.query(Feelbacks)
            .filter(Feelbacks.id == feelback.feelback_id)
            .first()
        )
        return response.user_id if response else None

    def addAvis(self, avis: AddAvis):
        try:
            self.db.add(
                Avis(
                    identite=avis.identite,
                    avis=avis.avis,
                    user_id=avis.user_id,
                    feelback_id=avis.feelback_id,
                )
            )
            self.db.commit()
        except Exception:
            self.for_rollback()
            return False

    def get_avis(self, feelback: Feelback):
        response = (
            self.db.query(Avis)
            .filter(Avis.feelback_id == feelback.feelback_id)
            .filter(Avis.user_id == feelback.user_id)
            .all()
        )
        return [i.responseModel() for i in response] if response else None
