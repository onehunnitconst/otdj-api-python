from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base

class User(Base):
    __tablename__ = "otdj_tb_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str]
    password: Mapped[str]
    nickname: Mapped[str]
    profile_image: Mapped[Optional[str]]


class Song(Base):
    __tablename__ = "otdj_tb_songs"

    id: Mapped[str] = mapped_column(primary_key=True, autoincrement=False)
    title: Mapped[str]
    cover: Mapped[Optional[str]]
    category: Mapped[str]
    artist: Mapped[str]
    added_date: Mapped[datetime]
    added_version: Mapped[str]

    charts: Mapped[List["Chart"]] = relationship(back_populates="song")


class Chart(Base):
    __tablename__ = "otdj_tb_charts"

    id: Mapped[str] = mapped_column(primary_key=True, autoincrement=False)
    song_id: Mapped[str] = mapped_column(ForeignKey("otdj_tb_charts.id"))
    chart_type: Mapped[str]
    difficulty: Mapped[str]
    level: Mapped[str]
    chart_constant: Mapped[float]
    added_date: Mapped[datetime]
    added_version: Mapped[str]
    
    song: Mapped["Song"] = relationship(back_populates="charts")


class Challenge(Base):
    __tablename__ = "otdj_tb_challenges"

    id: Mapped[int] = mapped_column(primary_key=True)
    song_id: Mapped[str] = mapped_column(ForeignKey("otdj_tb_songs.id"))
    chart_id: Mapped[str] = mapped_column(ForeignKey("otdj_tb_charts.id"))
    user_id: Mapped[str] = mapped_column(ForeignKey("otdj_tb_users.id"))
    challenge_type: Mapped[str]
    challenge_goal: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    completed_at: Mapped[Optional[datetime]]

    song: Mapped["Song"] = relationship()
    chart: Mapped["Chart"] = relationship()
    user: Mapped["User"] = relationship()


class ChallengePack(Base):
    __tablename__ = "otdj_tb_challenge_packs"

    id: Mapped[int] = mapped_column(primary_key=True)
    song_id: Mapped[str] = mapped_column(ForeignKey("otdj_tb_songs.id"))
    author_id: Mapped[str] = mapped_column(ForeignKey("otdj_tb_users.id"))
    name: Mapped[str]
    description: Mapped[str]
    cover_url: Mapped[Optional[str]]
 
    author: Mapped["User"] = relationship()
    items: Mapped[List["ChallengeItem"]] = relationship(back_populates="challenge_pack")

class ChallengeItem(Base):
    __tablename__ = "otdj_tb_challenge_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    challenge_pack_id: Mapped[int] = mapped_column(ForeignKey("otdj_tb_challenge_packs.id"))
    song_id: Mapped[str] = mapped_column(ForeignKey("otdj_tb_songs.id"))
    chart_id: Mapped[str] = mapped_column(ForeignKey("otdj_tb_charts.id"))
    todo_type: Mapped[str]
    todo_goal: Mapped[str]

    challenge_pack: Mapped["ChallengePack"] = relationship()
    song: Mapped["Song"] = relationship()
    chart: Mapped["Chart"] = relationship()