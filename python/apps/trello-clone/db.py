from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
    relationship,
    sessionmaker
)

from main import config
print("Config", config)

engine = create_engine('sqlite:///trolli.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)

    boards = relationship("Board", back_populates="user")

    def __repr__(self):
        return f"BoardList(id={self.id!r}, name={self.name!r})"


class Board(Base):
    __tablename__ = "boards"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="boards")

    def __repr__(self):
        return f"Board(id={self.id!r}, name={self.name!r})"


class BoardList(Base):
    __tablename__ = "board_lists"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    board_id = Column(Integer, ForeignKey("boards.id"), nullable=False)

    def __repr__(self):
        return f"BoardList(id={self.id!r}, name={self.name!r})"


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


def addNewBoard(session, boardName):
    """adds a new board to the db"""
    user = User(name="Owen")
    session.add(user)
    session.commit()
    session.refresh(user)
    board = (
        session.query(Board)
        .filter(Board.name == boardName)
        .one_or_none()
    )
    if board is not None:
        print("board already exists")
        return
    board = Board(name=boardName, user_id=user.id)
    session.add(board)
    session.commit()


addNewBoard(session, "test")
addNewBoard(session, "test")
