from sqlalchemy import Column, Integer, Date, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm.collections import InstrumentedList

from database.models import BaseEntityModel


class Assignment(BaseEntityModel):
    __tablename__ = "assignment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    date = Column(Date, ForeignKey("calender.date"))
    tasks: InstrumentedList = relationship("task", lazy="select", cascade="all, delete-orphan")
    comment = Column(String(255))

    def __repr__(self):
        return f"{self.user_date_id} - {self.status}"
