# domain/entities.py

from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
