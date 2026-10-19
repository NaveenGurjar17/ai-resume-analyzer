from sqlalchemy import Column, Integer, String, Text, ForeignKey
from db import Base, engine


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(255))


class Reports(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    resume_text = Column(Text)
    result = Column(Text)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Tables created")

