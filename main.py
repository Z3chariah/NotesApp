from os import name
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, List



app = FastAPI()



class Notes(BaseModel):
    note_name: str = Field(min_length=20, default='Untitled', description='Name of Note')
    note_body: str = Field(max_length=100_000, description='Page: Note Body')
    note_date: str = Field(max_length=8, description="date of todo")

class UpdateNotes(BaseModel):
    note_name: Optional[str] = Field(default='Untitled', description='Name of Note')
    note_body: Optional[str] = Field(max_length=100_000, description='Page: Note Body')
    note_date: Optional[str] = Field(min_length=8, max_length=8, description="date of todo")

class NoteStructure(Notes):
    note_identifier: int = Field(description='Unique Identifier of Note')

class CreateNote(Notes):
    pass


all_notes = [NoteStructure(note_name='Pharmacy Tech Module One', note_identifier=1, note_body='In this Module we learned about Infectious diseases', note_date='5/02/25'),
    NoteStructure(note_name='Pharmacy Tech Module One', note_identifier=2, note_body='In this Module we learned about Infectious diseases', note_date='5/02/25'),
    NoteStructure(note_name='Pharmacy Tech Module One', note_identifier=3, note_body='In this Module we learned about Infectious diseases', note_date='5/02/25'),
    NoteStructure(note_name='Pharmacy Tech Module One', note_identifier=5, note_body='In this Module we learned about Infectious diseases', note_date='5/02/25')]



@app.get('/notes/{note_id}', response_model= NoteStructure)
def get_note(note_id: int):
  for note in all_notes:
    if note.note_identifier == note_id:
        return note_id


@app.get('/notes', response_model = List[NoteStructure])
def get_notes(first_n: int):
        if first_n:
            return all_notes[:first_n]
        else: return all_notes

@app.post('/notes', response_model= NoteStructure)
def create_notes(note: CreateNote):
    new_note_id = max(note.note_identifier for note in all_notes) + 1

    new_note = NoteStructure(
                            note_identifier = new_note_id,
                            note_name = note.note_name,
                            note_body = note.note_body,
                            note_date = note.note_date)
    all_notes.append(new_note)
    return all_notes
