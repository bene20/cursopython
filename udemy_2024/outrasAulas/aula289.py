import json
from typing import TypedDict

class Movie(TypedDict):
    nome: str   
    ano: int
    is_movie: bool
    characters: list[str]

string_movie: Movie = '''
{
    "nome": "O Senhor dos anéis",
    "ano": 2015,
    "is_movie": true,
    "characters": ["Frodo", "Sam", "Gandalf", "Boromir"]
}'''

filme: Movie = json.loads(string_movie)
print(filme['ano'])