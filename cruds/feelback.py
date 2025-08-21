import functools

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


# ---------------------
# Décorateur transactionnel
# ---------------------
def transactional(commit: bool = True, refresh: bool = False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                result = func(self, *args, **kwargs)
                if commit:
                    self.db.commit()
                if refresh and result is not None:
                    self.db.refresh(result)
                return result
            except Exception:
                self.db.rollback()
                return False

        return wrapper

    return decorator


class CrudFeelback:
    def __init__(self):
        self.model = Feelbacks
        self.db: deps.Session = deps.db

    # ---------------------
    # CRUD Feelbacks
    # ---------------------
    @transactional(commit=True, refresh=True)
    def add(self, feelback: AddFeelback):
        try:
            self.db.add(Feelbacks(feelback=feelback))
            self.db.commit()
            return
        except Exception:
            self.db.rollback()
            return False

    @transactional()
    def remove(self, feelback: DeleteFeelback):
        deleted = (
            self.db.query(Feelbacks)
            .filter(Feelbacks.id == feelback.feelback_id)
            .filter(Feelbacks.user_id == feelback.user_id)
            .delete()
        )
        return bool(deleted)

    @transactional()
    def update(self, feelback: UpdateFeelback):
        response = (
            self.db.query(Feelbacks)
            .filter(Feelbacks.user_id == feelback.user_id)
            .filter(Feelbacks.topic == feelback.topic)
            .first()
        )
        if not response:
            return False

        mapping = {"bad": "bad", "good": "good", "midle": "middle"}
        if feelback.message in mapping:
            field = mapping[feelback.message]
            setattr(response, field, getattr(response, field) + 1)
            return True
        return False

    def get_all_(self, feelback: UserId):
        return [
            i.responseModel()
            for i in self.db.query(Feelbacks)
            .filter(Feelbacks.user_id == feelback.user_id)
            .all()
        ]

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

    def donute(self, feelback: UserId):
        response = (
            self.db.query(Feelbacks).filter(Feelbacks.user_id == feelback.user_id).all()
        )
        if not response:
            return [0, 0, 0]
        return [
            sum(i.middle for i in response),
            sum(i.bad for i in response),
            sum(i.good for i in response),
        ]

    def get_user_with_feelback(self, feelback: Feelback):
        response = (
            self.db.query(Feelbacks)
            .filter(Feelbacks.id == feelback.feelback_id)
            .first()
        )
        return response.user_id if response else None

    # ---------------------
    # CRUD Avis
    # ---------------------
    @transactional(commit=True, refresh=True)
    def addAvis(self, avis: AddAvis):
        obj = Avis(**avis.dict())
        self.db.add(obj)
        return obj

    def get_avis(self, feelback: UserId):
        avis_list = self.db.query(Avis).filter(Avis.user_id == feelback.user_id).all()
        feelbacks = self.get_all_(feelback)
        avis_res = [i.responseModel() for i in avis_list]
        print(avis_res)
        return avis_res, feelbacks

    # ---------------------
    # 📌 Nouveau : Feedbacks groupés par feelback_id
    # ---------------------
    def get_feedbacks_grouped(self, user_id: UserId):
        """
        Retourne les avis groupés par nom de section (récupéré depuis Feelbacks)
        pour un utilisateur donné :
        {
            "nom_section": [{name, text}, ...]
        }
        """
        # Récupère tous les avis pour cet utilisateur
        all_avis = self.db.query(Avis).filter(Avis.user_id == user_id.user_id).all()

        grouped = {}

        for avis in all_avis:
            # On récupère le feelback correspondant pour avoir son nom
            feelback = (
                self.db.query(Feelbacks)
                .filter(Feelbacks.id == avis.feelback_id)
                .first()
            )

            # Nom de section => si pas trouvé on met "Inconnu"
            section_name = getattr(feelback, "topic", "Inconnu")

            if section_name not in grouped:
                grouped[section_name] = []

            grouped[section_name].append({"name": avis.identite, "text": avis.avis})

        return grouped
