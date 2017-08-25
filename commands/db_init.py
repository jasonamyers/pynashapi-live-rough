from datetime import date

from flask_script import Command

from pynashapi.models import Moment


class DbInit(Command):
    def __init__(self, db):
        self.db = db

    def run(self):
        self.db.create_all()


class DbProp(Command):
    def __init__(self, db):
        self.db = db

    def run(self):
        moment = Moment(
            id=99999999,
            event_date=date(month=5, day=5, year=2009),
            details='Original PyNash night meetings started')
        moment.add()
