from db import db
from typing import List

class MusicModel(db.Model):
    __tablename__ = 'music_recs'

    id = db.Column(db.Integer, primary_key=True)
    song = db.Column(db.String(), nullable=False)
    artist = db.Column(db.String(), nullable=True)
    musics = db.Column(db.JSON(), nullable=True)
    state = db.Column(db.Boolean, default=False)
    ip = db.Column(db.String(), nullable=True)
    agent = db.Column(db.String(), nullable=True)

    @classmethod
    def find_by_ip(cls, ip: str) -> "MusicModel":
        return cls.query.filter_by(ip=ip).all()

    @classmethod
    def find_all(cls) -> List["MusicModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()