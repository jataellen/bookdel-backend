from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Chapter
from models import Book
import csv
# import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Set this to the origin(s) of your client-side code
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def read_csv_file(file_path: str) -> List[Chapter]:
    with open(file_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        chapters = []
        for row in csv_reader:
            chapter = Chapter(
                id=row["id"],
                title=row["title"],
                author=row["author"],
                text=row["text"],
                male_speakers=row["male_speakers"],
                female_speakers=row["female_speakers"],
                male_mentions=row["male_mentions"],
                bechdel=row["bechdel"]
            )
            chapters.append(chapter)
        return chapters

def read_books_csv_file(file_path: str) -> List[Book]:
    with open(file_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        books = []
        for row in csv_reader:
            book = Book(
                id=row["title"],
                title=row["title"],
                male_speakers=row["male_speakers"],
                male_speaker_count=row['male_speaker_count'],
                female_speakers=row["female_speakers"],
                female_speaker_count=row['female_speaker_count'],
                bechdel=row["bechdel"]
            )
            books.append(book)
        return books

db = read_csv_file("corpus.csv")
books_db = read_books_csv_file("books_csv.csv")
# route for get request, / home route
@app.get("/")
async def root():
    return {"Hello": "Jata"}

# route to get all the users
@app.get("/api/chapters")
async def get_chapters():
    return db

# route to get all the users
@app.get("/api/books")
async def get_books():
    return books_db

@app.get("/api/chapters/id/{id}")
async def get_chapter_by_id(id: str):
    return [x for x in db if x.id == id]

@app.get("/api/chapters/title/{title}")
async def get_chapter_by_title(title: str):
    formatted_title = title.replace("-", " ")
    return [x for x in db if x.title.lower() == formatted_title]