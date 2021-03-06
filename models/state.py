#!/usr/bin/python3
import os
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import *


class State(BaseModel, Base):
    if "HBNB_TYPE_STORAGE" in os.environ \
       and os.environ["HBNB_TYPE_STORAGE"] == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)

    if ("HBNB_TYPE_STORAGE" not in os.environ or
       os.environ["HBNB_TYPE_STORAGE"] != "db"):
        @property
        def cities(self):
            from models import storage
            all_cities = storage.all("City").values()
            return [x for x in all_cities if x.state_id == self.id]
