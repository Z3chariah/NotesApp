
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, List



app = FastAPI()



class Notes(BaseModel):
    name: str = Field(min_length=20, default='Untitled', description='Name of Note')
    body: str = Field(max_length=100_000, description='Page: Note Body')
    date: str = Field(max_length=8, description="date of todo")


class CreateNote(Notes):
    pass

class UpdateNotes(BaseModel):
    name: Optional[str] = Field(default='Untitled', description='Name of Note')
    body: Optional[str] = Field(max_length=100_000, description='Page: Note Body')
    date: Optional[str] = Field(min_length=8, max_length=8, description="date of todo")

class NoteStructure(Notes):
    identifier: int = Field(description='Unique Identifier of Note')




all_notes = [NoteStructure(name='Pharmacy Tech Module One', identifier=1, body='In this Module we learned about Infectious diseases', date='5/02/25'),
    NoteStructure(name='Pharmacy Tech Module One', identifier=2, body='In this Module we learned about Infectious diseases', date='5/02/25'),
    NoteStructure(name='Pharmacy Tech Module One', identifier=3, body='In this Module we learned about Infectious diseases', date='5/02/25'),
    NoteStructure(name='Pharmacy Tech Module One', identifier=5, body='In this Module we learned about Infectious diseases', date='5/02/25')]



@app.get('/notes', response_model= NoteStructure)
def get_notes():
    return all_notes
