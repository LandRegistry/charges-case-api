from app.db import db
from app.helper.serialize import serialize_datetime
from app import json
from dateutil.parser import parse
from datetime import datetime


class Case(db.Model, json.Serialisable):
    __tablename__ = 'case'

    id = db.Column(db.Integer, primary_key=True)
    deed_id = db.Column(db.Integer)
    conveyancer_id = db.Column(db.Integer)
    status = db.Column(db.String())
    last_updated = db.Column(db.DateTime())
    created_on = db.Column(db.DateTime())
    case_ref = db.Column(db.String())
    borrowers = db.relationship(
        'Borrower',
        order_by='Borrower.last_name',
        backref='case_borrower')

    def __init__(self,
                 conveyancer_id,
                 deed_id=None,
                 status='Case created',
                 last_updated=None,
                 created_on=None,
                 case_ref=''):

        if deed_id is not None:
            self.deed_id = deed_id

        self.conveyancer_id = conveyancer_id
        self.status = status
        self.case_ref = case_ref

        if last_updated is not None:
            self.last_updated = last_updated
        else:
            self.last_updated = datetime.now()

        if created_on is not None:
            self.created_on = created_on
        else:
            self.created_on = datetime.now()

    def json_format(self):
        jsondata = {}

        def append(name, parameter):
            value = parameter(self)
            if value is not None:
                jsondata[name] = value

        append('id', lambda obj: obj.id)
        append('deed_id', lambda obj: obj.deed_id)
        append('conveyancer_id', lambda obj: obj.conveyancer_id)
        append('status', lambda obj: obj.status)
        append('last_updated',
               lambda obj: serialize_datetime(obj.last_updated))
        append('created_on',
               lambda obj: serialize_datetime(obj.created_on))
        append('case_ref', lambda obj: obj.case_ref)
        append('borrowers', lambda obj: [borrowers.to_json()
                                         for borrowers in obj.borrowers])

        return jsondata

    def object_hook(dct):
        _id = dct.get('id')
        _deed_id = dct.get('deed_id')
        _conveyancer_id = dct.get('conveyancer_id')
        _status = dct.get('status')
        _last_updated = dct.get('last_updated')
        _created_on = dct.get('created_on')
        _case_ref = dct.get('case_ref')

        case = Case(
            _conveyancer_id,
            _deed_id,
        )
        case.id = _id
        case.status = _status
        case.last_updated = parse(_last_updated)
        case.created_on = parse(_created_on)
        case.case_ref = str(_case_ref)

        return case
