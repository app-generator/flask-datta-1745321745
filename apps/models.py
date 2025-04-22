# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Model-Name(db.Model):

    __tablename__ = 'Model-Name'

    id = db.Column(db.Integer, primary_key=True)

    #__Model-Name_FIELDS__
    field-name-01 = db.Column(db.Text, nullable=True)
    field-name-02 = db.Column(db.String(255),  nullable=True)
    field-name-03 = db.Column(db.Boolean, nullable=True)
    field-name-04 = db.Column(db.Integer, nullable=True)
    field-name-05 = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Model-Name_FIELDS__END

    def __init__(self, **kwargs):
        super(Model-Name, self).__init__(**kwargs)


class Model-Name-02(db.Model):

    __tablename__ = 'Model-Name-02'

    id = db.Column(db.Integer, primary_key=True)

    #__Model-Name-02_FIELDS__
    field-name-01 = db.Column(db.Boolean, nullable=True)
    field-name-02 = db.Column(db.Integer, nullable=True)

    #__Model-Name-02_FIELDS__END

    def __init__(self, **kwargs):
        super(Model-Name-02, self).__init__(**kwargs)



#__MODELS__END
