from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Chapter(BaseModel):
    id: str
    title: str
    author: str
    text: str
    male_speakers: str
    female_speakers: str
    male_mentions: str
    bechdel: str

class Book(BaseModel):
    id: str
    title: str
    male_speakers: str
    male_speaker_count: int
    female_speakers: str
    female_speaker_count: int
    bechdel: str

