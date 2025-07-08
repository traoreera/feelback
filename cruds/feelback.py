import deps
from ..models.feelbacks import Feelbacks
from ..schemas import AddFeelback, UserId, UpdateFeelback, DeleteFeelback


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
        response = self.db.query(Feelbacks).filter(Feelbacks.user_id == feelback.user_id).first()
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
